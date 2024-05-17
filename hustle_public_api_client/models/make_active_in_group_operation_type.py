from enum import Enum


class MakeActiveInGroupOperationType(str, Enum):
    MAKEACTIVEINGROUP = "makeActiveInGroup"

    def __str__(self) -> str:
        return str(self.value)
