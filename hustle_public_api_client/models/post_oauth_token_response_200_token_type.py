from enum import Enum


class PostOauthTokenResponse200TokenType(str, Enum):
    BEARER = "Bearer"

    def __str__(self) -> str:
        return str(self.value)
