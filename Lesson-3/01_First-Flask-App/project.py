from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"

@app.route('/hi')
def Hi():
    return "Hi everyone"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
