from enum import Enum


class PostGroupsBodyCountryCode(str, Enum):
    CA = "CA"
    PR = "PR"
    US = "US"

    def __str__(self) -> str:
        return str(self.value)
