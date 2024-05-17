from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.bb_luminate_external_lead_schema_external_object_version import (
    BbLuminateExternalLeadSchemaExternalObjectVersion,
)

T = TypeVar("T", bound="BbLuminateExternalLeadSchemaExternalObject")


@_attrs_define
class BbLuminateExternalLeadSchemaExternalObject:
    """
    Attributes:
        version (BbLuminateExternalLeadSchemaExternalObjectVersion):
        constituent_id (str):
    """

    version: BbLuminateExternalLeadSchemaExternalObjectVersion
    constituent_id: str

    def to_dict(self) -> Dict[str, Any]:
        version = self.version.value

        constituent_id = self.constituent_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "version": version,
                "constituentId": constituent_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = BbLuminateExternalLeadSchemaExternalObjectVersion(d.pop("version"))

        constituent_id = d.pop("constituentId")

        bb_luminate_external_lead_schema_external_object = cls(
            version=version,
            constituent_id=constituent_id,
        )

        return bb_luminate_external_lead_schema_external_object
