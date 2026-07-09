from datetime import datetime, timedelta
import hashlib

from services.machine_info import MachineInfo
from services.license_storage import LicenseStorage

try:
    from config.dev_config import DEVELOPMENT_MODE
except ImportError:
    DEVELOPMENT_MODE = False

try:
    from generated.generated_license import VALID_LICENSE_HASH
except ImportError:
    VALID_LICENSE_HASH = None


class LicenseManager:
    """
    Manages application license activation and validation.
    """

    LICENSE_DURATION_DAYS = 7
    LICENSE_DURATION_MINUTES = 3

    def __init__(self):
        self.machine_id = MachineInfo.get_machine_id()

    def activate(self, license_key: str) -> bool:
        """
        Activates application with user entered key.
        """

        data = LicenseStorage.load()
        if data is not None and self.is_expired(data):
            return False
        if not self._verify_key(license_key):
            return False

        now = datetime.now()
        data = {
            "license_hash": self._hash_key(license_key),
            "machine_id": self.machine_id,
            "activated_at": now.isoformat(),
            "last_run": now.isoformat()
        }
        LicenseStorage.save(
            license_key=data["license_hash"],
            machine_id=data["machine_id"],
            activated_at=data["activated_at"],
            expire_at=(
                now +
                timedelta(days=self.LICENSE_DURATION_DAYS)
            ).isoformat(),
            last_run=data["last_run"]
        )

        return True

    def can_run(self) -> bool:
        """
        Checks if application is allowed to run.
        """
        if DEVELOPMENT_MODE:
            return True

        if not LicenseStorage.exists():
            return False

        data = LicenseStorage.load()

        if data is None:
            return False

        if not self._check_machine(data):
            return False

        if not self._check_clock(data):
            return False

        if self.is_expired(data):
            return False

        self.update_last_run()

        return True

    def is_expired(self, data=None) -> bool:
        """
        Checks license expiration.
        """

        if data is None:
            data = LicenseStorage.load()

        if data is None:
            return True

        expire_date = datetime.fromisoformat(data["expire_at"])

        return datetime.now() > expire_date

    def _verify_key(self, key: str) -> bool:
        """
        Checks entered key.
        """
        if DEVELOPMENT_MODE:
            return True

        if VALID_LICENSE_HASH is None:
            return False

        return self._hash_key(key) == VALID_LICENSE_HASH

    @staticmethod
    def _hash_key(key: str) -> str:
        """
        Creates SHA256 hash.
        """

        return hashlib.sha256(key.encode("utf-8")).hexdigest()

    def _check_machine(self, data: dict) -> bool:
        """
        Prevents copying license file to another PC.
        """

        return (data.get("machine_id") == self.machine_id)

    def _check_clock(self, data: dict) -> bool:
        """
        Detects changing system clock backwards.
        """

        last_run = datetime.fromisoformat(data["last_run"])

        return datetime.now() >= last_run

    def update_last_run(self):
        """
        Updates last execution time.
        """

        LicenseStorage.update_last_run(
            datetime.now().isoformat()
        )

    def remaining_days(self) -> int:
        """
        Returns remaining license days.
        """

        data = LicenseStorage.load()

        if data is None:
            return 0

        activated = datetime.fromisoformat(data["activated_at"])
        expire = datetime.fromisoformat(data["expire_at"])
        remaining = (expire - datetime.now()).days

        return max(0, remaining)
