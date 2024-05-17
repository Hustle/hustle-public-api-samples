from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.group_location_coordinates import GroupLocationCoordinates


T = TypeVar("T", bound="GroupLocation")


@_attrs_define
class GroupLocation:
    """The location of the group.

    Attributes:
        label (str): The human readable location of the group. Example: Denver, CO, USA.
        coordinates (GroupLocationCoordinates): The coordinates that the group location is set to.
    """

    label: str
    coordinates: "GroupLocationCoordinates"

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
        from ..models.group_location_coordinates import GroupLocationCoordinates

        d = src_dict.copy()
        label = d.pop("label")

        coordinates = GroupLocationCoordinates.from_dict(d.pop("coordinates"))

        group_location = cls(
            label=label,
            coordinates=coordinates,
        )

        return group_location
