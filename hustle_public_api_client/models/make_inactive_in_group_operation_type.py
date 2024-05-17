from enum import Enum


class MakeInactiveInGroupOperationType(str, Enum):
    MAKEINACTIVEINGROUP = "makeInactiveInGroup"

    def __str__(self) -> str:
        return str(self.value)
