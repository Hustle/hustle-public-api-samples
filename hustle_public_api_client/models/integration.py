from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.integration_integration_type import IntegrationIntegrationType
from ..models.integration_type import IntegrationType

T = TypeVar("T", bound="Integration")


@_attrs_define
class Integration:
    """An integration represents a connection between Hustle data and an external service (such as Salesforce, VAN, or
    PDI).

        Attributes:
            id (str): The ID of the integration.
            type (IntegrationType): The type of object the attached ID corresponds to.
            name (str): The name of the integration.
            integration_type (IntegrationIntegrationType): The type of integration.
            organization_id (str): The ID of the organization the integration belongs to.
            created_at (str): An ISO-8601 string representing the date the integration was created.
    """

    id: str
    type: IntegrationType
    name: str
    integration_type: IntegrationIntegrationType
    organization_id: str
    created_at: str

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        name = self.name

        integration_type = self.integration_type.value

        organization_id = self.organization_id

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "type": type,
                "name": name,
                "integrationType": integration_type,
                "organizationId": organization_id,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = IntegrationType(d.pop("type"))

        name = d.pop("name")

        integration_type = IntegrationIntegrationType(d.pop("integrationType"))

        organization_id = d.pop("organizationId")

        created_at = d.pop("createdAt")

        integration = cls(
            id=id,
            type=type,
            name=name,
            integration_type=integration_type,
            organization_id=organization_id,
            created_at=created_at,
        )

        return integration
