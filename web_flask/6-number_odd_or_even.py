#!/usr/bin/python3
"""starts a Flask web application:
        must be listening on 0.0.0.0, port 5000
    """

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """index

    Returns:
        str: 'Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb

    Returns:
        str: HBNB
    """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def varpage(text):
    """vatpage

    Args:
        text (str): name for the page

    Returns:
        str: name for the page
    """
    var = str(text).replace("_", " ")
    return "C " + var


@app.route("/python", strict_slashes=False, defaults={'text': "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def varpagepy(text):
    """varpagepy

    Args:
        text (str): name for the page

    Returns:
        str: name for the page
    """
    var = str(text).replace("_", " ")
    return "Python " + var


@app.route("/number/<int:n>", strict_slashes=False)
def varpagenum(n):
    """varpagenum

    Args:
        n (int): this is number

    Returns:
        str : n is a number
    """
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numpage(n):
    """numpage

    Args:
        n (int): this is number

    Returns:
        html: print the number
    """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def evenorodd(n):
    """evenorodd

    Args:
        n (int): this is number

    Returns:
        html: print the number is ever or odd
    """
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
