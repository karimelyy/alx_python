"""
3-python_route.py - Flask Web Application with Four Routes

This script creates a Flask web application with four routes:
1. Root URL ("/"): Displays "Hello HBNB!"
2. "/hbnb": Displays "HBNB"
3. "/c/<text>": Displays "C " followed by the value of the text variable
   (replace underscore _ symbols with a space).
4. "/python/<text>": Displays "Python " followed by the value of the text variable
   (replace underscore _ symbols with a space). The default value of text is "is cool".

Usage:
    Run the script using 'python3 3-python_route.py'. The web application will
    be accessible on http://0.0.0.0:5000/.

Routes:
    - /: Displays the message "Hello HBNB!"
    - /hbnb: Displays the message "HBNB"
    - /c/<text>: Displays "C " followed by the value of the text variable.
    - /python/<text>: Displays "Python " followed by the value of the text variable.

Dependencies:
    - Flask: The web framework used for creating the application.

"""

from flask import Flask, escape

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL ("/") with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays a greeting message when the root URL is accessed.

    Returns:
        str: The greeting message "Hello HBNB!".
    """
    return 'Hello HBNB!'

# Define a route for the "/hbnb" URL with strict_slashes=False
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays a message when the "/hbnb" URL is accessed.

    Returns:
        str: The message "HBNB".
    """
    return 'HBNB'

# Define a route for the "/c/<text>" URL with strict_slashes=False
@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Displays "C " followed by the value of the text variable.

    Args:
        text (str): The value of the text variable.

    Returns:
        str: The message "C " followed by the value of the text variable.
    """
    return 'C {}'.format(escape(text.replace('_', ' ')))

# Define a route for the "/python/<text>" URL with strict_slashes=False
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Displays "Python " followed by the value of the text variable.

    Args:
        text (str): The value of the text variable.

    Returns:
        str: The message "Python " followed by the value of the text variable.
    """
    return 'Python {}'.format(escape(text.replace('_', ' ')))

# Run the application on 0.0.0.0 (accessible from any network interface) and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)