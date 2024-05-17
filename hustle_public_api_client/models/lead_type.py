from enum import Enum


class LeadType(str, Enum):
    LEAD = "lead"

    def __str__(self) -> str:
        return str(self.value)
