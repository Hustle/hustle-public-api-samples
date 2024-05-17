from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.group_country_code import GroupCountryCode
from ..models.group_type import GroupType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_location import GroupLocation


T = TypeVar("T", bound="Group")


@_attrs_define
class Group:
    """A group belongs to an Organization and organizes leads/agents/goals.

    Attributes:
        id (str): The ID of the group.
        type (GroupType): The type of object the attached ID corresponds to.
        name (str): The name of the group.
        country_code (GroupCountryCode): The country code of the country the group is registered in. Example: US.
        active (bool): Whether or not the group is active.
        organization_id (str): The organization this group belongs to.
        timezone (str): The timezone of the group. Represented as an IANA Zone ID. Example: America/Denver.
        created_at (str): An ISO-8601 string representing the date the group was created.
        description (Union[Unset, str]): The user provided description of the group.
        location (Union[Unset, GroupLocation]): The location of the group.
    """

    id: str
    type: GroupType
    name: str
    country_code: GroupCountryCode
    active: bool
    organization_id: str
    timezone: str
    created_at: str
    description: Union[Unset, str] = UNSET
    location: Union[Unset, "GroupLocation"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        name = self.name

        country_code = self.country_code.value

        active = self.active

        organization_id = self.organization_id

        timezone = self.timezone

        created_at = self.created_at

        description = self.description

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "type": type,
                "name": name,
                "countryCode": country_code,
                "active": active,
                "organizationId": organization_id,
                "timezone": timezone,
                "createdAt": created_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_location import GroupLocation

        d = src_dict.copy()
        id = d.pop("id")

        type = GroupType(d.pop("type"))

        name = d.pop("name")

        country_code = GroupCountryCode(d.pop("countryCode"))

        active = d.pop("active")

        organization_id = d.pop("organizationId")

        timezone = d.pop("timezone")

        created_at = d.pop("createdAt")

        description = d.pop("description", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, GroupLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = GroupLocation.from_dict(_location)

        group = cls(
            id=id,
            type=type,
            name=name,
            country_code=country_code,
            active=active,
            organization_id=organization_id,
            timezone=timezone,
            created_at=created_at,
            description=description,
            location=location,
        )

        return group
