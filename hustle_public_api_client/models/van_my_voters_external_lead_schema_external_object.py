from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.van_my_voters_external_lead_schema_external_object_version import (
    VanMyVotersExternalLeadSchemaExternalObjectVersion,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VanMyVotersExternalLeadSchemaExternalObject")


@_attrs_define
class VanMyVotersExternalLeadSchemaExternalObject:
    """
    Attributes:
        version (VanMyVotersExternalLeadSchemaExternalObjectVersion):
        van_id (str):
        van_phone_id (Union[Unset, float]):
    """

    version: VanMyVotersExternalLeadSchemaExternalObjectVersion
    van_id: str
    van_phone_id: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        version = self.version.value

        van_id = self.van_id

        van_phone_id = self.van_phone_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "version": version,
                "vanId": van_id,
            }
        )
        if van_phone_id is not UNSET:
            field_dict["vanPhoneId"] = van_phone_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = VanMyVotersExternalLeadSchemaExternalObjectVersion(d.pop("version"))

        van_id = d.pop("vanId")

        van_phone_id = d.pop("vanPhoneId", UNSET)

        van_my_voters_external_lead_schema_external_object = cls(
            version=version,
            van_id=van_id,
            van_phone_id=van_phone_id,
        )

        return van_my_voters_external_lead_schema_external_object
