from enum import Enum


class VanMyVotersPatchIntegrationType(str, Enum):
    UPDATEVANMYVOTERSCREDENTIALS = "updateVANMyVotersCredentials"

    def __str__(self) -> str:
        return str(self.value)
