from enum import Enum


class BbLuminateExternalLeadSchemaIntegrationType(str, Enum):
    BBLUMINATE = "bbluminate"

    def __str__(self) -> str:
        return str(self.value)
