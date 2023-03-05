# Prueba_Tecnica Readme

## Descripción

Este repositorio contiene una prueba técnica para sistemas inteligentes. La aplicación está implementada usando FastAPI y requiere una base de datos PostgreSQL.

## Clonar el repositorio

Primero, clone este repositorio usando el siguiente comando y ubique la consola en la carpeta del repositorio:
~~~
git clone https://github.com/Brayhanzuluaga/Prueba_Tecnica.git
~~~

## Crear el ambiente virtual

Luego, cree un ambiente virtual y actívelo con los siguientes comandos:
~~~
python -m venv prueba_tecnica

<path_to_env>\Scripts\activate.bat 
~~~

## Instalar dependencias
Para instalar las dependencias necesarias, ejecute el siguiente comando:
~~~
pip install -r requirements.txt
~~~
## Descargar e instalar Postgres
Descargue e instale PostgreSQL desde el siguiente enlace:
https://www.postgresql.org/download/

## Configurar la base de datos
Inicialice la base de datos utilizando la siguiente URL:
~~~
SQLALCHEMY_DATABASE_URL = "postgresql://[usuario]:[contraseña]@localhost:[puerto]/[Nombre_Base_de_datos]"
~~~
Reemplace los valores entre corchetes con su propio usuario, contraseña, puerto y nombre de la base de datos.

## Inicializar la aplicación

Para iniciar la aplicación, ejecute el siguiente comando en la terminal:
~~~
uvicorn main:app --reload
~~~
Después de unos segundos, la aplicación debería estar funcionando.

## Obtener la documentación

Para obtener la documentación de las peticiones, puede utilizar dos formatos:

### Para Swagger:
~~~ 
http://127.0.0.1:8000/docs
~~~
### Para formato alternativo:
~~~
http://127.0.0.1:8000/redoc
~~~