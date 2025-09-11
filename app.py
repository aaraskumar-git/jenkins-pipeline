from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
	return "we welcome you all to this project"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=30080)


