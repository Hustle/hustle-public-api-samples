from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.bb_luminate_external_lead_schema_integration_type import BbLuminateExternalLeadSchemaIntegrationType

if TYPE_CHECKING:
    from ..models.bb_luminate_external_lead_schema_external_object import BbLuminateExternalLeadSchemaExternalObject


T = TypeVar("T", bound="BbLuminateExternalLeadSchema")


@_attrs_define
class BbLuminateExternalLeadSchema:
    """
    Attributes:
        integration_type (BbLuminateExternalLeadSchemaIntegrationType):
        external_object (BbLuminateExternalLeadSchemaExternalObject):
    """

    integration_type: BbLuminateExternalLeadSchemaIntegrationType
    external_object: "BbLuminateExternalLeadSchemaExternalObject"

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
        from ..models.bb_luminate_external_lead_schema_external_object import BbLuminateExternalLeadSchemaExternalObject

        d = src_dict.copy()
        integration_type = BbLuminateExternalLeadSchemaIntegrationType(d.pop("integrationType"))

        external_object = BbLuminateExternalLeadSchemaExternalObject.from_dict(d.pop("externalObject"))

        bb_luminate_external_lead_schema = cls(
            integration_type=integration_type,
            external_object=external_object,
        )

        return bb_luminate_external_lead_schema
