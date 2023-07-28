# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    name = data['name']
    message = data['message']
    print('Received message from', name, ':', message)
    emit('message', {'name': name, 'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
