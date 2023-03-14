import json
import requests


# URL del endpoint para el post
urlpost = "http://127.0.0.1:8000/event/create"
# URL del endpoint para el get
urlget = "http://127.0.0.1:8000/events"
# Extrae los ejempos en formato json
f = open('examples.json')
data = json.load(f)


def example_create(examples: list, url: str):
    for example in examples:
        # Hacer la petición POST con los datos del evento
        response = requests.post(url, json=example)
        # Verificar si la petición fue exitosa
        print(response.status_code)
        print(example)
        if response.status_code == 200:
            print("La petición post fue exitosa")
        else:
            print("Ocurrió un error al hacer la petición post")


example_create(data, urlpost)
response = requests.get(urlget)
# Verificar si la petición fue exitosa
if response.status_code == 200:
    print("La petición get fue exitosa")
else:
    print("Ocurrió un error al hacer la petición get")
