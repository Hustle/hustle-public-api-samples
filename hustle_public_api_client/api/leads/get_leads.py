from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_leads_lead_status_in_group import GetLeadsLeadStatusInGroup
from ...models.get_leads_response_200 import GetLeadsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, str] = UNSET,
    group_id: Union[Unset, str] = UNSET,
    lead_status_in_group: Union[Unset, GetLeadsLeadStatusInGroup] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["id"] = id

    params["organizationId"] = organization_id

    params["groupId"] = group_id

    json_lead_status_in_group: Union[Unset, str] = UNSET
    if not isinstance(lead_status_in_group, Unset):
        json_lead_status_in_group = lead_status_in_group.value

    params["leadStatusInGroup"] = json_lead_status_in_group

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/leads",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetLeadsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetLeadsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetLeadsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, str] = UNSET,
    group_id: Union[Unset, str] = UNSET,
    lead_status_in_group: Union[Unset, GetLeadsLeadStatusInGroup] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> Response[Union[ErrorResponse, GetLeadsResponse200]]:
    """Get Leads

     Get a list of leads scoped by the query parameters.

    Args:
        id (Union[Unset, str]): Lead ID
        organization_id (Union[Unset, str]): Organization ID.
        group_id (Union[Unset, str]): A Group ID. This will return a lead that has this group
            inside of the activeGroupIds array. To also include inactive groups, use the
            searchInactiveGroups query parameter.
        lead_status_in_group (Union[Unset, GetLeadsLeadStatusInGroup]): When a groupId is passed,
            this determines whether we look in the activeGroupIds array, inactiveGroupIds array, or
            both. Defaults to active.
        cursor (Union[Unset, str]): Cursor for start of next set of items. Pass whatever you
            receive from the response to get the next elements in the array.
        limit (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetLeadsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        organization_id=organization_id,
        group_id=group_id,
        lead_status_in_group=lead_status_in_group,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, str] = UNSET,
    group_id: Union[Unset, str] = UNSET,
    lead_status_in_group: Union[Unset, GetLeadsLeadStatusInGroup] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> Optional[Union[ErrorResponse, GetLeadsResponse200]]:
    """Get Leads

     Get a list of leads scoped by the query parameters.

    Args:
        id (Union[Unset, str]): Lead ID
        organization_id (Union[Unset, str]): Organization ID.
        group_id (Union[Unset, str]): A Group ID. This will return a lead that has this group
            inside of the activeGroupIds array. To also include inactive groups, use the
            searchInactiveGroups query parameter.
        lead_status_in_group (Union[Unset, GetLeadsLeadStatusInGroup]): When a groupId is passed,
            this determines whether we look in the activeGroupIds array, inactiveGroupIds array, or
            both. Defaults to active.
        cursor (Union[Unset, str]): Cursor for start of next set of items. Pass whatever you
            receive from the response to get the next elements in the array.
        limit (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetLeadsResponse200]
    """

    return sync_detailed(
        client=client,
        id=id,
        organization_id=organization_id,
        group_id=group_id,
        lead_status_in_group=lead_status_in_group,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, str] = UNSET,
    group_id: Union[Unset, str] = UNSET,
    lead_status_in_group: Union[Unset, GetLeadsLeadStatusInGroup] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> Response[Union[ErrorResponse, GetLeadsResponse200]]:
    """Get Leads

     Get a list of leads scoped by the query parameters.

    Args:
        id (Union[Unset, str]): Lead ID
        organization_id (Union[Unset, str]): Organization ID.
        group_id (Union[Unset, str]): A Group ID. This will return a lead that has this group
            inside of the activeGroupIds array. To also include inactive groups, use the
            searchInactiveGroups query parameter.
        lead_status_in_group (Union[Unset, GetLeadsLeadStatusInGroup]): When a groupId is passed,
            this determines whether we look in the activeGroupIds array, inactiveGroupIds array, or
            both. Defaults to active.
        cursor (Union[Unset, str]): Cursor for start of next set of items. Pass whatever you
            receive from the response to get the next elements in the array.
        limit (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetLeadsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        organization_id=organization_id,
        group_id=group_id,
        lead_status_in_group=lead_status_in_group,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, str] = UNSET,
    group_id: Union[Unset, str] = UNSET,
    lead_status_in_group: Union[Unset, GetLeadsLeadStatusInGroup] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> Optional[Union[ErrorResponse, GetLeadsResponse200]]:
    """Get Leads

     Get a list of leads scoped by the query parameters.

    Args:
        id (Union[Unset, str]): Lead ID
        organization_id (Union[Unset, str]): Organization ID.
        group_id (Union[Unset, str]): A Group ID. This will return a lead that has this group
            inside of the activeGroupIds array. To also include inactive groups, use the
            searchInactiveGroups query parameter.
        lead_status_in_group (Union[Unset, GetLeadsLeadStatusInGroup]): When a groupId is passed,
            this determines whether we look in the activeGroupIds array, inactiveGroupIds array, or
            both. Defaults to active.
        cursor (Union[Unset, str]): Cursor for start of next set of items. Pass whatever you
            receive from the response to get the next elements in the array.
        limit (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetLeadsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            organization_id=organization_id,
            group_id=group_id,
            lead_status_in_group=lead_status_in_group,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
