import torch

from src.models.air_quality_regressor import AirQualityRegressor


def test_model_forward():
    model = AirQualityRegressor(input_dim=7)
    x = torch.randn(1, 7)
    y = model(x)
    assert y.shape == (1, 1)