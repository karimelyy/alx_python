#!/usr/bin/python3
import csv
import requests
import sys

# Extract user ID from command line argument
user_id = str(sys.argv[1])

# Formulate URLs to request user and todo data
request_user = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
request_todos = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)

# Retrieve user and todo data from JSONPlaceholder API
data_user = requests.get(request_user).json()
data_todos = requests.get(request_todos).json()

# Generate filename for CSV based on user ID
filename = f"{user_id}.csv"

# Write user and todo data to a CSV file
with open(filename, "w", newline="") as file:
    csvwriter = csv.writer(file, quoting=csv.QUOTE_ALL)
    
    # Write header row to CSV file
    csvwriter.writerow(["User ID", "Username", "Task Completed", "Task Title"])
    
    # Iterate over todo data and write each task to the CSV file
    for task in data_todos:
        csvwriter.writerow(
            [user_id, str(data_user["username"]), task["completed"], task["title"]]
        )