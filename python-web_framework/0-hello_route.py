"""
0-hello_route.py - Simple Flask Web Application

This script creates a basic Flask web application with a single route that
displays "Hello HBNB!" when the root URL is accessed.

Usage:
    Run the script using 'python3 0-hello_route.py'. The web application will
    be accessible on http://0.0.0.0:5000/.

Routes:
    - /: Displays the message "Hello HBNB!"

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

# Run the application on 0.0.0.0 (accessible from any network interface) and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)