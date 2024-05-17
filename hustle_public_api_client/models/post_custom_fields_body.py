from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostCustomFieldsBody")


@_attrs_define
class PostCustomFieldsBody:
    """Creates a new custom field.

    Attributes:
        name (str): The name of the custom field.
        agent_visible (bool): Whether the custom field is visible to agents.
        organization_id (str): The organization this custom field is scoped to.
    """

    name: str
    agent_visible: bool
    organization_id: str

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        agent_visible = self.agent_visible

        organization_id = self.organization_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "agentVisible": agent_visible,
                "organizationId": organization_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        agent_visible = d.pop("agentVisible")

        organization_id = d.pop("organizationId")

        post_custom_fields_body = cls(
            name=name,
            agent_visible=agent_visible,
            organization_id=organization_id,
        )

        return post_custom_fields_body
