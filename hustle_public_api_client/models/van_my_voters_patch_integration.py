from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.van_my_voters_patch_integration_type import VanMyVotersPatchIntegrationType

if TYPE_CHECKING:
    from ..models.van_my_voters_patch_integration_credentials import VanMyVotersPatchIntegrationCredentials


T = TypeVar("T", bound="VanMyVotersPatchIntegration")


@_attrs_define
class VanMyVotersPatchIntegration:
    """
    Attributes:
        type (VanMyVotersPatchIntegrationType): This operation will update the credentials associated with an
            integration provided the credentials are valid.
        credentials (VanMyVotersPatchIntegrationCredentials):
    """

    type: VanMyVotersPatchIntegrationType
    credentials: "VanMyVotersPatchIntegrationCredentials"

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        credentials = self.credentials.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "credentials": credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.van_my_voters_patch_integration_credentials import VanMyVotersPatchIntegrationCredentials

        d = src_dict.copy()
        type = VanMyVotersPatchIntegrationType(d.pop("type"))

        credentials = VanMyVotersPatchIntegrationCredentials.from_dict(d.pop("credentials"))

        van_my_voters_patch_integration = cls(
            type=type,
            credentials=credentials,
        )

        return van_my_voters_patch_integration
