from enum import Enum


class VanCreateIntegrationType(str, Enum):
    VAN = "van"

    def __str__(self) -> str:
        return str(self.value)
