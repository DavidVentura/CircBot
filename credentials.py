import sys
import os.path
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
