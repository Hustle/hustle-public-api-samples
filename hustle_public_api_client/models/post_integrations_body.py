from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pdi_create_integration import PDICreateIntegration
    from ..models.van_create_integration import VanCreateIntegration
    from ..models.van_my_voters_create_integration import VanMyVotersCreateIntegration


T = TypeVar("T", bound="PostIntegrationsBody")


@_attrs_define
class PostIntegrationsBody:
    """
    Attributes:
        organization_id (str): Owning Organization ID.
        integration (Union['PDICreateIntegration', 'VanCreateIntegration', 'VanMyVotersCreateIntegration']):
    """

    organization_id: str
    integration: Union["PDICreateIntegration", "VanCreateIntegration", "VanMyVotersCreateIntegration"]

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pdi_create_integration import PDICreateIntegration
        from ..models.van_create_integration import VanCreateIntegration

        organization_id = self.organization_id

        integration: Dict[str, Any]
        if isinstance(self.integration, PDICreateIntegration):
            integration = self.integration.to_dict()
        elif isinstance(self.integration, VanCreateIntegration):
            integration = self.integration.to_dict()
        else:
            integration = self.integration.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "organizationId": organization_id,
                "integration": integration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pdi_create_integration import PDICreateIntegration
        from ..models.van_create_integration import VanCreateIntegration
        from ..models.van_my_voters_create_integration import VanMyVotersCreateIntegration

        d = src_dict.copy()
        organization_id = d.pop("organizationId")

        def _parse_integration(
            data: object,
        ) -> Union["PDICreateIntegration", "VanCreateIntegration", "VanMyVotersCreateIntegration"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                integration_type_0 = PDICreateIntegration.from_dict(data)

                return integration_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                integration_type_1 = VanCreateIntegration.from_dict(data)

                return integration_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            integration_type_2 = VanMyVotersCreateIntegration.from_dict(data)

            return integration_type_2

        integration = _parse_integration(d.pop("integration"))

        post_integrations_body = cls(
            organization_id=organization_id,
            integration=integration,
        )

        return post_integrations_body
