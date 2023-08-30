from fastapi.testclient import TestClient
from main import app
import random

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Api funcionando correctamente",
        "Link del repositorio": "https://github.com/Brayhanzuluaga/Prueba_Tecnica"}


def test_get_logs():
    response = client.get("/log")
    assert response.status_code == 200


def test_get_events():
    response = client.get("/events")
    assert response.status_code == 200


def test_create_item():
    id = random.randint(0, 1000)
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