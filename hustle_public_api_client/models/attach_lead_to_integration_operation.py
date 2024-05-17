from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.attach_lead_to_integration_operation_type import AttachLeadToIntegrationOperationType

if TYPE_CHECKING:
    from ..models.bb_luminate_external_lead_schema import BbLuminateExternalLeadSchema
    from ..models.evertrue_external_lead_schema import EvertrueExternalLeadSchema
    from ..models.salesforce_external_lead_schema import SalesforceExternalLeadSchema
    from ..models.van_external_lead_schema import VanExternalLeadSchema
    from ..models.van_my_voters_external_lead_schema import VanMyVotersExternalLeadSchema


T = TypeVar("T", bound="AttachLeadToIntegrationOperation")


@_attrs_define
class AttachLeadToIntegrationOperation:
    """
    Attributes:
        type (AttachLeadToIntegrationOperationType): This operation will attach a lead in Hustle to a lead (or similar
            object) in an integration.
        integration_id (str): The ID of the integration to attach the lead to.
        external (Union['BbLuminateExternalLeadSchema', 'EvertrueExternalLeadSchema', 'SalesforceExternalLeadSchema',
            'VanExternalLeadSchema', 'VanMyVotersExternalLeadSchema']):
    """

    type: AttachLeadToIntegrationOperationType
    integration_id: str
    external: Union[
        "BbLuminateExternalLeadSchema",
        "EvertrueExternalLeadSchema",
        "SalesforceExternalLeadSchema",
        "VanExternalLeadSchema",
        "VanMyVotersExternalLeadSchema",
    ]

    def to_dict(self) -> Dict[str, Any]:
        from ..models.evertrue_external_lead_schema import EvertrueExternalLeadSchema
        from ..models.salesforce_external_lead_schema import SalesforceExternalLeadSchema
        from ..models.van_external_lead_schema import VanExternalLeadSchema
        from ..models.van_my_voters_external_lead_schema import VanMyVotersExternalLeadSchema

        type = self.type.value

        integration_id = self.integration_id

        external: Dict[str, Any]
        if isinstance(self.external, VanExternalLeadSchema):
            external = self.external.to_dict()
        elif isinstance(self.external, VanMyVotersExternalLeadSchema):
            external = self.external.to_dict()
        elif isinstance(self.external, EvertrueExternalLeadSchema):
            external = self.external.to_dict()
        elif isinstance(self.external, SalesforceExternalLeadSchema):
            external = self.external.to_dict()
        else:
            external = self.external.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "integrationId": integration_id,
                "external": external,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bb_luminate_external_lead_schema import BbLuminateExternalLeadSchema
        from ..models.evertrue_external_lead_schema import EvertrueExternalLeadSchema
        from ..models.salesforce_external_lead_schema import SalesforceExternalLeadSchema
        from ..models.van_external_lead_schema import VanExternalLeadSchema
        from ..models.van_my_voters_external_lead_schema import VanMyVotersExternalLeadSchema

        d = src_dict.copy()
        type = AttachLeadToIntegrationOperationType(d.pop("type"))

        integration_id = d.pop("integrationId")

        def _parse_external(
            data: object,
        ) -> Union[
            "BbLuminateExternalLeadSchema",
            "EvertrueExternalLeadSchema",
            "SalesforceExternalLeadSchema",
            "VanExternalLeadSchema",
            "VanMyVotersExternalLeadSchema",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                external_type_0 = VanExternalLeadSchema.from_dict(data)

                return external_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                external_type_1 = VanMyVotersExternalLeadSchema.from_dict(data)

                return external_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                external_type_2 = EvertrueExternalLeadSchema.from_dict(data)

                return external_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                external_type_3 = SalesforceExternalLeadSchema.from_dict(data)

                return external_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            external_type_4 = BbLuminateExternalLeadSchema.from_dict(data)

            return external_type_4

        external = _parse_external(d.pop("external"))

        attach_lead_to_integration_operation = cls(
            type=type,
            integration_id=integration_id,
            external=external,
        )

        return attach_lead_to_integration_operation
