from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ("/") with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL ("/"). Displays a greeting message.

    Returns:
        str: The greeting message "Hello HBNB!".
    """
    return 'Hello HBNB!'

# Run the Flask application on 0.0.0.0 (accessible from any network interface) and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)