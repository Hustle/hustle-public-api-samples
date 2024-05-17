from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.pdi_create_integration_type import PDICreateIntegrationType

if TYPE_CHECKING:
    from ..models.pdi_create_integration_credentials import PDICreateIntegrationCredentials


T = TypeVar("T", bound="PDICreateIntegration")


@_attrs_define
class PDICreateIntegration:
    """
    Attributes:
        type (PDICreateIntegrationType):
        name (str): Name of the integration to be created
        credentials (PDICreateIntegrationCredentials):
    """

    type: PDICreateIntegrationType
    name: str
    credentials: "PDICreateIntegrationCredentials"

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        name = self.name

        credentials = self.credentials.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "name": name,
                "credentials": credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pdi_create_integration_credentials import PDICreateIntegrationCredentials

        d = src_dict.copy()
        type = PDICreateIntegrationType(d.pop("type"))

        name = d.pop("name")

        credentials = PDICreateIntegrationCredentials.from_dict(d.pop("credentials"))

        pdi_create_integration = cls(
            type=type,
            name=name,
            credentials=credentials,
        )

        return pdi_create_integration
