from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.pdi_patch_integration_type import PDIPatchIntegrationType

if TYPE_CHECKING:
    from ..models.pdi_patch_integration_credentials import PDIPatchIntegrationCredentials


T = TypeVar("T", bound="PDIPatchIntegration")


@_attrs_define
class PDIPatchIntegration:
    """
    Attributes:
        type (PDIPatchIntegrationType): This operation will update the credentials associated with an integration
            provided the credentials are valid.
        credentials (PDIPatchIntegrationCredentials):
    """

    type: PDIPatchIntegrationType
    credentials: "PDIPatchIntegrationCredentials"

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
        from ..models.pdi_patch_integration_credentials import PDIPatchIntegrationCredentials

        d = src_dict.copy()
        type = PDIPatchIntegrationType(d.pop("type"))

        credentials = PDIPatchIntegrationCredentials.from_dict(d.pop("credentials"))

        pdi_patch_integration = cls(
            type=type,
            credentials=credentials,
        )

        return pdi_patch_integration
