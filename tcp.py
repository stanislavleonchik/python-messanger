import time
from flask import Flask, request

app = Flask(__name__)
messages = [
    {'username': 'John', 'time': time.time(), 'text': 'Hi!'},
    {'username': 'Marry', 'time': time.time(), 'text': 'Poshel naxui :D'}]
password_storage = {
    'John': '12345',
    'Mary': '54321'
}

@app.route("/status")
def statusm():
    k = 0
    for i in password_storage:
        k += 1

    return {'status': True,
            'datetime': str(time.time()),
            'number_of_members': k,
            'messages_count': len(messages)}


@app.route("/send", methods=['POST'])
def sendm():
    username = request.json['username']
    password = request.json['password']
    text = request.json['text']

    if username not in password_storage:
        password_storage[username] = password

    if not isinstance(username, str) or len(username) == 0:
        return {'ok': False}
    if not isinstance(text, str) or len(text) == 0:
        return {'ok': False}
    if password_storage[username] != password:
        return {'ok': False}

    messages.append({'username': username, 'time': time.time(), 'text': text})

    return {'ok': True}


@app.route("/messages")
def messagesm():
    '''
    Param after - отметка времени после которой сообщения будут в резул
    :return:
    '''
    after = float(request.args['after'])
    filtred_messages = [message for message in messages if
                        message['time'] > after]
    return {'messages': filtred_messages}

# Don't touch it!

app.run()
