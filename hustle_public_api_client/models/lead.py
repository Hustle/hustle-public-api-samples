from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.lead_type import LeadType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lead_custom_fields import LeadCustomFields


T = TypeVar("T", bound="Lead")


@_attrs_define
class Lead:
    """A lead represents someone that messages and calls are sent to.

    Attributes:
        id (str): The ID of the lead.
        type (LeadType): The type of object the attached ID corresponds to.
        phone_number (str): The phone number of the lead. The combination of organizationId and phoneNumber represent a
            lead. Attempting to insert a new lead with these existing values will overwrite the existing lead.
        organization_id (str): The ID of the organization the lead belongs to. The combination of organizationId and
            phoneNumber represent a lead. Attempting to insert a new lead with these existing values will overwrite the
            existing lead.
        active_group_ids (List[str]): The IDs of the groups the lead belongs to where they are still active.
        inactive_group_ids (List[str]): The IDs of the groups the lead belongs to where the lead is inactive. Because
            deleting a lead from a group is not allowed, the only way to stop a lead from receiving messages meant for a
            group is to make them inactive.
        custom_fields (LeadCustomFields): The custom fields and associated values for the lead.
        tag_ids (List[str]): The IDs of the tags that have been applied to the lead.
        global_opted_out (bool): Whether or not the lead has opted out of all messages. If this is true, the lead will
            not receive any messages.
        created_at (str): An ISO-8601 string representing the date the agent was created.
        first_name (Union[Unset, str]): The first name of the lead.
        last_name (Union[Unset, str]): The last name of the lead.
        notes (Union[Unset, str]): Notes about the lead.
        follow_up (Union[Unset, str]): Follow up comments for the lead.
        email (Union[Unset, str]): The email of the lead.
    """

    id: str
    type: LeadType
    phone_number: str
    organization_id: str
    active_group_ids: List[str]
    inactive_group_ids: List[str]
    custom_fields: "LeadCustomFields"
    tag_ids: List[str]
    global_opted_out: bool
    created_at: str
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    follow_up: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        phone_number = self.phone_number

        organization_id = self.organization_id

        active_group_ids = self.active_group_ids

        inactive_group_ids = self.inactive_group_ids

        custom_fields = self.custom_fields.to_dict()

        tag_ids = self.tag_ids

        global_opted_out = self.global_opted_out

        created_at = self.created_at

        first_name = self.first_name

        last_name = self.last_name

        notes = self.notes

        follow_up = self.follow_up

        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "type": type,
                "phoneNumber": phone_number,
                "organizationId": organization_id,
                "activeGroupIds": active_group_ids,
                "inactiveGroupIds": inactive_group_ids,
                "customFields": custom_fields,
                "tagIds": tag_ids,
                "globalOptedOut": global_opted_out,
                "createdAt": created_at,
            }
        )
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.lead_custom_fields import LeadCustomFields

        d = src_dict.copy()
        id = d.pop("id")

        type = LeadType(d.pop("type"))

        phone_number = d.pop("phoneNumber")

        organization_id = d.pop("organizationId")

        active_group_ids = cast(List[str], d.pop("activeGroupIds"))

        inactive_group_ids = cast(List[str], d.pop("inactiveGroupIds"))

        custom_fields = LeadCustomFields.from_dict(d.pop("customFields"))

        tag_ids = cast(List[str], d.pop("tagIds"))

        global_opted_out = d.pop("globalOptedOut")

        created_at = d.pop("createdAt")

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        notes = d.pop("notes", UNSET)

        follow_up = d.pop("followUp", UNSET)

        email = d.pop("email", UNSET)

        lead = cls(
            id=id,
            type=type,
            phone_number=phone_number,
            organization_id=organization_id,
            active_group_ids=active_group_ids,
            inactive_group_ids=inactive_group_ids,
            custom_fields=custom_fields,
            tag_ids=tag_ids,
            global_opted_out=global_opted_out,
            created_at=created_at,
            first_name=first_name,
            last_name=last_name,
            notes=notes,
            follow_up=follow_up,
            email=email,
        )

        return lead
