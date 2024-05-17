from enum import Enum


class PDICreateIntegrationType(str, Enum):
    PDI = "pdi"

    def __str__(self) -> str:
        return str(self.value)
