from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pdi_patch_integration import PDIPatchIntegration
    from ..models.van_my_voters_patch_integration import VanMyVotersPatchIntegration
    from ..models.van_patch_integration import VanPatchIntegration


T = TypeVar("T", bound="PatchIntegrationsBody")


@_attrs_define
class PatchIntegrationsBody:
    """
    Attributes:
        integration_id (str): Id of the integration to be updated
        operation (Union['PDIPatchIntegration', 'VanMyVotersPatchIntegration', 'VanPatchIntegration']):
    """

    integration_id: str
    operation: Union["PDIPatchIntegration", "VanMyVotersPatchIntegration", "VanPatchIntegration"]

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pdi_patch_integration import PDIPatchIntegration
        from ..models.van_patch_integration import VanPatchIntegration

        integration_id = self.integration_id

        operation: Dict[str, Any]
        if isinstance(self.operation, PDIPatchIntegration):
            operation = self.operation.to_dict()
        elif isinstance(self.operation, VanPatchIntegration):
            operation = self.operation.to_dict()
        else:
            operation = self.operation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "integrationId": integration_id,
                "operation": operation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pdi_patch_integration import PDIPatchIntegration
        from ..models.van_my_voters_patch_integration import VanMyVotersPatchIntegration
        from ..models.van_patch_integration import VanPatchIntegration

        d = src_dict.copy()
        integration_id = d.pop("integrationId")

        def _parse_operation(
            data: object,
        ) -> Union["PDIPatchIntegration", "VanMyVotersPatchIntegration", "VanPatchIntegration"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operation_type_0 = PDIPatchIntegration.from_dict(data)

                return operation_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operation_type_1 = VanPatchIntegration.from_dict(data)

                return operation_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            operation_type_2 = VanMyVotersPatchIntegration.from_dict(data)

            return operation_type_2

        operation = _parse_operation(d.pop("operation"))

        patch_integrations_body = cls(
            integration_id=integration_id,
            operation=operation,
        )

        return patch_integrations_body
