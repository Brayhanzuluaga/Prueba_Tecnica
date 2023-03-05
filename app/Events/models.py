from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime


# La clase Event es una definición de modelo de datos que representa un evento en una base de datos.
class Event(Base):
    __tablename__ = "event"
    id = Column(Integer, primary_key=True)
    eventName = Column(String)
    eventType = Column(String)
    eventDescription = Column(String)
    date = Column(DateTime)
    eventCheck = Column(Boolean)
    state = Column(Boolean)
    management = Column(Integer)


# Definición del modelo de registro
class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, index=True)
    level = Column(String(10))
    msg = Column(String)
    date = Column(DateTime)
