"""
    Usage:
    $ python3 upload_leads_csv.py BASE_URL EMAIL_ADDRESS CLIENT_SECRET ORGANIZATION_ID CSV_FILENAME
    eg:
    $ python3 upload_leads_csv.py https://api.hustle.com/v3 jane.doe@email.com supersecretpassword 123456 ./leads_to_upload.csv

    NOTE: This script expects your csv to be in the form:
    phoneNumber,firstName,lastName
    +12248033037,Merlin,Modlin
    +12248033090,Angella,Stearn
    +12248032747,Saran,Galiano
"""

import sys
import csv
import time
from hustle_public_api_client import Client
from hustle_public_api_client import AuthenticatedClient
from hustle_public_api_client.api.access_token import post_oauth_token
from hustle_public_api_client.models import PostOauthTokenBody, Lead, PostLeadsBody
from hustle_public_api_client.api.leads import post_leads

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


def create_lead(lead: PostLeadsBody, client: HustleApiClient) -> Lead.id:
    request = post_leads.sync_detailed(client=client, body=lead)
    if request.status_code == 401:
        # Maybe we need to try and regenerate the access_token
        client.refresh_token()
        request = post_leads.sync_detailed(client=client, body=lead)
    while request.status_code == 429:
        # We've hit a rate limit so we need to sleep a bit. You may want to implement exponential backoff in your own script
        time.sleep(1000)
        request = post_leads.sync_detailed(client=client, body=lead)
    print(request.parsed)
    return request.parsed.id


if __name__ == '__main__':
    client = HustleApiClient(base_url=base_url, client_id=client_id, client_secret=client_secret)
    with open(csv_file_name) as csvfile:
        csv_reader = csv.reader(csvfile)
        for i, row in enumerate(csv_reader):
            # Skip headers row
            if i == 0:
                continue
            phone_number = row[0]
            first_name = row[1]
            last_name = row[2]

            lead = PostLeadsBody(
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
                organization_id=organization_id
            )
            new_lead_id = create_lead(lead, client)
            print('New lead with ID ', new_lead_id, ' has been created')
