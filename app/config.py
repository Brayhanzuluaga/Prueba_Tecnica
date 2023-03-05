# La función "get_url" devuelve la cadena de conexión a la base de datos "EventDB2".
# En este caso, la cadena de conexión especifica el usuario y la contraseña para acceder a la base de datos,  #noqa
# así como la dirección del servidor y el puerto utilizado para conectarse a la base de datos.
def get_url():
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1214734456@localhost:5432/EventDB2"
    return SQLALCHEMY_DATABASE_URL
