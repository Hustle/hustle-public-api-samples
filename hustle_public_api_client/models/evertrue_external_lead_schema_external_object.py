from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.evertrue_external_lead_schema_external_object_version import (
    EvertrueExternalLeadSchemaExternalObjectVersion,
)

T = TypeVar("T", bound="EvertrueExternalLeadSchemaExternalObject")


@_attrs_define
class EvertrueExternalLeadSchemaExternalObject:
    """
    Attributes:
        version (EvertrueExternalLeadSchemaExternalObjectVersion):
        remote_id (str):
    """

    version: EvertrueExternalLeadSchemaExternalObjectVersion
    remote_id: str

    def to_dict(self) -> Dict[str, Any]:
        version = self.version.value

        remote_id = self.remote_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "version": version,
                "remoteId": remote_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = EvertrueExternalLeadSchemaExternalObjectVersion(d.pop("version"))

        remote_id = d.pop("remoteId")

        evertrue_external_lead_schema_external_object = cls(
            version=version,
            remote_id=remote_id,
        )

        return evertrue_external_lead_schema_external_object
