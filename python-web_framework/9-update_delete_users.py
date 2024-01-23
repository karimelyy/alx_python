from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Replace with a secret key for flash messages

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables

# Root route
@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

# Add User route
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')

            # Validate the data
            if not name or not email:
                flash("Name and email are required fields.", 'error')
                return render_template('add_user.html')

            # Insert the new user into the User table
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()

            # Flash success message
            flash("User added successfully!", 'success')
            return redirect(url_for('users'))
        except Exception as e:
            # Handle exceptions and flash an error message
            flash(f"Error adding user: {str(e)}", 'error')

    # Render the add_user.html template for GET requests
    return render_template('add_user.html')

# Users route
@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

# Update a User
@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        try:
            # Extract updated name and email from the form data
            updated_name = request.form.get('name')
            updated_email = request.form.get('email')

            # Validate the data
            if not updated_name or not updated_email:
                flash("Name and email are required fields.", 'error')
                return render_template('update_user.html', user=user)

            # Update the user in the User table
            user.name = updated_name
            user.email = updated_email
            db.session.commit()

            # Flash success message
            flash("User updated successfully!", 'success')
            return redirect(url_for('users'))
        except Exception as e:
            # Handle exceptions and flash an error message
            flash(f"Error updating user: {str(e)}", 'error')

    # Render the update_user.html template for GET requests
    return render_template('update_user.html', user=user)

# Delete a User
@app.route('/delete_user/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        try:
            # Delete the user from the User table
            db.session.delete(user)
            db.session.commit()

            # Flash success message
            flash("User deleted successfully!", 'success')
            return redirect(url_for('users'))
        except Exception as e:
            # Handle exceptions and flash an error message
            flash(f"Error deleting user: {str(e)}", 'error')

    # Render the delete_user.html template for GET requests
    return render_template('delete_user.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)