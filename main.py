from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_url_path='', static_folder='assets/')
wss = SocketIO(app)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login')
def login():
	return render_template('login.html')

if __name__ == '__main__':
	wss.run(app, host='0.0.0.0')