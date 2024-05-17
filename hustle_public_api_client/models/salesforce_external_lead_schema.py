from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.salesforce_external_lead_schema_integration_type import SalesforceExternalLeadSchemaIntegrationType

if TYPE_CHECKING:
    from ..models.salesforce_external_lead_schema_external_object import SalesforceExternalLeadSchemaExternalObject


T = TypeVar("T", bound="SalesforceExternalLeadSchema")


@_attrs_define
class SalesforceExternalLeadSchema:
    """
    Attributes:
        integration_type (SalesforceExternalLeadSchemaIntegrationType):
        external_object (SalesforceExternalLeadSchemaExternalObject):
    """

    integration_type: SalesforceExternalLeadSchemaIntegrationType
    external_object: "SalesforceExternalLeadSchemaExternalObject"

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
        from ..models.salesforce_external_lead_schema_external_object import SalesforceExternalLeadSchemaExternalObject

        d = src_dict.copy()
        integration_type = SalesforceExternalLeadSchemaIntegrationType(d.pop("integrationType"))

        external_object = SalesforceExternalLeadSchemaExternalObject.from_dict(d.pop("externalObject"))

        salesforce_external_lead_schema = cls(
            integration_type=integration_type,
            external_object=external_object,
        )

        return salesforce_external_lead_schema
