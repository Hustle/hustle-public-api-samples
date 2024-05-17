from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.van_my_voters_external_lead_schema_integration_type import VanMyVotersExternalLeadSchemaIntegrationType

if TYPE_CHECKING:
    from ..models.van_my_voters_external_lead_schema_external_object import VanMyVotersExternalLeadSchemaExternalObject


T = TypeVar("T", bound="VanMyVotersExternalLeadSchema")


@_attrs_define
class VanMyVotersExternalLeadSchema:
    """
    Attributes:
        integration_type (VanMyVotersExternalLeadSchemaIntegrationType):
        external_object (VanMyVotersExternalLeadSchemaExternalObject):
    """

    integration_type: VanMyVotersExternalLeadSchemaIntegrationType
    external_object: "VanMyVotersExternalLeadSchemaExternalObject"

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
        from ..models.van_my_voters_external_lead_schema_external_object import (
            VanMyVotersExternalLeadSchemaExternalObject,
        )

        d = src_dict.copy()
        integration_type = VanMyVotersExternalLeadSchemaIntegrationType(d.pop("integrationType"))

        external_object = VanMyVotersExternalLeadSchemaExternalObject.from_dict(d.pop("externalObject"))

        van_my_voters_external_lead_schema = cls(
            integration_type=integration_type,
            external_object=external_object,
        )

        return van_my_voters_external_lead_schema
