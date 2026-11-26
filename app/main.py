
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
import joblib


MODEL_PATH = "artifacts/classifier.joblib"


@asynccontextmanager
async def lifespan(app: FastAPI):

    app.state.model = joblib.load(MODEL_PATH)

    print("ML model loaded successfully!")

    yield

    app.state.model = None


app = FastAPI(
    title="News Category Classifier",
    version="1.0.0",
    lifespan=lifespan
)


class PredictionRequest(BaseModel):
    text: str = Field(min_length=1)


class PredictionResponse(BaseModel):
    prediction: str


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(
    request: Request,
    payload: PredictionRequest
):

    model = request.app.state.model

    try:
        prediction = model.predict([payload.text])

        return PredictionResponse(
            prediction=str(prediction[0])
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )
