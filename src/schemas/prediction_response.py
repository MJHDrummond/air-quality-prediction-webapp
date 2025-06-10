from pydantic import BaseModel


class PredictResponse(BaseModel):
    pm25: float
