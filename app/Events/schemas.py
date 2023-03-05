from typing import Optional, Generic, TypeVar
from datetime import datetime
from pydantic.generics import GenericModel
from pydantic import BaseModel, Field

# Función que se usa para crear un tipo genérico en tiempo de compilación
T = TypeVar('T')


# La clase "EventSchema" define una estructura de datos para representar un evento
class EventSchema(BaseModel):
    id: Optional[int] = None
    eventName: Optional[str] = None
    eventType: Optional[str] = None
    eventDescription: Optional[str] = None
    eventCheck: Optional[bool] = None
    date: Optional[datetime] = None

    class Config:
        orm_mode = True


# La clase "LogSchema" define una estructura de datos para representar un log
class LogSchema(BaseModel):
    id: Optional[int] = None
    msg: Optional[str] = None
    date: Optional[datetime] = None
    level: Optional[str] = None

    class Config:
        orm_mode = True


# Esta clase define un modelo de datos llamado "EventManagement"
# que especifica los campos que pueden estar presentes en una instancia del modelo
class EventManagement(BaseModel):
    id: Optional[int] = None
    eventName: Optional[str] = None
    eventType: Optional[str] = None
    eventDescription: Optional[str] = None
    eventCheck: Optional[bool] = None
    date: Optional[datetime] = None
    management: Optional[int] = None

    class Config:
        orm_mode = True


# La clase RequestEvent es una clase que representa un modelo de datos
# utilizado para recibir una solicitud HTTP que contiene información sobre un evento.
class RequestEvent(BaseModel):
    parameter: EventSchema = Field(...)


# La clase RequestEventManagement es un modelo que se utiliza para definir
# los campos y tipos de datos de una solicitud para crear o actualizar un evento en el sistema.
class RequestEventManagement(BaseModel):
    parameter: EventManagement = Field(...)


# La clase Response es una clase genérica que representa una respuesta HTTP de una API.
class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


# La clase Request es una clase genérica que se utiliza para representar una solicitud
# que contiene un parámetro de cualquier tipo T.
class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)
