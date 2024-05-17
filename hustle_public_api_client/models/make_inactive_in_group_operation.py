from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.make_inactive_in_group_operation_type import MakeInactiveInGroupOperationType

T = TypeVar("T", bound="MakeInactiveInGroupOperation")


@_attrs_define
class MakeInactiveInGroupOperation:
    """
    Attributes:
        type (MakeInactiveInGroupOperationType): This operation will make the lead inactive in the specified group.
            Because deleting a lead from a group is not allowed since the lead has message history, the only way to stop a
            lead from receiving messages meant for a group is to make them inactive.
        group_id (str): The ID of the group to make the lead inactive in.
    """

    type: MakeInactiveInGroupOperationType
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
        type = MakeInactiveInGroupOperationType(d.pop("type"))

        group_id = d.pop("groupId")

        make_inactive_in_group_operation = cls(
            type=type,
            group_id=group_id,
        )

        return make_inactive_in_group_operation
