from enum import Enum


class IntegrationType(str, Enum):
    INTEGRATION = "integration"

    def __str__(self) -> str:
        return str(self.value)
