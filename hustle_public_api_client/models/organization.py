from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define

from ..models.organization_type import OrganizationType

T = TypeVar("T", bound="Organization")


@_attrs_define
class Organization:
    """An organization owns multiple groups and is the entity leads are scoped to in Hustle.

    Attributes:
        id (str): The ID of the organization.
        type (OrganizationType): The type of object the attached ID corresponds to.
        name (str): The name of the organization.
        integrations (List[str]): The IDs of the integrations the organization owns.
        created_at (str): An ISO-8601 string representing the date the organization was created.
    """

    id: str
    type: OrganizationType
    name: str
    integrations: List[str]
    created_at: str

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        name = self.name

        integrations = self.integrations

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "type": type,
                "name": name,
                "integrations": integrations,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = OrganizationType(d.pop("type"))

        name = d.pop("name")

        integrations = cast(List[str], d.pop("integrations"))

        created_at = d.pop("createdAt")

        organization = cls(
            id=id,
            type=type,
            name=name,
            integrations=integrations,
            created_at=created_at,
        )

        return organization
