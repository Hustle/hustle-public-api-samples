from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.remove_tag_operation_type import RemoveTagOperationType

T = TypeVar("T", bound="RemoveTagOperation")


@_attrs_define
class RemoveTagOperation:
    """
    Attributes:
        type (RemoveTagOperationType): This operation will remove a tag form a lead.
        tag_id (str): The ID of the tag to remove from the lead.
    """

    type: RemoveTagOperationType
    tag_id: str

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        tag_id = self.tag_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "tagId": tag_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = RemoveTagOperationType(d.pop("type"))

        tag_id = d.pop("tagId")

        remove_tag_operation = cls(
            type=type,
            tag_id=tag_id,
        )

        return remove_tag_operation
