from enum import Enum


class PDIPatchIntegrationType(str, Enum):
    UPDATEPDICREDENTIALS = "updatePDICredentials"

    def __str__(self) -> str:
        return str(self.value)
