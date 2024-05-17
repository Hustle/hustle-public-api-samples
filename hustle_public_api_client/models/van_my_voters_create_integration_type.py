from enum import Enum


class VanMyVotersCreateIntegrationType(str, Enum):
    VAN_MYVOTERS = "van_myvoters"

    def __str__(self) -> str:
        return str(self.value)
