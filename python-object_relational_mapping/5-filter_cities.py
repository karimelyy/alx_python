"""Script to list all cities of a specific state from the database hbtn_0e_4_usa"""

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

    # Execute the parameterized query to retrieve cities of the specified state
    query = """
            SELECT name
            FROM cities
            WHERE state_id = (SELECT id FROM states WHERE name = %s)
            ORDER BY id ASC
            """
    cursor.execute(query, (state_name,))

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the results
    if rows:
        result = ', '.join(city[0] for city in rows)
        print(result)
    else:
        print()

    # Close cursor and database connection
    cursor.close()
    db.close()