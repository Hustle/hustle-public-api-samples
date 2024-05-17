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


def create_lead(phone_number: str, first_name: str, last_name: str, access_token: str):
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
    print(json)


def main():
    access_token = get_access_token()

    with open(csv_file_name) as csvfile:
        csv_reader = csv.reader(csvfile)
        for i, row in enumerate(csv_reader):
            # Skip headers row
            if i == 0:
                continue
            phone_number = row[0]
            first_name = row[1]
            last_name = row[2]

            try:
                create_lead(phone_number, first_name, last_name, access_token)
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 401:
                    # Maybe we need to try and regenerate the access_token
                    access_token = get_access_token()
                    create_lead(phone_number, first_name, last_name, access_token)
                elif e.response.status_code == 429:
                    # We've hit a rate limit so we need to sleep a bit. You may want to implement exponential backoff in your own script
                    print(f'hit rate limit {e.response}')
                    time.sleep(1000)
                    create_lead(phone_number, first_name, last_name, access_token)
                else:
                    raise e
            break


if __name__ == "__main__":
    main()
