from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.apply_tag_operation import ApplyTagOperation
    from ..models.attach_lead_to_integration_operation import AttachLeadToIntegrationOperation
    from ..models.make_active_in_group_operation import MakeActiveInGroupOperation
    from ..models.make_inactive_in_group_operation import MakeInactiveInGroupOperation
    from ..models.opt_out_operation import OptOutOperation
    from ..models.remove_tag_operation import RemoveTagOperation
    from ..models.set_custom_field_operation import SetCustomFieldOperation


T = TypeVar("T", bound="PatchLeadsBody")


@_attrs_define
class PatchLeadsBody:
    """
    Attributes:
        id (str): Lead ID
        operation (Union['ApplyTagOperation', 'AttachLeadToIntegrationOperation', 'MakeActiveInGroupOperation',
            'MakeInactiveInGroupOperation', 'OptOutOperation', 'RemoveTagOperation', 'SetCustomFieldOperation']):
    """

    id: str
    operation: Union[
        "ApplyTagOperation",
        "AttachLeadToIntegrationOperation",
        "MakeActiveInGroupOperation",
        "MakeInactiveInGroupOperation",
        "OptOutOperation",
        "RemoveTagOperation",
        "SetCustomFieldOperation",
    ]

    def to_dict(self) -> Dict[str, Any]:
        from ..models.apply_tag_operation import ApplyTagOperation
        from ..models.attach_lead_to_integration_operation import AttachLeadToIntegrationOperation
        from ..models.make_active_in_group_operation import MakeActiveInGroupOperation
        from ..models.make_inactive_in_group_operation import MakeInactiveInGroupOperation
        from ..models.remove_tag_operation import RemoveTagOperation
        from ..models.set_custom_field_operation import SetCustomFieldOperation

        id = self.id

        operation: Dict[str, Any]
        if isinstance(self.operation, MakeActiveInGroupOperation):
            operation = self.operation.to_dict()
        elif isinstance(self.operation, MakeInactiveInGroupOperation):
            operation = self.operation.to_dict()
        elif isinstance(self.operation, AttachLeadToIntegrationOperation):
            operation = self.operation.to_dict()
        elif isinstance(self.operation, ApplyTagOperation):
            operation = self.operation.to_dict()
        elif isinstance(self.operation, RemoveTagOperation):
            operation = self.operation.to_dict()
        elif isinstance(self.operation, SetCustomFieldOperation):
            operation = self.operation.to_dict()
        else:
            operation = self.operation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "operation": operation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.apply_tag_operation import ApplyTagOperation
        from ..models.attach_lead_to_integration_operation import AttachLeadToIntegrationOperation
        from ..models.make_active_in_group_operation import MakeActiveInGroupOperation
        from ..models.make_inactive_in_group_operation import MakeInactiveInGroupOperation
        from ..models.opt_out_operation import OptOutOperation
        from ..models.remove_tag_operation import RemoveTagOperation
        from ..models.set_custom_field_operation import SetCustomFieldOperation

        d = src_dict.copy()
        id = d.pop("id")

        def _parse_operation(
            data: object,
        ) -> Union[
            "ApplyTagOperation",
            "AttachLeadToIntegrationOperation",
            "MakeActiveInGroupOperation",
            "MakeInactiveInGroupOperation",
            "OptOutOperation",
            "RemoveTagOperation",
            "SetCustomFieldOperation",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operation_type_0 = MakeActiveInGroupOperation.from_dict(data)

                return operation_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operation_type_1 = MakeInactiveInGroupOperation.from_dict(data)

                return operation_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operation_type_2 = AttachLeadToIntegrationOperation.from_dict(data)

                return operation_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operation_type_3 = ApplyTagOperation.from_dict(data)

                return operation_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operation_type_4 = RemoveTagOperation.from_dict(data)

                return operation_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operation_type_5 = SetCustomFieldOperation.from_dict(data)

                return operation_type_5
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            operation_type_6 = OptOutOperation.from_dict(data)

            return operation_type_6

        operation = _parse_operation(d.pop("operation"))

        patch_leads_body = cls(
            id=id,
            operation=operation,
        )

        return patch_leads_body
