from fastapi.testclient import TestClient
from fastapi import FastAPI, Request, HTTPException

from app.main import app

with TestClient(app) as client:

    response = client.get("/health")

    print(f"Status Code--->: {response.status_code}")
    print(f"Response: {response.json()}")

with TestClient(app) as client:

    response = client.post(
        "/predict",
        json={
            # "text": "NASA launched a new spacecraft"
            "text": "The baseball team won the championship"
        }
    )

    print(f"Status Code--->: {response.status_code}")
    print(f"Response: {response.json()}")
    