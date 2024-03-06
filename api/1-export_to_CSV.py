#!/usr/bin/python3
import csv
import requests
import sys

# Get user ID from command line argument and convert to string
user_id = str(sys.argv[1])

# Construct URLs to retrieve user and todo data
request_user = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
request_todos = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)

# Fetch user and todo data from the JSONPlaceholder API
data_user = requests.get(request_user).json()
data_todos = requests.get(request_todos).json()

# Define filename for the CSV file based on the user ID
filename = f"{user_id}.csv"

# Open the CSV file in write mode and create a CSV writer object
with open(filename, "w", newline="") as file:
    csvwriter = csv.writer(file, quoting=csv.QUOTE_ALL)
    
    # Iterate over todo data and write each task to the CSV file
    for task in data_todos:
        # Write task details to the CSV file
        csvwriter.writerow(
            [user_id, str(data_user["username"]), task["completed"], task["title"]]
        )