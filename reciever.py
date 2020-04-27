from time import sleep
import datetime
import requests

username = 'Steve'
last_received = 0
while True:
    # text = input()
    response = requests.get(
        'http://127.0.0.1:5000/messages',
        params={'after': last_received}
    )
    if response.status_code == 200:

        messages = response.json()['messages']

        for message in messages:
            print(message['username'],
                  datetime.datetime.fromtimestamp(message['time']))
            print(message['text'])
            print()
            last_received = message['time']

    sleep(1)
