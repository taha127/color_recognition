from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
import pickle
import numpy as np
import json
from datetime import datetime
import pickle
from services.color_math import linear_to_xyz, srgb_to_linear
from colormath.color_objects import LabColor
from services.app_paths import get_app_data_dir
from PySide6.QtGui import QImage
import cv2
import os


PROFILE_DIR = get_app_data_dir() / "profiles"
PROFILE_DIR.mkdir(parents=True, exist_ok=True)


def create_recognition_model(samples_xyz, samples_lab):

    X = np.array(samples_xyz)
    Y = np.array(samples_lab)

    model = Pipeline([
        ("poly", PolynomialFeatures(degree=2, include_bias=False)),
        ("ridge", Ridge(alpha=0.01))
    ])

    model.fit(X, Y)

    return model


def save_profile(name, xyz, lab, model: Pipeline):

    # -------------------- Convert numpy ---------------------
    xyz = [list(x) for x in xyz]
    lab = [l.tolist() if hasattr(l, "tolist") else l for l in lab]

    # --------------------- Save model with pickle ---------------------
    model_path = PROFILE_DIR / f"{name}.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    # --------------------- Save profile metadata ---------------------
    meta = {
        "name": name,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "samples_xyz": xyz,
        "samples_lab": lab,
        "model": model_path.name
    }
    meta_path = PROFILE_DIR / f"{name}.json"
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=4)


def delete_profile_by_name(profile_name: str):
    """
    Delete profile json and model file completely
    """

    json_path = os.path.join(PROFILE_DIR, f"{profile_name}.json")
    model_path = os.path.join(PROFILE_DIR, f"{profile_name}.pkl")

    # Delete JSON
    if os.path.exists(json_path):
        os.remove(json_path)

    # Delete Model
    if os.path.exists(model_path):
        os.remove(model_path)


def load_profiles():

    profiles = []

    for file in PROFILE_DIR.glob("*.json"):
        with open(file, "r") as f:
            data = json.load(f)
            profiles.append(data)

    return profiles


def predict_color(model: Pipeline, roi_qimage):

    # ---- Convert QImage to numpy ----
    roi_qimage = roi_qimage.convertToFormat(QImage.Format_RGB888)
    w = roi_qimage.width()
    h = roi_qimage.height()

    ptr = roi_qimage.bits()
    ptr.setsize(h * w * 3)
    arr = np.array(ptr, dtype=np.uint8).reshape((h, w, 3))

    # ---- Apply median blur ----
    arr = cv2.medianBlur(arr, 41)

    # ---- Mean RGB ----
    mean_rgb = arr.mean(axis=(0, 1))

    # ---- RGB → XYZ ----
    lin = srgb_to_linear(mean_rgb)
    xyz = linear_to_xyz(lin)

    # ---- Predict ----
    lab_pred = model.predict([xyz])[0]

    return LabColor(*lab_pred)


def load_profile_model(profile_meta):

    model_path = PROFILE_DIR / profile_meta["model"]
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    return model
