from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_tags_agent_visibility import GetTagsAgentVisibility
from ...models.get_tags_response_200 import GetTagsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, str] = UNSET,
    agent_visibility: Union[Unset, GetTagsAgentVisibility] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["id"] = id

    params["name"] = name

    params["organizationId"] = organization_id

    json_agent_visibility: Union[Unset, str] = UNSET
    if not isinstance(agent_visibility, Unset):
        json_agent_visibility = agent_visibility.value

    params["agentVisibility"] = json_agent_visibility

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/tags",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetTagsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetTagsResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetTagsResponse200]]:
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
    name: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, str] = UNSET,
    agent_visibility: Union[Unset, GetTagsAgentVisibility] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> Response[Union[ErrorResponse, GetTagsResponse200]]:
    """Get Tags

     Get a list of tags scoped by query parameters.

    Args:
        id (Union[Unset, str]): Tag ID
        name (Union[Unset, str]): Tag name. This is not a partial or fuzzy match but looks for an
            exact match of the tag name.
        organization_id (Union[Unset, str]): Organization ID
        agent_visibility (Union[Unset, GetTagsAgentVisibility]): The context in which an agent can
            see and collect tags.
            LEAD_PROFILES: Agents will be able to see these while sending messages and use them to
            collect info about contacts.
            OPT_OUT: Specifically for opt-out reasons. Will only be displayed when agents opt out a
            contact.
            NEVER: Only for admins. Agents will never see this tag.
        cursor (Union[Unset, str]): Cursor for start of next set of items. Pass whatever you
            receive from the response to get the next elements in the array.
        limit (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTagsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        name=name,
        organization_id=organization_id,
        agent_visibility=agent_visibility,
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
    name: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, str] = UNSET,
    agent_visibility: Union[Unset, GetTagsAgentVisibility] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> Optional[Union[ErrorResponse, GetTagsResponse200]]:
    """Get Tags

     Get a list of tags scoped by query parameters.

    Args:
        id (Union[Unset, str]): Tag ID
        name (Union[Unset, str]): Tag name. This is not a partial or fuzzy match but looks for an
            exact match of the tag name.
        organization_id (Union[Unset, str]): Organization ID
        agent_visibility (Union[Unset, GetTagsAgentVisibility]): The context in which an agent can
            see and collect tags.
            LEAD_PROFILES: Agents will be able to see these while sending messages and use them to
            collect info about contacts.
            OPT_OUT: Specifically for opt-out reasons. Will only be displayed when agents opt out a
            contact.
            NEVER: Only for admins. Agents will never see this tag.
        cursor (Union[Unset, str]): Cursor for start of next set of items. Pass whatever you
            receive from the response to get the next elements in the array.
        limit (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTagsResponse200]
    """

    return sync_detailed(
        client=client,
        id=id,
        name=name,
        organization_id=organization_id,
        agent_visibility=agent_visibility,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, str] = UNSET,
    agent_visibility: Union[Unset, GetTagsAgentVisibility] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> Response[Union[ErrorResponse, GetTagsResponse200]]:
    """Get Tags

     Get a list of tags scoped by query parameters.

    Args:
        id (Union[Unset, str]): Tag ID
        name (Union[Unset, str]): Tag name. This is not a partial or fuzzy match but looks for an
            exact match of the tag name.
        organization_id (Union[Unset, str]): Organization ID
        agent_visibility (Union[Unset, GetTagsAgentVisibility]): The context in which an agent can
            see and collect tags.
            LEAD_PROFILES: Agents will be able to see these while sending messages and use them to
            collect info about contacts.
            OPT_OUT: Specifically for opt-out reasons. Will only be displayed when agents opt out a
            contact.
            NEVER: Only for admins. Agents will never see this tag.
        cursor (Union[Unset, str]): Cursor for start of next set of items. Pass whatever you
            receive from the response to get the next elements in the array.
        limit (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTagsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        name=name,
        organization_id=organization_id,
        agent_visibility=agent_visibility,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    organization_id: Union[Unset, str] = UNSET,
    agent_visibility: Union[Unset, GetTagsAgentVisibility] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> Optional[Union[ErrorResponse, GetTagsResponse200]]:
    """Get Tags

     Get a list of tags scoped by query parameters.

    Args:
        id (Union[Unset, str]): Tag ID
        name (Union[Unset, str]): Tag name. This is not a partial or fuzzy match but looks for an
            exact match of the tag name.
        organization_id (Union[Unset, str]): Organization ID
        agent_visibility (Union[Unset, GetTagsAgentVisibility]): The context in which an agent can
            see and collect tags.
            LEAD_PROFILES: Agents will be able to see these while sending messages and use them to
            collect info about contacts.
            OPT_OUT: Specifically for opt-out reasons. Will only be displayed when agents opt out a
            contact.
            NEVER: Only for admins. Agents will never see this tag.
        cursor (Union[Unset, str]): Cursor for start of next set of items. Pass whatever you
            receive from the response to get the next elements in the array.
        limit (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTagsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            name=name,
            organization_id=organization_id,
            agent_visibility=agent_visibility,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
