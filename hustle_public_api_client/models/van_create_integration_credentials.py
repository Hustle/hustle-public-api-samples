from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="VanCreateIntegrationCredentials")


@_attrs_define
class VanCreateIntegrationCredentials:
    """
    Attributes:
        application_name (str): application name used to authenticate.
        api_key (str): apiKey used to authenticate.
    """

    application_name: str
    api_key: str

    def to_dict(self) -> Dict[str, Any]:
        application_name = self.application_name

        api_key = self.api_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "applicationName": application_name,
                "apiKey": api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        application_name = d.pop("applicationName")

        api_key = d.pop("apiKey")

        van_create_integration_credentials = cls(
            application_name=application_name,
            api_key=api_key,
        )

        return van_create_integration_credentials
