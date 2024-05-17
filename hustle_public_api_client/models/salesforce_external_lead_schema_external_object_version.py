from enum import Enum


class SalesforceExternalLeadSchemaExternalObjectVersion(str, Enum):
    VALUE_0 = "41.0"

    def __str__(self) -> str:
        return str(self.value)
