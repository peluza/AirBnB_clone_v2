#!/usr/bin/python3
"""starts a Flask web application:
        must be listening on 0.0.0.0, port 5000
    """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def varpage(text):
    var = str(text).replace("_", " ")
    return "C " + var


@app.route("/python", strict_slashes=False, defaults={'text': "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def varpagepy(text):
    var = str(text).replace("_", " ")
    return "Python " + var


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)