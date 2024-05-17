from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.custom_field_type import CustomFieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomField")


@_attrs_define
class CustomField:
    """A custom field is a custom property that can be attached to a lead.

    Attributes:
        id (str): The ID of the custom field.
        type (CustomFieldType): The type of object the attached ID corresponds to.
        name (str): The name of the custom field.
        agent_visible (bool): Whether the custom field is visible to agents.
        created_at (str): An ISO-8601 string representing the date the custom field was created.
        organization_id (Union[Unset, str]): The organization this custom field is scoped to (if any).
    """

    id: str
    type: CustomFieldType
    name: str
    agent_visible: bool
    created_at: str
    organization_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        name = self.name

        agent_visible = self.agent_visible

        created_at = self.created_at

        organization_id = self.organization_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "type": type,
                "name": name,
                "agentVisible": agent_visible,
                "createdAt": created_at,
            }
        )
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = CustomFieldType(d.pop("type"))

        name = d.pop("name")

        agent_visible = d.pop("agentVisible")

        created_at = d.pop("createdAt")

        organization_id = d.pop("organizationId", UNSET)

        custom_field = cls(
            id=id,
            type=type,
            name=name,
            agent_visible=agent_visible,
            created_at=created_at,
            organization_id=organization_id,
        )

        return custom_field
