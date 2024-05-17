from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.post_groups_body_location_coordinates import PostGroupsBodyLocationCoordinates


T = TypeVar("T", bound="PostGroupsBodyLocation")


@_attrs_define
class PostGroupsBodyLocation:
    """The location of the group. This is used to assign a timezone and enforce hours of operation.

    Attributes:
        label (str): The human readable location of the group. Example: Denver, CO, USA.
        coordinates (PostGroupsBodyLocationCoordinates): The coordinates that the group location is set to.
    """

    label: str
    coordinates: "PostGroupsBodyLocationCoordinates"

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        coordinates = self.coordinates.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "label": label,
                "coordinates": coordinates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_groups_body_location_coordinates import PostGroupsBodyLocationCoordinates

        d = src_dict.copy()
        label = d.pop("label")

        coordinates = PostGroupsBodyLocationCoordinates.from_dict(d.pop("coordinates"))

        post_groups_body_location = cls(
            label=label,
            coordinates=coordinates,
        )

        return post_groups_body_location
