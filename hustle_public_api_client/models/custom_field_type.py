from enum import Enum


class CustomFieldType(str, Enum):
    CUSTOM_FIELD = "custom_field"

    def __str__(self) -> str:
        return str(self.value)
