from enum import Enum


class OptOutOperationType(str, Enum):
    OPTOUT = "optOut"

    def __str__(self) -> str:
        return str(self.value)
