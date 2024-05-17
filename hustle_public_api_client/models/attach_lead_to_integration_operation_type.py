from enum import Enum


class AttachLeadToIntegrationOperationType(str, Enum):
    ATTACHLEADTOINTEGRATION = "attachLeadToIntegration"

    def __str__(self) -> str:
        return str(self.value)
