from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.tag import Tag


T = TypeVar("T", bound="GetTagsResponse200")


@_attrs_define
class GetTagsResponse200:
    """
    Attributes:
        items (List['Tag']): List of tags matching the query.
        cursor (Union[None, str]): Cursor for start of next set of items. If there were no items to return with the last
            cursor you passed, this will return null.
        has_more (bool): Whether there are more items to load past this cursor.
    """

    items: List["Tag"]
    cursor: Union[None, str]
    has_more: bool

    def to_dict(self) -> Dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        cursor: Union[None, str]
        cursor = self.cursor

        has_more = self.has_more

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "items": items,
                "cursor": cursor,
                "hasMore": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tag import Tag

        d = src_dict.copy()
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Tag.from_dict(items_item_data)

            items.append(items_item)

        def _parse_cursor(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        cursor = _parse_cursor(d.pop("cursor"))

        has_more = d.pop("hasMore")

        get_tags_response_200 = cls(
            items=items,
            cursor=cursor,
            has_more=has_more,
        )

        return get_tags_response_200
