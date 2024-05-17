from enum import Enum


class VanMyVotersExternalLeadSchemaIntegrationType(str, Enum):
    VAN_MYVOTERS = "van-myvoters"

    def __str__(self) -> str:
        return str(self.value)
