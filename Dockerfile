FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* requirements.txt* ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ ./src/
COPY data/ ./data/
COPY src/models/airquality-pm25-wekerom-model.pth ./src/models/airquality-pm25-wekerom-model

ENV PYTHONPATH=/app/src

EXPOSE 8000

CMD ["uvicorn", "src.api.routes:app", "--host", "0.0.0.0", "--port", "8000"]
