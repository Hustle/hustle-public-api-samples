from enum import Enum


class IntegrationIntegrationType(str, Enum):
    BBLUMINATE = "bbluminate"
    EVERTRUE = "evertrue"
    MSDYNAMICS = "msdynamics"
    PDI = "pdi"
    SALESFORCE_MANAGED_PACKAGE = "salesforce_managed_package"
    VAN = "van"
    VAN_MYVOTERS = "van_myvoters"

    def __str__(self) -> str:
        return str(self.value)
