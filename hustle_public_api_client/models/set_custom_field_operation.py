from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.set_custom_field_operation_type import SetCustomFieldOperationType

T = TypeVar("T", bound="SetCustomFieldOperation")


@_attrs_define
class SetCustomFieldOperation:
    """
    Attributes:
        type (SetCustomFieldOperationType): This operation will set the value of a custom field on a lead.
        custom_field_name (str): The label of the custom field to set. This must exist as a custom field in the
            organization.
        value (str): The value to set the custom field to.
    """

    type: SetCustomFieldOperationType
    custom_field_name: str
    value: str

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        custom_field_name = self.custom_field_name

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "customFieldName": custom_field_name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = SetCustomFieldOperationType(d.pop("type"))

        custom_field_name = d.pop("customFieldName")

        value = d.pop("value")

        set_custom_field_operation = cls(
            type=type,
            custom_field_name=custom_field_name,
            value=value,
        )

        return set_custom_field_operation
