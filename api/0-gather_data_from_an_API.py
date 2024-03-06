import requests
import sys

# Get the employee ID from command line arguments
employee_id = sys.argv[1]

# Make a GET request to retrieve employee information
user_request = requests.get('https://jsonplaceholder.typicode.com/users/'+employee_id)
todos_request = requests.get('https://jsonplaceholder.typicode.com/users/'+employee_id+'/todos')

# Parse the JSON response
user_data = user_request.json()
todos_data = todos_request.json()

# Initialize a counter for completed tasks
tasks_completed = 0

# Iterate through the tasks to count completed ones
for todo in todos_data:
    if todo.get('completed'):
        tasks_completed += 1

# Print the employee's name and the number of completed tasks
print ('Employee "{}" has completed tasks ({}/{}) :'.format(user_data.get('name'), tasks_completed, len(todos_data)))

# Print the titles of completed tasks
for task in todos_data:
    if task.get('completed'):
        print('\t - ' + task.get('title'))