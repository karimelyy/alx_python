"""
1-hbnb_route.py - Flask Web Application with Two Routes

This script creates a Flask web application with two routes:
1. Root URL ("/"): Displays "Hello HBNB!"
2. "/hbnb": Displays "HBNB"

Usage:
    Run the script using 'python3 1-hbnb_route.py'. The web application will
    be accessible on http://0.0.0.0:5000/.

Routes:
    - /: Displays the message "Hello HBNB!"
    - /hbnb: Displays the message "HBNB"

Dependencies:
    - Flask: The web framework used for creating the application.

"""

from flask import Flask

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

# Run the application on 0.0.0.0 (accessible from any network interface) and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)