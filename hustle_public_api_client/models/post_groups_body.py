from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.post_groups_body_country_code import PostGroupsBodyCountryCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_groups_body_location import PostGroupsBodyLocation


T = TypeVar("T", bound="PostGroupsBody")


@_attrs_define
class PostGroupsBody:
    """The details of the group being created.

    Attributes:
        name (str): The name of the group.
        country_code (PostGroupsBodyCountryCode): The country code of the country the group is registered in. Example:
            US.
        location (PostGroupsBodyLocation): The location of the group. This is used to assign a timezone and enforce
            hours of operation.
        organization_id (str): The organization this group belongs to.
        description (Union[Unset, str]): The user provided description of the group.
    """

    name: str
    country_code: PostGroupsBodyCountryCode
    location: "PostGroupsBodyLocation"
    organization_id: str
    description: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        country_code = self.country_code.value

        location = self.location.to_dict()

        organization_id = self.organization_id

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "countryCode": country_code,
                "location": location,
                "organizationId": organization_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_groups_body_location import PostGroupsBodyLocation

        d = src_dict.copy()
        name = d.pop("name")

        country_code = PostGroupsBodyCountryCode(d.pop("countryCode"))

        location = PostGroupsBodyLocation.from_dict(d.pop("location"))

        organization_id = d.pop("organizationId")

        description = d.pop("description", UNSET)

        post_groups_body = cls(
            name=name,
            country_code=country_code,
            location=location,
            organization_id=organization_id,
            description=description,
        )

        return post_groups_body
