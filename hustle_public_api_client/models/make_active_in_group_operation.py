from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.make_active_in_group_operation_type import MakeActiveInGroupOperationType

T = TypeVar("T", bound="MakeActiveInGroupOperation")


@_attrs_define
class MakeActiveInGroupOperation:
    """
    Attributes:
        type (MakeActiveInGroupOperationType): This operation will make the lead active in the group and add the lead to
            a specified group if they are not already a part of it. This is a permanent addition since these leads have
            message history and other auditing requirements that make them impossible to permanently delete. The only way to
            stop texting a lead in a group is to make them inactive using the MakeInactiveInGroup operation.
        group_id (str): The ID of the group to reactivate the lead in or add the lead to.
    """

    type: MakeActiveInGroupOperationType
    group_id: str

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        group_id = self.group_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "groupId": group_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = MakeActiveInGroupOperationType(d.pop("type"))

        group_id = d.pop("groupId")

        make_active_in_group_operation = cls(
            type=type,
            group_id=group_id,
        )

        return make_active_in_group_operation
