from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

# Retrieve database credentials from command-line arguments
db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

# Initialize Flask application
app = Flask(__name__)

# Configure Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy extension
db = SQLAlchemy(app)

# Define User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create Database Tables
def create_tables():
    with app.app_context():
        db.create_all()

# Call the function to create tables
create_tables()

# Route to handle adding new users
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Handle POST request
        try:
            name = request.form.get('name')  # Corrected line to retrieve form data
            email = request.form.get('email')  # Corrected line to retrieve form data

            # Attempt to insert the new user into the User table
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()

            # Flash success message
            flash("User added successfully!", 'success')
            return redirect(url_for('users'))
        except Exception as e:
            # Handle exceptions (e.g., duplicate email) and flash an error message
            flash(f"Error adding user: {str(e)}", 'error')

    # Render the add_user.html template for GET requests
    return render_template('add_user.html')

# Route to display all users
@app.route('/users')
def users():
    # Connect to the alx_flask_db database and retrieve all users
    all_users = User.query.all()
    
    # Render the results using the users.html template
    return render_template('users.html', users=all_users)

# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)