import json
import datetime
import os
from services.app_paths import get_app_data_dir


class ColorHistoryService:

    saved_colors_file_path = (
        get_app_data_dir() / "color_history" / "saved_colors.json"
    )

    def __init__(self):

        self._ensure_directory()

    def _ensure_directory(self):
        if not self.saved_colors_file_path.parent.exists():
            self.saved_colors_file_path.parent.mkdir(
                parents=True, exist_ok=True)

    def load_saved_colors(self):
        if not os.path.exists(self.saved_colors_file_path):
            return []

        try:
            with open(self.saved_colors_file_path, "r", encoding="utf-8") as f:
                return json.load(f)

        except (json.JSONDecodeError, IOError) as e:
            return []

    def save_color(self, name: str, hex_code: str):

        colors = self.load_saved_colors()

        new_entry = {
            "name": name,
            "hex": hex_code,
            "saved_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        colors.append(new_entry)

        with open(self.saved_colors_file_path, "w", encoding="utf-8") as f:
            json.dump(colors, f, indent=4, ensure_ascii=False)

        return new_entry

    def delete_color_by_name(self, name: str):

        colors = self.load_saved_colors()
        print(name)
        colors = [c for c in colors if c["name"] != name]

        with open(self.saved_colors_file_path, "w", encoding="utf-8") as f:
            json.dump(colors, f, indent=4, ensure_ascii=False)

    def rename_color(self, old_name: str, new_name: str):

        colors = self.load_saved_colors()
        for color in colors:
            if color["name"] == old_name:
                color["name"] = new_name
                break

        with open(self.saved_colors_file_path, "w", encoding="utf-8") as f:
            json.dump(colors, f, indent=4, ensure_ascii=False)
