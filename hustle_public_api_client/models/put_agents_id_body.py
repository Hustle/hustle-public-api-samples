from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutAgentsIdBody")


@_attrs_define
class PutAgentsIdBody:
    """
    Attributes:
        name (str): The display name of the agent.
        full_name (str): The full name of the agent.
        send_invite (Union[Unset, bool]): Whether this update should send a new email invite to the agent.
    """

    name: str
    full_name: str
    send_invite: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        full_name = self.full_name

        send_invite = self.send_invite

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "fullName": full_name,
            }
        )
        if send_invite is not UNSET:
            field_dict["sendInvite"] = send_invite

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        full_name = d.pop("fullName")

        send_invite = d.pop("sendInvite", UNSET)

        put_agents_id_body = cls(
            name=name,
            full_name=full_name,
            send_invite=send_invite,
        )

        return put_agents_id_body
