from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.van_patch_integration_type import VanPatchIntegrationType

if TYPE_CHECKING:
    from ..models.van_patch_integration_credentials import VanPatchIntegrationCredentials


T = TypeVar("T", bound="VanPatchIntegration")


@_attrs_define
class VanPatchIntegration:
    """
    Attributes:
        type (VanPatchIntegrationType): This operation will update the credentials associated with an integration
            provided the credentials are valid.
        credentials (VanPatchIntegrationCredentials):
    """

    type: VanPatchIntegrationType
    credentials: "VanPatchIntegrationCredentials"

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
        from ..models.van_patch_integration_credentials import VanPatchIntegrationCredentials

        d = src_dict.copy()
        type = VanPatchIntegrationType(d.pop("type"))

        credentials = VanPatchIntegrationCredentials.from_dict(d.pop("credentials"))

        van_patch_integration = cls(
            type=type,
            credentials=credentials,
        )

        return van_patch_integration
