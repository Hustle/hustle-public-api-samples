"""
    This script assumes that there is only one VAN integration on the org. If you have multiple, be sure to parse
    the GET Integrations response for the one you are interested in.

    Usage:
    $ python3 upload_leads_csv.py BASE_URL EMAIL_ADDRESS CLIENT_SECRET ORGANIZATION_ID CSV_FILENAME
    eg:
    $ python3 upload_leads_csv.py https://api.hustle.com/v3 jane.doe@email.com supersecretpassword 123456 ./leads_to_upload.csv

    NOTE: This script expects your csv to be in the form:
    phoneNumber,firstName,lastName,vanId
    +12248033037,Merlin,Modlin,12345
    +12248033090,Angella,Stearn,12346
    +12248032747,Saran,Galiano,12347
"""

import sys
import csv
import time
import requests

if len(sys.argv) != 6:
    print(__doc__)
    sys.exit()

base_url = sys.argv[1]
client_id = sys.argv[2]
client_secret = sys.argv[3]
organization_id = sys.argv[4]
csv_file_name = sys.argv[5]


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


def get_integration(access_token: str):
    bearer = f'Bearer {access_token}'
    headers = {'Authorization': bearer}
    params = {'organizationId': organization_id, 'integrationType': 'van'}
    request = requests.get(f'{base_url}/integrations', headers=headers, params=params)
    if request.status_code == 404:
        print('No van integration in org')
    request.raise_for_status()
    json = request.json()
    print(json)
    return json['items'][0]['id']


def create_lead(phone_number: str, first_name: str, last_name: str, van_id: str, access_token: str, integration_id: str):
    payload = {
        'firstName': first_name,
        'lastName': last_name,
        'phoneNumber': phone_number,
        'organizationId': organization_id
    }
    headers = {'Authorization': f'Bearer {access_token}'}
    request = requests.post(
        f'{base_url}/leads',
        json=payload,
        headers=headers
    )
    request.raise_for_status()
    json = request.json()
    lead_id = json['id']

    payload = {
        "id": lead_id,
        "operation": {
            "type": "attachLeadToIntegration",
            "integrationId": integration_id,
            "external": {
                "integrationType": 'van',
                "externalObject": {
                    "version": "v4",
                    "vanId": van_id
                }
            }
        }
    }
    response = requests.request("PATCH", url='https://api.hustle.com/v3/leads', json=payload,
                                headers={'Authorization': f'Bearer {access_token}'})
    request.raise_for_status()
    print('Successfully created lead {} and linked to integration {}'.format(lead_id, integration_id))

def main():
    access_token = get_access_token()
    integration_id = get_integration(access_token)

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

            try:
                create_lead(phone_number, first_name, last_name, van_id, access_token, integration_id)
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 401:
                    # Maybe we need to try and regenerate the access_token
                    access_token = get_access_token()
                    create_lead(phone_number, first_name, last_name, van_id, access_token, integration_id)
                elif e.response.status_code == 429:
                    # We've hit a rate limit so we need to sleep a bit. You may want to implement exponential backoff in your own script
                    print(f'hit rate limit {e.response}')
                    time.sleep(1000)
                    create_lead(phone_number, first_name, last_name, van_id, access_token, integration_id)
                else:
                    raise e
            break


if __name__ == "__main__":
    main()
