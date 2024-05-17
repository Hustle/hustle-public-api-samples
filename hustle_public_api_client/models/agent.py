from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.agent_type import AgentType

T = TypeVar("T", bound="Agent")


@_attrs_define
class Agent:
    """An agent represents someone that contacts leads on behalf of an organization.

    Attributes:
        id (str): The ID of the agent.
        type (AgentType): The type of object the attached ID corresponds to.
        name (str): The display name of the agent.
        full_name (str): The full name of the agent.
        phone_number (str): The phone number of the agent.
        organization_id (str): The ID of the organization the agent belongs to.
        group_id (str): The ID of the group the agent belongs to.
        created_at (str): An ISO-8601 string representing the date the agent was created.
    """

    id: str
    type: AgentType
    name: str
    full_name: str
    phone_number: str
    organization_id: str
    group_id: str
    created_at: str

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        name = self.name

        full_name = self.full_name

        phone_number = self.phone_number

        organization_id = self.organization_id

        group_id = self.group_id

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "type": type,
                "name": name,
                "fullName": full_name,
                "phoneNumber": phone_number,
                "organizationId": organization_id,
                "groupId": group_id,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = AgentType(d.pop("type"))

        name = d.pop("name")

        full_name = d.pop("fullName")

        phone_number = d.pop("phoneNumber")

        organization_id = d.pop("organizationId")

        group_id = d.pop("groupId")

        created_at = d.pop("createdAt")

        agent = cls(
            id=id,
            type=type,
            name=name,
            full_name=full_name,
            phone_number=phone_number,
            organization_id=organization_id,
            group_id=group_id,
            created_at=created_at,
        )

        return agent
