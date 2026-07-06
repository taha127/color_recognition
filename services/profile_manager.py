import json
import shutil
from datetime import datetime
from pathlib import Path
from services.app_paths import get_app_data_dir
import os


class ProfileManager:

    def __init__(self):
        self.profiles_dir = get_app_data_dir() / "profiles"
        self.profiles_dir.mkdir(exist_ok=True)
        self.settings_file = get_app_data_dir() / "settings" / "profiles.json"
        self.settings_file.parent.mkdir(exist_ok=True)

        if not self.settings_file.exists():
            self.save(
                {
                    "current": None,
                    "profiles": []
                }
            )

    def load(self):
        with open(self.settings_file, encoding="utf8") as f:
            return json.load(f)

    def save(self, data):
        with open(self.settings_file, "w", encoding="utf8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def add_profile(self, filepath, name):
        data = self.load()
        src = Path(filepath)
        dst = self.profiles_dir / src.name
        shutil.copy2(src, dst)
        data["profiles"] = [p for p in data["profiles"] if p["name"] != name]
        data["profiles"].append({
            "name": name,
            "path": str(dst),
            "saved_at": datetime.now().timestamp()
        })
        data["current"] = name
        self.save(data)

    def current_profile(self):
        data = self.load()
        current = data["current"]
        if current is None:
            return None

        for profile in data["profiles"]:

            if profile["name"] == current:
                return profile

        return None

    def set_current(self, name):
        data = self.load()
        data["current"] = name
        self.save(data)

    def last_profiles(self, count=3):
        data = self.load()

        profiles = sorted(
            data["profiles"],
            key=lambda p: p["saved_at"],
            reverse=True
        )
        return profiles[:count]

    def remove_profile(self, name):
        data = self.load()

        profile = next((p for p in data["profiles"] if p["name"] == name), None)

        if profile is None:
            return

        if os.path.exists(profile["path"]):
            os.remove(profile["path"])

        data["profiles"] = [
            p for p in data["profiles"]
            if p["name"] != name
        ]

        if data["current"] == name:
            data["current"] = None

        self.save(data)
