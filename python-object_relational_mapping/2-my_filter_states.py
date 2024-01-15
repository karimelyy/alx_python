"""Script to filter states by name from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username, password, database, state_name = sys.argv[1:]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Fetch all rows
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    # Filter rows by case-insensitive comparison in Python
    filtered_rows = [(id, name) for id, name in rows if name.lower() == state_name.lower()]

    # Display the filtered results
    for row in filtered_rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()