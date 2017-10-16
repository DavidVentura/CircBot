import sys
import json
import requests
import credentials


def get_livechat_id():

    token_str = credentials.read()
    url = 'https://content.googleapis.com/youtube/v3/liveBroadcasts?broadcastStatus=active&broadcastType=all&part=id%2Csnippet%2CcontentDetails'
    headers = {"Authorization": "Bearer %s" % token_str}

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        resp = r.json()
        if len(resp["items"]) == 0:
            return False
        else:
            # Should only be 1 item unless YT adds multiple livestreams
            # then we'll assume it's the first for now
            print("Live events:", len(resp["items"]))
            from pprint import pprint
            pprint(resp)
            print("*" * 50)
            streamMeta = resp["items"][0]["snippet"]
            liveChatID = streamMeta["liveChatId"]
            return liveChatID
    else:
        print("Unrecognized error:\n")
        resp = r.json()
        print(json.dumps(resp, indent=4, sort_keys=True))


def main():
    liveChatID = get_livechat_id()
    if not liveChatID:
        print("No livestream found :(")
        sys.exit(1)
    print(liveChatID)


if __name__ == '__main__':
    main()
