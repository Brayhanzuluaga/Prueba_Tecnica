# __Prueba_Tecnica Readme__

## __Descripción__

Este repositorio contiene una prueba técnica para sistemas inteligentes. La aplicación está implementada usando FastAPI y requiere una base de datos PostgreSQL.

## __Clonar el repositorio__

Primero, clone este repositorio usando el siguiente comando y ubique la consola en la carpeta del repositorio:
~~~
git clone https://github.com/Brayhanzuluaga/Prueba_Tecnica.git
~~~

## __Crear el ambiente virtual__

Luego, cree un ambiente virtual y actívelo con los siguientes comandos:
~~~
python -m venv prueba_tecnica

<path_to_env>\Scripts\activate.bat 
~~~

## __Instalar dependencias__
Para instalar las dependencias necesarias, ejecute el siguiente comando:
~~~
pip install -r requirements.txt
~~~
## __Descargar e instalar Postgres__
Descargue e instale PostgreSQL desde el siguiente enlace:
https://www.postgresql.org/download/

## __Configurar la base de datos__
Inicialice la base de datos utilizando la siguiente URL que se encuentra en script config.py:
~~~
SQLALCHEMY_DATABASE_URL = "postgresql://[usuario]:[contraseña]@localhost:[puerto]/[Nombre_Base_de_datos]"
~~~
Reemplace los valores entre corchetes con su propio usuario, contraseña, puerto y nombre de la base de datos.

## __Inicializar la aplicación__

Para iniciar la aplicación, ejecute el siguiente comando en la terminal:
~~~
uvicorn main:app --reload
~~~
Después de unos segundos, la aplicación debería estar funcionando.

## __Obtener la documentación__

Para obtener la documentación de las peticiones, puede utilizar dos formatos:

### __Para Swagger:__
~~~ 
http://127.0.0.1:8000/docs
~~~
### __Para formato alternativo:__
~~~
http://127.0.0.1:8000/redoc
~~~

---