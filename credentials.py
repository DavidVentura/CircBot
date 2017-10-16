import sys
import os.path
import httplib2
from oauth2client import client


class Credentials:
    credentials = {}

    def expired(self):
        return self.credentials.access_token_expired

    def read(self):
        if not os.path.isfile("OAuthCredentials.json"):
            print("Auth first")
            sys.exit(1)

        credentialsFile = open("OAuthCredentials.json", "r")
        credentialsJSON = credentialsFile.read()

        self.credentials = client.OAuth2Credentials.from_json(credentialsJSON)

        token_obj = self.credentials.get_access_token()
        token_str = str(token_obj.access_token)
        return token_str

    def auth(self):
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

        self.credentials = flow.step2_exchange(auth_code)
        self.credentials.authorize(httplib2.Http())

        outFile = open("OAuthCredentials.json", "w")
        outFile.write(str(self.credentials.to_json()))
        outFile.close()


if __name__ == '__main__':
    c = Credentials()
    c.auth()
