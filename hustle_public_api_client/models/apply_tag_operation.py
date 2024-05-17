from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.apply_tag_operation_type import ApplyTagOperationType

T = TypeVar("T", bound="ApplyTagOperation")


@_attrs_define
class ApplyTagOperation:
    """
    Attributes:
        type (ApplyTagOperationType): This operation will attach a tag in an organization to a lead in that same
            organization.
        tag_id (str): The ID of the tag to apply to the lead.
    """

    type: ApplyTagOperationType
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
        type = ApplyTagOperationType(d.pop("type"))

        tag_id = d.pop("tagId")

        apply_tag_operation = cls(
            type=type,
            tag_id=tag_id,
        )

        return apply_tag_operation
