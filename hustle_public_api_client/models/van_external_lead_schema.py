from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.van_external_lead_schema_integration_type import VanExternalLeadSchemaIntegrationType

if TYPE_CHECKING:
    from ..models.van_external_lead_schema_external_object import VanExternalLeadSchemaExternalObject


T = TypeVar("T", bound="VanExternalLeadSchema")


@_attrs_define
class VanExternalLeadSchema:
    """
    Attributes:
        integration_type (VanExternalLeadSchemaIntegrationType):
        external_object (VanExternalLeadSchemaExternalObject):
    """

    integration_type: VanExternalLeadSchemaIntegrationType
    external_object: "VanExternalLeadSchemaExternalObject"

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
        from ..models.van_external_lead_schema_external_object import VanExternalLeadSchemaExternalObject

        d = src_dict.copy()
        integration_type = VanExternalLeadSchemaIntegrationType(d.pop("integrationType"))

        external_object = VanExternalLeadSchemaExternalObject.from_dict(d.pop("externalObject"))

        van_external_lead_schema = cls(
            integration_type=integration_type,
            external_object=external_object,
        )

        return van_external_lead_schema
