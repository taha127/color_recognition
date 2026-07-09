import hashlib
import platform
import socket
import uuid
import machineid


class MachineInfo:
    """
    Generates a unique and relatively stable machine identifier.
    """

    @staticmethod
    def get_machine_id() -> str:
        """
        Returns a SHA256 hash representing this machine.
        """

        parts = [
            machineid.id(),                  # OS Machine ID (stable)
            platform.system(),
            platform.release(),
            platform.machine(),
            platform.processor(),
            socket.gethostname(),
            hex(uuid.getnode()),             # MAC Address
        ]
        raw = "|".join(parts)

        return hashlib.sha256(raw.encode("utf-8")).hexdigest().upper()

    @staticmethod
    def get_short_machine_id(length: int = 16) -> str:
        """
        Returns a shortened Machine ID for display.
        """

        return MachineInfo.get_machine_id()[:length]

    @staticmethod
    def get_display_machine_id() -> str:
        """
        Returns formatted Machine ID.
        Example:
        A1B2-C3D4-E5F6-G7H8
        """

        short = MachineInfo.get_machine_id()[:16]

        return "-".join(
            short[i:i + 4]
            for i in range(0, len(short), 4)
        )
