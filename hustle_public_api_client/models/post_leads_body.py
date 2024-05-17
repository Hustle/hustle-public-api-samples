from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_leads_body_custom_fields import PostLeadsBodyCustomFields


T = TypeVar("T", bound="PostLeadsBody")


@_attrs_define
class PostLeadsBody:
    """
    Attributes:
        phone_number (str): The phone number of the lead. The combination of organizationId and phoneNumber represent a
            lead. Attempting to insert a new lead with these existing values will overwrite the existing lead.
        organization_id (str): The ID of the organization the lead belongs to. The combination of organizationId and
            phoneNumber represent a lead. Attempting to insert a new lead with these existing values will overwrite the
            existing lead.
        custom_fields (Union[Unset, PostLeadsBodyCustomFields]): The custom fields and associated values for the lead.
        first_name (Union[Unset, str]): The first name of the lead.
        last_name (Union[Unset, str]): The last name of the lead.
        notes (Union[Unset, str]): Notes about the lead.
        follow_up (Union[Unset, str]): Follow up comments for the lead.
        email (Union[Unset, str]): The email of the lead.
        tag_ids (Union[Unset, List[str]]): The IDs of the tags that have been applied to the lead.
    """

    phone_number: str
    organization_id: str
    custom_fields: Union[Unset, "PostLeadsBodyCustomFields"] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    follow_up: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    tag_ids: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        phone_number = self.phone_number

        organization_id = self.organization_id

        custom_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        first_name = self.first_name

        last_name = self.last_name

        notes = self.notes

        follow_up = self.follow_up

        email = self.email

        tag_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "phoneNumber": phone_number,
                "organizationId": organization_id,
            }
        )
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if follow_up is not UNSET:
            field_dict["followUp"] = follow_up
        if email is not UNSET:
            field_dict["email"] = email
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_leads_body_custom_fields import PostLeadsBodyCustomFields

        d = src_dict.copy()
        phone_number = d.pop("phoneNumber")

        organization_id = d.pop("organizationId")

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, PostLeadsBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PostLeadsBodyCustomFields.from_dict(_custom_fields)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        notes = d.pop("notes", UNSET)

        follow_up = d.pop("followUp", UNSET)

        email = d.pop("email", UNSET)

        tag_ids = cast(List[str], d.pop("tagIds", UNSET))

        post_leads_body = cls(
            phone_number=phone_number,
            organization_id=organization_id,
            custom_fields=custom_fields,
            first_name=first_name,
            last_name=last_name,
            notes=notes,
            follow_up=follow_up,
            email=email,
            tag_ids=tag_ids,
        )

        return post_leads_body
