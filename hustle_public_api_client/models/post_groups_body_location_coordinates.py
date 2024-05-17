from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostGroupsBodyLocationCoordinates")


@_attrs_define
class PostGroupsBodyLocationCoordinates:
    """The coordinates that the group location is set to.

    Attributes:
        lat (float): The latitude of the group location. Example: 39.7392358.
        lng (float): The longitude of the group location. Example: -104.990251.
    """

    lat: float
    lng: float

    def to_dict(self) -> Dict[str, Any]:
        lat = self.lat

        lng = self.lng

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "lat": lat,
                "lng": lng,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lat = d.pop("lat")

        lng = d.pop("lng")

        post_groups_body_location_coordinates = cls(
            lat=lat,
            lng=lng,
        )

        return post_groups_body_location_coordinates
