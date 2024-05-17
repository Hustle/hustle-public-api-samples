from enum import Enum


class SalesforceExternalLeadSchemaIntegrationType(str, Enum):
    SALESFORCE = "salesforce"

    def __str__(self) -> str:
        return str(self.value)
