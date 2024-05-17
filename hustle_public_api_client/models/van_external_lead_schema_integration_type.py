from enum import Enum


class VanExternalLeadSchemaIntegrationType(str, Enum):
    VAN = "van"

    def __str__(self) -> str:
        return str(self.value)
