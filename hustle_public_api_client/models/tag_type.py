from enum import Enum


class TagType(str, Enum):
    TAG = "tag"

    def __str__(self) -> str:
        return str(self.value)
