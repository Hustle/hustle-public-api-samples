"""
    Usage:
    $ python3 get_all_organizations_in_account_with_pagination.py BASE_URL EMAIL_ADDRESS CLIENT_SECRET
    eg:
    $ python3 upload_leads_csv.py https://api.hustle.com/v3 jane.doe@email.com supersecretpassword
"""

import sys
import time
import requests

if len(sys.argv) != 3:
    print(__doc__)
    sys.exit()

base_url = sys.argv[1]
client_id = sys.argv[2]
client_secret = sys.argv[3]

def get_access_token():
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    request = requests.post(f'{base_url}/oauth/token', data=payload)
    request.raise_for_status()

    json = request.json()

    access_token = json['access_token']
    scope = json['scope']
    print(f'\nuser {client_id} has scope {scope}\n')
    return access_token


def get_organizations(access_token: str):
    bearer = f'Bearer {access_token}'
    headers = {'Authorization': bearer}
    organizations = []
    cursor = ''
    while True:
        params = {'cursor': cursor} if cursor != '' else {}
        try:
            request = requests.get(f'{base_url}/organizations', headers=headers, params=params)
            request.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                # Maybe we need to try and regenerate the access_token
                access_token = get_access_token()
                bearer = f'Bearer {access_token}'
                headers = {'Authorization': bearer}
                request = requests.get(f'{base_url}/organizations', headers=headers, params=params)
            elif e.response.status_code == 429:
                # We've hit a rate limit so we need to sleep a bit. You may want to implement exponential backoff in your own script
                print(f'hit rate limit {e.response}')
                while request.status_code == 429:
                    time.sleep(1000)
                    request = requests.get(f'{base_url}/organizations', headers=headers, params=params)
            else:
                raise e
        json = request.json()
        print(json)
        organizations.extend(json['items'])
        if not json['hasMore']:
            break
        cursor = json['cursor']

    return organizations


def main():
    access_token = get_access_token()
    organizations = get_organizations(access_token)
    print(organizations)


if __name__ == "__main__":
    main()
