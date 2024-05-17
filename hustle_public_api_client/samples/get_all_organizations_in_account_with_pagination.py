"""
    Usage:
    $ python3 get_all_organizations_in_account_with_pagination.py BASE_URL EMAIL_ADDRESS CLIENT_SECRET
    eg:
    $ python3 upload_leads_csv.py https://api.hustle.com/v3 jane.doe@email.com supersecretpassword
"""

import sys
import time
from hustle_public_api_client import Client
from hustle_public_api_client import AuthenticatedClient
from hustle_public_api_client.api.access_token import post_oauth_token
from hustle_public_api_client.models import PostOauthTokenBody, Organization
from hustle_public_api_client.api.organizations import get_organizations

if len(sys.argv) != 3:
    print(__doc__)
    sys.exit()

base_url = sys.argv[1]
client_id = sys.argv[2]
client_secret = sys.argv[3]


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


def get_organizations_from_api():
    retrieved_organizations = []
    cursor = None
    while True:
        request = get_organizations.sync_detailed(client=client, cursor=cursor)
        if request.status_code == 401:
            client.refresh_token()
            request = get_organizations.sync_detailed(client=client)
        while request.status_code == 429:
            time.sleep(1000)
            request = get_organizations.sync_detailed(client=client)
        print(request.parsed)
        retrieved_organizations.extend(request.parsed.items)
        if not request.parsed.has_more:
            break
        cursor = request.parsed.cursor

    return retrieved_organizations


if __name__ == '__main__':
    client = HustleApiClient(base_url=base_url, client_id=client_id, client_secret=client_secret)
    organizations = get_organizations_from_api()
    print(organizations)
