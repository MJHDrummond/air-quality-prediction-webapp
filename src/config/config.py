import os


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__))))
MODEL_PATH = os.path.join(
    PROJECT_ROOT, "src/models/airquality-pm25-wekerom-model.pth")
CSV_PATH = os.path.join(PROJECT_ROOT, "data/airquality-wekerom.csv")
WINDOW_SIZE = 7
