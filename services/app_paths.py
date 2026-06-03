import os
from pathlib import Path

APP_NAME = "ColorRecognitionApp"


def get_app_data_dir() -> Path:
    base = Path(os.getenv("APPDATA"))
    app_dir = base / APP_NAME
    app_dir.mkdir(parents=True, exist_ok=True)
    return app_dir
