# This script is licensed under the Apace 2.0 License
# This script is a derivative work of the script at
# https://developers.google.com/api-client-library/python/auth/installed-app

import httplib2
from oauth2client import client


def main():
    flow = client.flow_from_clientsecrets(
        'client_secrets.json',
        scope='https://www.googleapis.com/auth/youtube.readonly https://www.googleapis.com/auth/youtube https://www.googleapis.com/auth/youtube.force-ssl',
        redirect_uri='urn:ietf:wg:oauth:2.0:oob')

    auth_uri = flow.step1_get_authorize_url()
    print(auth_uri)

    print("Open the shown link")
    auth_code = input('Enter the auth code: ')

    credentials = flow.step2_exchange(auth_code)
    credentials.authorize(httplib2.Http())

    outFile = open("OAuthCredentials.json", "w")
    outFile.write(str(credentials.to_json()))
    outFile.close()


if __name__ == '__main__':
    main()
