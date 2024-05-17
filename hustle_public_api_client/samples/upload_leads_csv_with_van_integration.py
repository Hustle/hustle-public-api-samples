"""
    Usage:
    $ python3 upload_leads_csv_with_van_integration.py BASE_URL EMAIL_ADDRESS CLIENT_SECRET ORGANIZATION_ID CSV_FILENAME
    eg:
    $ python3 upload_leads_csv_with_van_integration.py https://api.hustle.com/v3 jane.doe@email.com supersecretpassword 123456 ./leads_to_upload.csv

    NOTE: This script expects your csv to be in the form:
    phoneNumber,firstName,lastName,vanId
    +12248033037,Merlin,Modlin,12345
    +12248033090,Angella,Stearn,12346
    +12248032747,Saran,Galiano,12347
"""

import sys
import csv
import time
from hustle_public_api_client import Client
from hustle_public_api_client import AuthenticatedClient
from hustle_public_api_client.api.access_token import post_oauth_token
from hustle_public_api_client.api.integrations import get_integrations
from hustle_public_api_client.models import PostOauthTokenBody, Organization, Lead, PostLeadsBody, PatchLeadsBody, \
    AttachLeadToIntegrationOperation, VanExternalLeadSchema, Integration
from hustle_public_api_client.api.organizations import get_organizations
from hustle_public_api_client.api.leads import post_leads, patch_leads

if len(sys.argv) != 6:
    print(__doc__)
    sys.exit()

base_url = sys.argv[1]
client_id = sys.argv[2]
client_secret = sys.argv[3]
organization_id = sys.argv[4]
csv_file_name = sys.argv[5]


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class HustleApiClient(AuthenticatedClient, metaclass=Singleton):
    client_id_stored = ''
    client_secret_stored = ''

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(token='', *args, **kwargs)
        self.client_id_stored = client_id
        self.client_secret_stored = client_secret
        self.refresh_token()

    def refresh_token(self):
        unauth_client = Client(base_url=base_url)
        credentials: PostOauthTokenBody = PostOauthTokenBody.from_dict({
            'client_id': self.client_id_stored,
            'client_secret': self.client_secret_stored,
            'grant_type': 'client_credentials',
        })
        token = post_oauth_token.sync_detailed(client=unauth_client, body=credentials)
        if token.status_code != 200:
            raise Exception('Credentials not valid')
        self.token = token.parsed.access_token


def get_integration_from_api(organization_id: Organization.id) -> Integration.id:
    request = get_integrations.sync_detailed(client=client, organization_id=organization_id, integration_type='van')
    if request.status_code == 401:
        # Maybe we need to try and regenerate the access_token
        client.refresh_token()
        request = get_organizations.sync_detailed(client=client)
    while request.status_code == 429:
        # We've hit a rate limit so we need to sleep a bit. You may want to implement exponential backoff in your own script
        time.sleep(1000)
        request = get_organizations.sync_detailed(client=client)
    if request.status_code != 200:
        raise Exception('Received unexpected error code on GET Integrations: {} '
                        'with message {}'.format(request.status_code, request.parsed.message))
    print(request.parsed)
    if request.parsed.items.count != 1:
        raise Exception('Organization does not have van integration')
    return request.parsed.items[0].id


def create_lead(
        lead: PostLeadsBody,
        integration_id: AttachLeadToIntegrationOperation.integration_id,
        external_lead_id: VanExternalLeadSchema.external_object.van_id,
        client: HustleApiClient
) -> Lead.id:
    lead_request = post_leads.sync_detailed(client=client, body=lead)
    if lead_request.status_code == 401:
        # Maybe we need to try and regenerate the access_token
        client.refresh_token()
        lead_request = post_leads.sync_detailed(client=client, body=lead)
    while lead_request.status_code == 429:
        # We've hit a rate limit so we need to sleep a bit. You may want to implement exponential backoff in your own script
        time.sleep(1000)
        lead_request = post_leads.sync_detailed(client=client, body=lead)
    print(lead_request.parsed)
    patch_request = PatchLeadsBody.from_dict({
        "id": lead_request.parsed.id,
        "operation": {
            "type": "attachLeadToIntegration",
            "integrationId": integration_id,
            "external": {
                "integrationType": 'van',
                "externalObject": {
                    "version": "v4",
                    "vanId": external_lead_id
                }
            }
        }
    })
    link_request = patch_leads.sync_detailed(client=client, body=patch_request)
    if link_request.status_code == 401:
        # Maybe we need to try and regenerate the access_token
        client.refresh_token()
        link_request = patch_leads.sync_detailed(client=client, body=patch_request)
    while link_request.status_code == 429:
        # We've hit a rate limit so we need to sleep a bit. You may want to implement exponential backoff in your own script
        time.sleep(1000)
        link_request = patch_leads.sync_detailed(client=client, body=patch_request)
    return link_request.parsed.id


if __name__ == '__main__':
    client = HustleApiClient(base_url=base_url, client_id=client_id, client_secret=client_secret)
    integration_id = get_integration_from_api(organization_id=organization_id)
    with open(csv_file_name) as csvfile:
        csv_reader = csv.reader(csvfile)
        for i, row in enumerate(csv_reader):
            # Skip headers row
            if i == 0:
                continue
            phone_number = row[0]
            first_name = row[1]
            last_name = row[2]
            van_id = row[3]

            lead = PostLeadsBody(
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
                organization_id=organization_id
            )
            new_lead_id = create_lead(lead=lead, integration_id=integration_id, external_lead_id=van_id, client=client)
            print('New lead with ID ', new_lead_id, ' has been created and linked with integration ', integration_id)
