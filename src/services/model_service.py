import os

import torch
import sys

from src.models.air_quality_regressor import AirQualityRegressor
from src.config import config as config


class ModelService:
    def __init__(self):
        print(sys.path)
        self.model = AirQualityRegressor(input_dim=config.WINDOW_SIZE)
        self.model.load_state_dict(torch.load(config.MODEL_PATH))
        self.model.eval()

    def predict(self, features):
        if len(features) != config.WINDOW_SIZE:
            raise ValueError(f"Expected exactly 7 input features "
                             f"(previous 7 days PM2.5), "
                             f"got {len(features)}")
        with torch.no_grad():
            input_tensor = torch.tensor(features).float().unsqueeze(0)
            output = self.model(input_tensor)
            return output.item()
