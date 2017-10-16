# CircBot
YouTube LiveStream Chatbot

# Quickstart
1. pip3 install oauth2client httplib2 requests
2. Make a new project with the [Google API Console](https://console.developers.google.com/apis/) and enable the Youtube Data API.  
3. Add OAuth API credentials, download the JSON file and save it as client_secrets.json in the project folder
4. Run credentials.py ("python3 credentials.py"), approve the OAuth request in your webbrowser, and copy the auth code to the console
5. Start the stream so that the bot can fetch the live chat identifier
6. Run main.py ("python3 main.py")


# Related Documentaion and Links
https://developers.google.com/youtube/v3/live/docs/liveChatMessages
https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list
https://developers.google.com/youtube/v3/live/getting-started  
https://developers.google.com/api-client-library/python/auth/installed-app

http://docs.python-requests.org/en/latest/user/quickstart/
