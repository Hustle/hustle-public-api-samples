from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PDICreateIntegrationCredentials")


@_attrs_define
class PDICreateIntegrationCredentials:
    """
    Attributes:
        username (str): Username or email used to authenticate to the integration.
        password (str): Password used to authenticate to the integration.
        api_key (str): apiKey used to authenticate to PDI.
    """

    username: str
    password: str
    api_key: str

    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        password = self.password

        api_key = self.api_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "username": username,
                "password": password,
                "apiKey": api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        password = d.pop("password")

        api_key = d.pop("apiKey")

        pdi_create_integration_credentials = cls(
            username=username,
            password=password,
            api_key=api_key,
        )

        return pdi_create_integration_credentials
