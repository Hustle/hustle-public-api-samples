from enum import Enum


class SetCustomFieldOperationType(str, Enum):
    SETCUSTOMFIELD = "setCustomField"

    def __str__(self) -> str:
        return str(self.value)
