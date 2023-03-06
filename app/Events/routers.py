from typing import Optional
from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from app.Events import repository
from app.Events.schemas import RequestEvent, Response, RequestEventManagement
from app.database import get_db

router = APIRouter()


# Peticion Post que crea eventos validando que el evento no se haya creado previamente.
@router.post("/event/create")
async def create_event_service(request: RequestEvent,
                               db: Session = Depends(get_db)):
    """
    Peticion Post que crea eventos
    validando que el evento no se haya creado previamente.
    """
    try:
        repository.create_event(db, event=request.parameter)
        repository.create_log(
            db,
            f'El evento con id {request.parameter.id} y nombre {request.parameter.eventName} se creo correctamente',  #noqa
            "Info")
        return Response(
            status="Ok", code="200",
            message="Event created successfully").dict(exclude_none=True)
    except Exception:
        db.rollback()
        repository.create_log(
            db,
            f'El evento con id {request.parameter.id} fue previemente creado',  #noqa
            "Error")
        return Response(
            status="FAIL", code="400",
            message="Event id previously created").dict(exclude_none=True)


# Peticion Get que devuelve una lista de eventos
# utilizando parámetros opcionales para paginar los resultados.
@router.get("/events")
async def get_event(skip: int = 0,
                    limit: int = 100,
                    db: Session = Depends(get_db)):
    """
    Peticion Get que devuelve una lista de eventos
    utilizando parámetros opcionales para paginar los resultados.
    """
    _events = repository.get_event(db)
    return Response(status="Ok",
                    code="200",
                    message="Success fetch all data",
                    result=_events)


# Peticion Get que devuelve una lista del log de los eventos
# utilizando parámetros opcionales para paginar los resultados.
@router.get("/log")
async def eventLogInfo(skip: int = 0,
                       limit: int = 100,
                       db: Session = Depends(get_db)):
    """
    Peticion Get que devuelve una lista del log de los eventos
    utilizando parámetros opcionales para paginar los resultados.
    """
    _logs = repository.get_event_log(db)
    return Response(status="Ok",
                    code="200",
                    message="Success fetch all data",
                    result=_logs)


# Peticion Get que devuelve una lista de eventos filtrados
# clasificandolos en revisado o sin revisar
# ademas de clasificar en requiere gestion o sin gestion
# utilizando parámetros opcionales para dicho filtrado.
@router.get("/events/management")
async def get_event_management(request: Request,
                               eventCheck: Optional[bool] = None,
                               management: Optional[int] = None,
                               db: Session = Depends(get_db)):
    """

    Peticion Get que devuelve una lista de eventos filtrados
    clasificandolos en revisado o sin revisar
    ademas de clasificar en requiere gestion o sin gestion
    utilizando parámetros opcionales para dicho filtrado.

    Ejemplo de filtrado: http://127.0.0.1:8000/events/management?eventCheck=True&management=2
    """
    if request.query_params:
        return Response(status="Ok",
                        code="200",
                        message="Success fetch all data ",
                        result=repository.get_event(db,
                                                    **request.query_params))
    else:
        return Response(status="Ok",
                        code="200",
                        message="Success fetch all data ",
                        result=repository.get_event(db))


# Peticion Get que devuelve el evento indicado mediante el id
# utilizando parámetros opcionales para paginar los resultados.
@router.get("/event/{id}")
async def get_event_id(id: int, db: Session = Depends(get_db)):
    """
    Peticion Get que devuelve el evento indicado mediante el id
    utilizando parámetros opcionales para paginar los resultados.
    """
    try:
        _event = repository.get_event_by_id(db, id)
        if _event.state is False:
            return Response(status="FAIL",
                            code="404",
                            message="Event previously deleted")
        return Response(status="Ok",
                        code="200",
                        message="Success get  data",
                        result=_event)
    except Exception:
        raise HTTPException(
            status_code=404,
            detail=f"El usuario con id {id} no existe en la base de datos")


# Peticion Patch que actualiza el evento indicado.
@router.patch("/event/update")
async def update_event_service(request: RequestEventManagement,
                               db: Session = Depends(get_db)):
    """
    Peticion Patch que actualiza el evento indicado.
    """
    try:
        _event = repository.get_event_by_id(db, request.parameter.id)
        if _event.state is False:
            db.rollback()
            repository.create_log(
                db,
                f'Consulta del evento con id {_event.id} fallida ya que fue eliminada previamente',
                "Error")
            return Response(status="FAIL",
                            code="404",
                            message="Event previously deleted")
        _event = repository.update_event(
            db,
            event_id=request.parameter.id,
            eventName=request.parameter.eventName,
            eventType=request.parameter.eventType,
            eventDescription=request.parameter.eventDescription,
            eventCheck=request.parameter.eventCheck,
            date=request.parameter.date,
            management=request.parameter.management)
        repository.create_log(
            db, f'Evento de id {_event.id} actualizado correctamente', "Info")
        _event.id = _event.id
        return Response(status="Ok",
                        code="200",
                        message="Event updated successfully",
                        result=_event).dict(exclude_none=True)
    except Exception:
        db.rollback()
        repository.create_log(
            db,
            f'Actualizacion fallida, el usuario con id {request.parameter.id} no existe en la base de datos',  #noqa
            "Error")
        raise HTTPException(
            status_code=404,
            detail=f'El usuario con id {request.parameter.id} no existe en la base de datos'
        )


# Peticion Delete que elimina permanentemente el evento indicado de la base de datos.
@router.delete("/event/permanentlydeleted/{id}")
async def permanentlydeleted(id: int, db: Session = Depends(get_db)):
    """
    Peticion Delete que elimina permanentemente el evento indicado de la base de datos.
    """
    repository.remove_event(db, event_id=id)
    repository.create_log(
        db,
        f'El evento con id {id} fue eliminado permanentemente de manera exitosa',
        "Info")
    return Response(status="Ok", code="200",
                    message="Success delete data").dict(exclude_none=True)


# Peticion Delete que elimina (soft destroy) el evento indicado.
@router.delete("/event/delete/{id}")
async def softdelete(id: int, db: Session = Depends(get_db)):
    """
    Peticion Delete que elimina (soft destroy) el evento indicado.
    """
    try:
        repository.softremove_event(db, event_id=id)
    except Exception:
        repository.create_log(
            db, f'El evento con id {id} no existe en la base de datos',
            "Error")
        return Response(
            status="Fail",
            code="404",
            message=f'El evento con id {id} no existe en la base de datos'
        ).dict(exclude_none=True)
    repository.create_log(
        db, f'El evento con id {id} fue eliminado de manera exitosa', "Info")
    return Response(status="Ok", code="200",
                    message="Success delete data").dict(exclude_none=True)
