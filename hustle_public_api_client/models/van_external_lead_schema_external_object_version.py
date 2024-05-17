from enum import Enum


class VanExternalLeadSchemaExternalObjectVersion(str, Enum):
    V4 = "v4"

    def __str__(self) -> str:
        return str(self.value)
