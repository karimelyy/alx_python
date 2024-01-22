"""
6-number_odd_or_even.py - Flask Web Application with Odd or Even Number Check

This script creates a Flask web application with seven routes:
1. Root URL ("/"): Displays "Hello HBNB!"
2. "/hbnb": Displays "HBNB"
3. "/c/<text>": Displays "C " followed by the value of the text variable
   (replace underscore _ symbols with a space).
4. "/python/<text>": Displays "Python " followed by the value of the text variable
   (replace underscore _ symbols with a space). The default value of text is "is cool".
5. "/number/<n>": Displays "n is a number" only if n is an integer.
6. "/number_template/<n>": Displays an HTML page only if n is an integer.
   The page contains an H1 tag with the text "Number: n" inside the BODY tag.
7. "/number_odd_or_even/<n>": Displays an HTML page only if n is an integer.
   The page contains an H1 tag with the text "Number: n is even|odd" inside the BODY tag.

Usage:
    Run the script using 'python3 6-number_odd_or_even.py'. The web application will
    be accessible on http://0.0.0.0:5000/.

Routes:
    - /: Displays the message "Hello HBNB!"
    - /hbnb: Displays the message "HBNB"
    - /c/<text>: Displays "C " followed by the value of the text variable.
    - /python/<text>: Displays "Python " followed by the value of the text variable.
    - /number/<n>: Displays "n is a number" only if n is an integer.
    - /number_template/<n>: Displays an HTML page only if n is an integer.
    - /number_odd_or_even/<n>: Displays an HTML page with the text "Number: n is even|odd" if n is an integer.

Dependencies:
    - Flask: The web framework used for creating the application.

"""

from flask import Flask, escape, render_template

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

# Define a route for the "/number/<n>" URL with strict_slashes=False
@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Displays "n is a number" only if n is an integer.

    Args:
        n (int): The value of the n variable.

    Returns:
        str: The message "n is a number" if n is an integer.
    """
    return '{} is a number'.format(n)

# Define a route for the "/number_template/<n>" URL with strict_slashes=False
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """
    Displays an HTML page with the text "Number: n" if n is an integer.

    Args:
        n (int): The value of the n variable.

    Returns:
        str: The rendered HTML page with the text "Number: n".
    """
    return render_template('6-number_template.html', number=n)

# Define a route for the "/number_odd_or_even/<n>" URL with strict_slashes=False
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_route(n):
    """
    Displays an HTML page with the text "Number: n is even|odd" if n is an integer.

    Args:
        n (int): The value of the n variable.

    Returns:
        str: The rendered HTML page with the text "Number: n is even|odd".
    """
    return render_template('6-number_odd_or_even.html', number=n)

# Run the application on 0.0.0.0 (accessible from any network interface) and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)