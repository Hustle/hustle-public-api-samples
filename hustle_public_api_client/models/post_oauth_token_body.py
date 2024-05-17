from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.post_oauth_token_body_grant_type import PostOauthTokenBodyGrantType

T = TypeVar("T", bound="PostOauthTokenBody")


@_attrs_define
class PostOauthTokenBody:
    """
    Attributes:
        grant_type (PostOauthTokenBodyGrantType):
        client_id (str):
        client_secret (str):
    """

    grant_type: PostOauthTokenBodyGrantType
    client_id: str
    client_secret: str

    def to_dict(self) -> Dict[str, Any]:
        grant_type = self.grant_type.value

        client_id = self.client_id

        client_secret = self.client_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "grant_type": grant_type,
                "client_id": client_id,
                "client_secret": client_secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        grant_type = PostOauthTokenBodyGrantType(d.pop("grant_type"))

        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        post_oauth_token_body = cls(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
        )

        return post_oauth_token_body
