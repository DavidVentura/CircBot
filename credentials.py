import sys
import os.path
import httplib2
from oauth2client import client


def read():
    if not os.path.isfile("OAuthCredentials.json"):
        print("Auth first")
        sys.exit(1)

    credentialsFile = open("OAuthCredentials.json", "r")
    credentialsJSON = credentialsFile.read()

    credentials = client.OAuth2Credentials.from_json(credentialsJSON)

    token_obj = credentials.get_access_token()
    token_str = str(token_obj.access_token)
    return token_str


def auth():
    if os.path.isfile("OAuthCredentials.json"):
        print("Trying to auth but OAuthCredentials.json exists")
        return
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
    auth()
