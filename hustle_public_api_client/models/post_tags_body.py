from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.post_tags_body_agent_visibility import PostTagsBodyAgentVisibility

T = TypeVar("T", bound="PostTagsBody")


@_attrs_define
class PostTagsBody:
    """
    Attributes:
        name (str): The name of the tag
        organization_id (str): The organization this tag belongs to.
        agent_visibility (PostTagsBodyAgentVisibility): The context in which an agent can see and collect tags.
            LEAD_PROFILES: Agents will be able to see these while sending messages and use them to collect info about
            contacts.
            OPT_OUT: Specifically for opt-out reasons. Will only be displayed when agents opt out a contact.
            NEVER: Only for admins. Agents will never see this tag.
    """

    name: str
    organization_id: str
    agent_visibility: PostTagsBodyAgentVisibility

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        organization_id = self.organization_id

        agent_visibility = self.agent_visibility.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "organizationId": organization_id,
                "agentVisibility": agent_visibility,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        organization_id = d.pop("organizationId")

        agent_visibility = PostTagsBodyAgentVisibility(d.pop("agentVisibility"))

        post_tags_body = cls(
            name=name,
            organization_id=organization_id,
            agent_visibility=agent_visibility,
        )

        return post_tags_body
