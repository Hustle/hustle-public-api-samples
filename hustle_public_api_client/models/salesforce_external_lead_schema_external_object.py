from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.salesforce_external_lead_schema_external_object_version import (
    SalesforceExternalLeadSchemaExternalObjectVersion,
)

T = TypeVar("T", bound="SalesforceExternalLeadSchemaExternalObject")


@_attrs_define
class SalesforceExternalLeadSchemaExternalObject:
    """
    Attributes:
        version (SalesforceExternalLeadSchemaExternalObjectVersion):
        salesforce_object_type (str):
        salesforce_object_id (str):
    """

    version: SalesforceExternalLeadSchemaExternalObjectVersion
    salesforce_object_type: str
    salesforce_object_id: str

    def to_dict(self) -> Dict[str, Any]:
        version = self.version.value

        salesforce_object_type = self.salesforce_object_type

        salesforce_object_id = self.salesforce_object_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "version": version,
                "salesforceObjectType": salesforce_object_type,
                "salesforceObjectId": salesforce_object_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = SalesforceExternalLeadSchemaExternalObjectVersion(d.pop("version"))

        salesforce_object_type = d.pop("salesforceObjectType")

        salesforce_object_id = d.pop("salesforceObjectId")

        salesforce_external_lead_schema_external_object = cls(
            version=version,
            salesforce_object_type=salesforce_object_type,
            salesforce_object_id=salesforce_object_id,
        )

        return salesforce_external_lead_schema_external_object
