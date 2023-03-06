# __Prueba_Tecnica Readme__

## __Descripción__

Este repositorio contiene una prueba técnica para sistemas inteligentes. La aplicación está implementada usando Python 3.9.5,el framework FastAPI 0.92.0 y requiere una base de datos PostgreSQL en su version 15.

## __Clonar el repositorio__

Primero, clone este repositorio usando el siguiente comando y ubique la consola en la carpeta del repositorio:
~~~
git clone https://github.com/Brayhanzuluaga/Prueba_Tecnica.git
~~~

## __Estructura de carpetas y archivos__

La estructura de las carpetas y archivos es de la siguiente manera: 
~~~
+ Prueba_Tecnica
    + app
        init.py
        database.py
        config.py
        + Events 
            models.py
            shemas.py
            repository.py
            routes.py
    main.py
    README.md
    requeriments.txt
    examples.json
    static_example.py
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
Descargue e instale PostgreSQL 15 desde el siguiente enlace:
https://www.postgresql.org/download/

## __Configurar la base de datos__
Inicialice la aplicacion de postgres, luego en dicha aplicacion crea y nombra la base de datos, finalmente inicializa la base de datos utilizando la siguiente URL que se encuentra en script config.py:
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

## __Pruebas de eventos Estáticos__

Para llevar a cabo las pruebas estáticas, se utiliza un archivo llamado Examples.json que contiene ejemplos iniciales por defecto. Es importante mencionar que el siguiente script solo debe ejecutarse una sola vez y antes de generar otra petición POST.

Para llevar a cabo las pruebas, se debe abrir otra terminal y ejecutar el siguiente comando:
~~~
python .\static_example.py
~~~

Este script generará varias peticiones POST y una petición GET, las cuales serán registradas en la tabla de la base de datos del  loc. De esta manera, se podrán realizar pruebas estáticas sobre el comportamiento del sistema en diferentes situaciones.

---


## __Especificación de campos del objeto "Evento"__

El objeto "Evento" tiene los siguientes campos:

 - __"id"__: Identificador numérico del evento, representado por un entero (int).

 - __"eventName"__: Nombre del evento, representado por una cadena de caracteres (str).

 - __"eventType"__: Tipo de evento, representado por una cadena de caracteres (str).

 - __"eventDescription"__: Descripción del evento, representado por una cadena de caracteres (str).

 - __"eventCheck"__: Estado del evento, representado por un valor booleano (bool). Puede ser "Pendiente por revisar" (True) o "Revisado" (False).

 - __"date"__: Fecha del evento, representada por un objeto de tipo datetime.

 - __"management"__: Tipo de gestión requerida para el evento, representado por un entero (int). Puede ser "Sin revisar" (0), "Requiere gestión" (1), o "Sin gestión" (2).

Cada campo del objeto "Evento" tiene un tipo de dato específico, como se indica en la descripción de cada campo. Estos campos son utilizados para almacenar información sobre los eventos, como su nombre, fecha, estado, etc.