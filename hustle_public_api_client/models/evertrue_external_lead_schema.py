from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.evertrue_external_lead_schema_integration_type import EvertrueExternalLeadSchemaIntegrationType

if TYPE_CHECKING:
    from ..models.evertrue_external_lead_schema_external_object import EvertrueExternalLeadSchemaExternalObject


T = TypeVar("T", bound="EvertrueExternalLeadSchema")


@_attrs_define
class EvertrueExternalLeadSchema:
    """
    Attributes:
        integration_type (EvertrueExternalLeadSchemaIntegrationType):
        external_object (EvertrueExternalLeadSchemaExternalObject):
    """

    integration_type: EvertrueExternalLeadSchemaIntegrationType
    external_object: "EvertrueExternalLeadSchemaExternalObject"

    def to_dict(self) -> Dict[str, Any]:
        integration_type = self.integration_type.value

        external_object = self.external_object.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "integrationType": integration_type,
                "externalObject": external_object,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.evertrue_external_lead_schema_external_object import EvertrueExternalLeadSchemaExternalObject

        d = src_dict.copy()
        integration_type = EvertrueExternalLeadSchemaIntegrationType(d.pop("integrationType"))

        external_object = EvertrueExternalLeadSchemaExternalObject.from_dict(d.pop("externalObject"))

        evertrue_external_lead_schema = cls(
            integration_type=integration_type,
            external_object=external_object,
        )

        return evertrue_external_lead_schema
