from enum import Enum


class ApplyTagOperationType(str, Enum):
    APPLYTAG = "applyTag"

    def __str__(self) -> str:
        return str(self.value)
