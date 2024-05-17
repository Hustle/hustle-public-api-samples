from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.van_my_voters_create_integration_type import VanMyVotersCreateIntegrationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.van_my_voters_create_integration_credentials import VanMyVotersCreateIntegrationCredentials


T = TypeVar("T", bound="VanMyVotersCreateIntegration")


@_attrs_define
class VanMyVotersCreateIntegration:
    """
    Attributes:
        type (VanMyVotersCreateIntegrationType):
        name (str): Name of the integration to be created
        credentials (VanMyVotersCreateIntegrationCredentials):
        ref_key (Union[Unset, str]): Key used for processing of saved list.
    """

    type: VanMyVotersCreateIntegrationType
    name: str
    credentials: "VanMyVotersCreateIntegrationCredentials"
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
        from ..models.van_my_voters_create_integration_credentials import VanMyVotersCreateIntegrationCredentials

        d = src_dict.copy()
        type = VanMyVotersCreateIntegrationType(d.pop("type"))

        name = d.pop("name")

        credentials = VanMyVotersCreateIntegrationCredentials.from_dict(d.pop("credentials"))

        ref_key = d.pop("refKey", UNSET)

        van_my_voters_create_integration = cls(
            type=type,
            name=name,
            credentials=credentials,
            ref_key=ref_key,
        )

        return van_my_voters_create_integration
