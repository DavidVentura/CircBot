#!/usr/bin/env python3
import sys
import json
import time
import requests
import getLiveChatID
import credentials
from pprint import pprint
from datetime import datetime

VERSION = "0.3.2"
PYTHONIOENCODING = "UTF-8"
debug = 0


# Message handler
def handle_msg(msg):
    # pprint(msg)
    pAt = msg["snippet"]["publishedAt"]
    obj = {'id': msg["id"],
           'msg': msg["snippet"]["displayMessage"],
           'date': datetime.strptime(pAt, "%Y-%m-%dT%H:%M:%S.%fZ")
           }
    pprint(obj)
    print("#" * 50)
    return


def main():
    token_str = credentials.read()
    liveChatID = getLiveChatID.get_livechat_id()
    print("Live Chat ID", liveChatID)
    if not liveChatID:
        print("[] No livestream found :(")
        sys.exit(1)

    nextPageToken = ''
    while (True):

        # Make sure access token is valid before request
        if (credentials.access_token_expired):
            # Access token expired, get a new one
            # credentials.read() should refresh the token automatically
            token_str = credentials.read()

        url = 'https://content.googleapis.com/youtube/v3/liveChat/messages?liveChatId='+liveChatID+'&part=snippet,authorDetails&pageToken='+nextPageToken

        headers = {"Authorization": "Bearer " + token_str}

        r = requests.get(url, headers=headers)

        if (r.status_code == 200):
            resp = r.json()
            nextPageToken = resp["nextPageToken"]
            msgs = resp["items"]
            for msg in msgs:
                handle_msg(msg)

            delay = resp['pollingIntervalMillis']/1000
        elif (r.status_code == 401):  # Unauthorized
            delay = 10
            if not credentials.access_token_expired:
                print("Error: Unauthorized. waiting 30 seconds...")
                if (debug >= 1):
                    resp = r.json()
                    print(json.dumps(resp, indent=4, sort_keys=True))
                delay = 30
        else:
            print("Unrecognized error:\n")
            resp = r.json()
            print(json.dumps(resp, indent=4, sort_keys=True))
            delay = 30

        time.sleep(delay)


if __name__ == '__main__':
    main()
