from enum import Enum


class VanPatchIntegrationType(str, Enum):
    UPDATEVANCREDENTIALS = "updateVANCredentials"

    def __str__(self) -> str:
        return str(self.value)
