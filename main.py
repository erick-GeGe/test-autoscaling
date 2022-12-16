from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    x = 1
    for i in range(1000000):
        x += x**(1/2)
    return 'OK'

if __name__ == '__main__':
	app.run(port=80)
