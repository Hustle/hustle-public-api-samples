from enum import Enum


class EvertrueExternalLeadSchemaIntegrationType(str, Enum):
    EVERTRUE = "evertrue"

    def __str__(self) -> str:
        return str(self.value)
