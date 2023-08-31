from fastapi.testclient import TestClient
from main import app
import random

client = TestClient(app)


# Prueba unitaria que valida si la url principal esta funcionando
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Api funcionando correctamente",
        "Link del repositorio": "https://github.com/Brayhanzuluaga/Prueba_Tecnica"}


# Prueba unitaria que valida funcionamiento de la peticion de los logs
def test_get_logs():
    response = client.get("/log")
    assert response.status_code == 200


# Prueba unitaria que valida funcionamiento de la peticion de los eventos
def test_get_events():
    response = client.get("/events")
    assert response.status_code == 200


# Prueba unitaria que valida funcionamiento del error en la peticion de un evento que no existe
def test_get_nonexistent_event_id():
    id = random.randint(0, 10000)
    response = client.get(f"/event/{id}")
    assert response.status_code == 404
    assert response.json() == {"detail": f"The user with id {id} does not exist in the database"}


# Prueba unitaria que valida funcionamiento de la creacion de un evento
def test_create_item():
    id = random.randint(0, 10000)
    response = client.post(
        "/event/create",
        json={
            "parameter": {
                "id": id,
                "eventName": "string",
                "eventType": "string",
                "eventDescription": "string",
                "eventCheck": True,
                "date": "2023-08-30T21:09:00.170Z"}},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Event created successfully"}


# Prueba unitaria que valida funcionamiento del error en la creacion de un evento que existe
def test_create_existing_item():
    response = client.post(
        "/event/create",
        json={
            "parameter": {
                "id": 8,
                "eventName": "string",
                "eventType": "string",
                "eventDescription": "string",
                "eventCheck": True,
                "date": "2023-08-30T21:09:00.170Z"}},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Event previously created"}


# Prueba unitaria que valida funcionamiento del filtrado por Requiere Gestión / Sin Gestión.
def test_get_events_management():
    response = client.get("/events/management?eventCheck=True&management=7")
    assert response.status_code == 404
    assert response.json() == {"detail": "Type of management required for the event, represented by an integer (int). It can be No review (0), Management required (1), or No management (2)."} #noqa