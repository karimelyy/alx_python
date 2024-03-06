import requests
import sys

# Get the employee ID from command line arguments
id = sys.argv[1]

# Make a GET request to retrieve employee information
request_user = requests.get('https://jsonplaceholder.typicode.com/users/'+employee_id)
request_todos = requests.get('https://jsonplaceholder.typicode.com/users/'+employee_id+'/todos')

# Parse the JSON response
data_user = request_user.json()
data_todos = request_todos.json()

# Initialize a counter for completed tasks
completed = 0

# Iterate through the tasks to count completed ones
for i in data_todos:
    if i.get('completed'):
        completed += 1

# Print the employee's name and the number of completed tasks
print ('Employee "{}" has completed tasks ({}/{}) :'.format(data_user.get('name'), completed, len(data_todos)))

# Print the titles of completed tasks
for item in data_todos:
    if item.get('completed'):
        print('\t - ' + item.get('title'))