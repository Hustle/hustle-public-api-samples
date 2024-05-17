from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostAgentsBody")


@_attrs_define
class PostAgentsBody:
    """
    Attributes:
        name (str): The display name of the agent.
        full_name (str): The full name of the agent.
        email (str): The email of the agent - This will be used by the agent to log in.
        group_id (str): The ID of the group the agent will belong to.
    """

    name: str
    full_name: str
    email: str
    group_id: str

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        full_name = self.full_name

        email = self.email

        group_id = self.group_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "fullName": full_name,
                "email": email,
                "groupId": group_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        full_name = d.pop("fullName")

        email = d.pop("email")

        group_id = d.pop("groupId")

        post_agents_body = cls(
            name=name,
            full_name=full_name,
            email=email,
            group_id=group_id,
        )

        return post_agents_body
