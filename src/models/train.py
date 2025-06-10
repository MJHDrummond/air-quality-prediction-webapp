import torch
import torch.optim as optim
import numpy as np

from src.models.air_quality_regressor import AirQualityRegressor
from src.ingestion.data_loader import load_data
from src.config import config as config

df = load_data(config.CSV_PATH)

pm25_values = df["pm25_daily_mean"].to_numpy()

X = []
y = []

window_size = config.WINDOW_SIZE

for i in range(len(pm25_values) - window_size):
    window = pm25_values[i:i+window_size]
    target = pm25_values[i+window_size]

    if not np.isnan(window).any() and not np.isnan(target):
        X.append(window)
        y.append(target)

X = np.array(X).astype(np.float32)
y = np.array(y).astype(np.float32).reshape(-1, 1)

print(f"Dataset size: X = {X.shape}, y = {y.shape}")

model = AirQualityRegressor(input_dim=window_size)
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = torch.nn.MSELoss()

for epoch in range(50):
    model.train()
    inputs = torch.from_numpy(X)
    targets = torch.from_numpy(y)

    outputs = model(inputs)
    loss = loss_fn(outputs, targets)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 5 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item()}")

torch.save(model.state_dict(), config.MODEL_PATH)
print(f"Model saved to {config.MODEL_PATH}")
