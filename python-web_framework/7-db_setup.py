from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 7-db_setup.py <db_username> <db_password> <db_name>")
    sys.exit(1)

# Retrieve database credentials from command-line arguments
db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

# Initialize a Flask application
app = Flask(__name__)

# Configure Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy extension with the Flask application
db = SQLAlchemy(app)

# Define User Model
class User(db.Model):
    # Define columns for the User model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create Database Tables
def create_tables():
    with app.app_context():
        # Create all defined database tables
        db.create_all()

# Call the function to create tables
create_tables()

# Define a route for the root URL ('/')
@app.route('/', strict_slashes=False)
def index():
    # Return a simple greeting message
    return "Hello, ALX Flask!"

# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)