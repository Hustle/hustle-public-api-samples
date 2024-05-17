from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.tag_agent_visibility import TagAgentVisibility
from ..models.tag_type import TagType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Tag")


@_attrs_define
class Tag:
    """A tag represents a label that can be applied to a lead.

    Attributes:
        id (str): The tag's ID.
        type (TagType): The type of this object.
        name (str): The tag name/label that shows up in the UI.
        created_at (str): An ISO-8601 string representing the date the tag was created.
        agent_visibility (TagAgentVisibility): The context in which an agent can see and collect tags.
            LEAD_PROFILES: The default use. Agents will be able to see these while sending messages and use them to collect
            info about contacts.
            OPT_OUT: Specifically for opt-out reasons. Will only be displayed when agents opt out a contact.
            NEVER: Only for admins. Agents will never see this tag.
        organization_id (Union[Unset, str]): The organization this tag belongs to.
    """

    id: str
    type: TagType
    name: str
    created_at: str
    agent_visibility: TagAgentVisibility
    organization_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        name = self.name

        created_at = self.created_at

        agent_visibility = self.agent_visibility.value

        organization_id = self.organization_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "type": type,
                "name": name,
                "createdAt": created_at,
                "agentVisibility": agent_visibility,
            }
        )
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = TagType(d.pop("type"))

        name = d.pop("name")

        created_at = d.pop("createdAt")

        agent_visibility = TagAgentVisibility(d.pop("agentVisibility"))

        organization_id = d.pop("organizationId", UNSET)

        tag = cls(
            id=id,
            type=type,
            name=name,
            created_at=created_at,
            agent_visibility=agent_visibility,
            organization_id=organization_id,
        )

        return tag
