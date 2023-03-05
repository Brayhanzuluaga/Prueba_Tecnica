from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import get_url

# La función "create_engine" es una función del paquete SQLAlchemy que se utiliza para crear un objeto Engine, #noqa
# que es responsable de establecer y administrar la conexión a una base de datos.
engine = create_engine(get_url())

# Se crea una sesión local utilizando un objeto Engine que se especifica en el argumento "bind".
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Se crea una clase base de modelo declarativo, que se utiliza para definir clases que representan tablas en la base de datos.  #noqa
Base = declarative_base()


# La función devuelve un generador que proporciona una sesión de base de datos (objeto Session) a la que se puede acceder desde dentro del contexto del generador.  #noqa
# La sesión de la base de datos se crea mediante la función "SessionLocal()" que se define en otra parte del código.  #noqa
def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
