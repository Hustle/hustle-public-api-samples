from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.post_oauth_token_response_200_token_type import PostOauthTokenResponse200TokenType

T = TypeVar("T", bound="PostOauthTokenResponse200")


@_attrs_define
class PostOauthTokenResponse200:
    """
    Attributes:
        access_token (str):
        token_type (PostOauthTokenResponse200TokenType):
        scope (str):
        expires_in (float):
    """

    access_token: str
    token_type: PostOauthTokenResponse200TokenType
    scope: str
    expires_in: float

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token

        token_type = self.token_type.value

        scope = self.scope

        expires_in = self.expires_in

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "access_token": access_token,
                "token_type": token_type,
                "scope": scope,
                "expires_in": expires_in,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("access_token")

        token_type = PostOauthTokenResponse200TokenType(d.pop("token_type"))

        scope = d.pop("scope")

        expires_in = d.pop("expires_in")

        post_oauth_token_response_200 = cls(
            access_token=access_token,
            token_type=token_type,
            scope=scope,
            expires_in=expires_in,
        )

        return post_oauth_token_response_200
