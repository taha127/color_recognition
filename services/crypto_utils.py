import base64
import hashlib
import json
from cryptography.fernet import Fernet, InvalidToken
from services.machine_info import MachineInfo


class CryptoUtils:
    """
    Utility class for encrypting and decrypting application data.
    """

    @staticmethod
    def _generate_key() -> bytes:
        """
        Generates a Fernet key derived from the current machine ID.
        """

        machine_id = MachineInfo.get_machine_id()
        digest = hashlib.sha256(machine_id.encode("utf-8")).digest()

        return base64.urlsafe_b64encode(digest)

    @staticmethod
    def encrypt_text(text: str) -> bytes:
        """
        Encrypts a UTF-8 string.
        """

        fernet = Fernet(CryptoUtils._generate_key())

        return fernet.encrypt(text.encode("utf-8"))

    @staticmethod
    def decrypt_text(data: bytes) -> str:
        """
        Decrypts encrypted bytes.
        Raises ValueError if the data is invalid.
        """

        fernet = Fernet(CryptoUtils._generate_key())

        try:
            return fernet.decrypt(data).decode("utf-8")
        except InvalidToken:
            raise ValueError("Invalid encrypted data.")

    @staticmethod
    def encrypt_dict(data: dict) -> bytes:
        """
        Encrypts a dictionary.
        """

        json_text = json.dumps(
            data,
            ensure_ascii=False,
            indent=None
        )

        return CryptoUtils.encrypt_text(json_text)

    @staticmethod
    def decrypt_dict(data: bytes) -> dict:
        """
        Decrypts encrypted dictionary data.
        """

        json_text = CryptoUtils.decrypt_text(data)

        return json.loads(json_text)

    @staticmethod
    def save_encrypted_file(path: str, data: dict) -> None:
        """
        Saves encrypted dictionary to a file.
        """

        encrypted = CryptoUtils.encrypt_dict(data)

        with open(path, "wb") as f:
            f.write(encrypted)

    @staticmethod
    def load_encrypted_file(path: str) -> dict:
        """
        Loads encrypted dictionary from a file.
        """

        with open(path, "rb") as f:
            encrypted = f.read()

        return CryptoUtils.decrypt_dict(encrypted)
