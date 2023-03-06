from datetime import datetime
from sqlalchemy.orm import Session
from app.Events.models import Event
from app.Events.schemas import EventSchema
from app.database import engine
from app.Events.models import Log
from app.Events import models


# La función se encarga de crear todas las tablas definidas en los modelos de la base de datos,
def create_tables():
    models.Base.metadata.create_all(bind=engine)


# La función "check" toma un argumento booleano llamado "eventcheck"
# devuelve una cadena que indica si el evento asociado ha sido revisado o no.
def check(eventcheck: bool):
    if eventcheck:
        check = "Revisado"
    if not eventcheck:
        check = "No revisado"
    return check


# Esta función se encarga de obtener una lista de eventos desde la base de datos
# Utilizando SQLAlchemy como ORM, y filtra aquellos eventos que tengan el estado en True.
def get_event(db: Session, **filters):
    filters["state"] = True
    eventsFilter = db.query(Event).filter_by(**filters).all()
    for i in list(eventsFilter):
        i.management_str = check_management(i.management)
        i.eventCheck_str = check(i.eventCheck)
    return eventsFilter


# La función utiliza la sesión de base de datos para realizar una consulta en la tabla "Log".
# luego, devuelve una lista de todos los resultados que cumplen con las condiciones de búsqueda especificadas.  #noqa
def get_event_log(db: Session, skip: int = 0, limit: int = 100, **filters):
    return db.query(Log).filter_by(**filters).all()


# Esta función se encarga de obtener un evento específico de la base de datos,
# Utilizando el ID del evento como parámetro de entrada.
def get_event_by_id(db: Session, Event_id: int):
    event = db.query(Event).filter(Event.id == Event_id).first()
    event.management_str = check_management(event.management)
    event.eventCheck_str = check(event.eventCheck)
    return event


# Esta función se encarga de crear un nuevo evento en la base de datos.
def create_event(db: Session, event: EventSchema):
    event_check = event.eventCheck if event.eventCheck is not None else False
    _Event = Event(id=event.id,
                   eventName=event.eventName,
                   eventType=event.eventType,
                   eventDescription=event.eventDescription,
                   eventCheck=event_check,
                   date=event.date,
                   state=True,
                   management=0)
    db.add(_Event)
    db.commit()
    db.refresh(_Event)
    return _Event


# La función crea un nuevo objeto "Log" con el mensaje y nivel de registro especificados,
# así como la fecha y hora actual.
def create_log(db: Session, message: str, level: str):
    _Log = Log(msg=message, level=level, date=datetime.now())
    db.add(_Log)
    db.commit()
    db.refresh(_Log)
    return _Log


# La función toma un argumento entero llamado "management"
# devuelve una cadena que indica el estado de gestión del objeto correspondiente.
def check_management(management: int):
    if management == 0:
        return "Sin revisar"
    elif management == 1:
        return "Requiere gestión"
    elif management == 2:
        return "Sin gestión"
    else:
        return "Ingresa 1 en el parametro management para indicar que requiere gestion o 2 para indicar que no requiere gestion"  #noqa


# Esta función se encarga de eliminar un evento de la base de datos.
def remove_event(db: Session, event_id: int):
    _Event = get_event_by_id(db=db, Event_id=event_id)
    db.delete(_Event)
    db.commit()


# Esta función se encarga de realizar una eliminación suave o lógica
# de un evento de la base de datos,
# Es decir, en lugar de eliminar el evento de forma definitiva,
# se cambia su estado a "inactivo" o "no válido".
def softremove_event(db: Session, event_id: int):
    _Event = get_event_by_id(db=db, Event_id=event_id)
    _Event.state = False
    db.commit()
    db.refresh(_Event)


# Esta función se encarga de actualizar un evento existente
# en la base de datos con los nuevos valores proporcionados.
def update_event(db: Session, event_id: int, eventName: str, eventType: str,
                 eventDescription: str, eventCheck: str, date: datetime,
                 management: bool):
    _Event = get_event_by_id(db=db, Event_id=event_id)
    _Event.eventName = eventName
    _Event.eventType = eventType
    _Event.eventDescription = eventDescription
    _Event.eventCheck = eventCheck
    _Event.date = date
    _Event.management = management
    db.commit()
    db.refresh(_Event)
    return _Event
