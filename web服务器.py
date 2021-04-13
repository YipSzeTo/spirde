from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'hello'

@app.route('/nihao')
def index1():
	return 'nihao'

@app.route('/happy')
def index2():
	return 'happy'

if __name__ == '__main__':
	app.run()