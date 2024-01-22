from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL ("/") with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
     """This route displays 'Hello HBNB!' when accessed."""
    return 'Hello HBNB!'

# Run the application on 0.0.0.0 (accessible from any network interface) and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)