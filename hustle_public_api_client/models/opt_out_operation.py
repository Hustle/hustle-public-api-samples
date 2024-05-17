from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.opt_out_operation_type import OptOutOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OptOutOperation")


@_attrs_define
class OptOutOperation:
    """
    Attributes:
        type (OptOutOperationType): This operation will opt a lead out of receiving messages from Hustle. If account
            sync is enabled, all other leads in the account with the same number will also be opted out. Be careful with
            this as the only way to currently opt leads back in is to contact Hustle support.
        tag_id (Union[Unset, str]): The ID of the tag to apply to the lead when opting them out. This must be an OptOut
            tag.
    """

    type: OptOutOperationType
    tag_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        tag_id = self.tag_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if tag_id is not UNSET:
            field_dict["tagId"] = tag_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = OptOutOperationType(d.pop("type"))

        tag_id = d.pop("tagId", UNSET)

        opt_out_operation = cls(
            type=type,
            tag_id=tag_id,
        )

        return opt_out_operation
