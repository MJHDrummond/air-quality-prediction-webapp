from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.schemas.prediction_request import PredictRequest
from src.schemas.prediction_response import PredictResponse
from src.services.model_service import ModelService

app = FastAPI(title='Air Quality Prediction API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["OPTIONS", "GET", "POST"],
    allow_headers=["Content-Type"],
)

model_service = ModelService()


@app.post('/predict', response_model=PredictResponse)
def predict_pm25(req: PredictRequest):
    prediction = model_service.predict(req.features)
    return PredictResponse(pm25=prediction)
