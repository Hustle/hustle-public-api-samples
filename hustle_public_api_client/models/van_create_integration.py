from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.van_create_integration_type import VanCreateIntegrationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.van_create_integration_credentials import VanCreateIntegrationCredentials


T = TypeVar("T", bound="VanCreateIntegration")


@_attrs_define
class VanCreateIntegration:
    """
    Attributes:
        type (VanCreateIntegrationType):
        name (str): Name of the integration to be created
        credentials (VanCreateIntegrationCredentials):
        ref_key (Union[Unset, str]): Key used for processing of saved list.
    """

    type: VanCreateIntegrationType
    name: str
    credentials: "VanCreateIntegrationCredentials"
    ref_key: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        name = self.name

        credentials = self.credentials.to_dict()

        ref_key = self.ref_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "name": name,
                "credentials": credentials,
            }
        )
        if ref_key is not UNSET:
            field_dict["refKey"] = ref_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.van_create_integration_credentials import VanCreateIntegrationCredentials

        d = src_dict.copy()
        type = VanCreateIntegrationType(d.pop("type"))

        name = d.pop("name")

        credentials = VanCreateIntegrationCredentials.from_dict(d.pop("credentials"))

        ref_key = d.pop("refKey", UNSET)

        van_create_integration = cls(
            type=type,
            name=name,
            credentials=credentials,
            ref_key=ref_key,
        )

        return van_create_integration
