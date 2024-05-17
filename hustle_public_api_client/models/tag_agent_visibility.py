from enum import Enum


class TagAgentVisibility(str, Enum):
    LEAD_PROFILES = "LEAD_PROFILES"
    NEVER = "NEVER"
    OPT_OUT = "OPT_OUT"

    def __str__(self) -> str:
        return str(self.value)
