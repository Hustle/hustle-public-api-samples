from enum import Enum


class RemoveTagOperationType(str, Enum):
    REMOVETAG = "removeTag"

    def __str__(self) -> str:
        return str(self.value)
