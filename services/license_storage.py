from pathlib import Path
from typing import Optional

from services.app_paths import get_app_data_dir
from services.crypto_utils import CryptoUtils


class LicenseStorage:
    """
    Stores and loads encrypted license information.
    """

    FILE_NAME = "license.dat"

    @classmethod
    def _file_path(cls) -> Path:
        app_dir = Path(get_app_data_dir())
        app_dir.mkdir(parents=True, exist_ok=True)
        return app_dir / cls.FILE_NAME

    @classmethod
    def exists(cls) -> bool:
        return cls._file_path().exists()

    @classmethod
    def load(cls) -> Optional[dict]:
        """
        Returns None if no license file exists.
        """

        path = cls._file_path()

        if not path.exists():
            return None

        try:
            return CryptoUtils.load_encrypted_file(str(path))
        except Exception:
            return None

    @classmethod
    def save(cls, license_key: str, machine_id: str, activated_at: str, expire_at: str, last_run: str,) -> None:
        """
        Saves license information.
        """

        data = {
            "license_key": license_key,
            "machine_id": machine_id,
            "activated_at": activated_at,
            "expire_at": expire_at,
            "last_run": last_run,
        }

        CryptoUtils.save_encrypted_file(
            str(cls._file_path()),
            data,
        )

    @classmethod
    def update_last_run(cls, last_run: str) -> None:
        """
        Updates only the last execution time.
        """

        data = cls.load()

        if data is None:
            return

        data["last_run"] = last_run
        CryptoUtils.save_encrypted_file(
            str(cls._file_path()),
            data,
        )

    @classmethod
    def delete(cls) -> None:
        """
        Deletes license file.
        """

        path = cls._file_path()

        if path.exists():
            path.unlink()
