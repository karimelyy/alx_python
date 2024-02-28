"""
This script fetches the TODO list of a specific employee from the JSONPlaceholder API
and exports the data to a JSON file.

Usage: python script_name.py <employee_id>
"""

import json
import requests
import sys

def export_employee_tasks(employee_id):
    """
    Fetches the TODO list of a specific employee from the JSONPlaceholder API
    and exports the data to a JSON file.

    Args:
        employee_id (int): The ID of the employee whose tasks are to be exported.

    Returns:
        None
    """
    # Constructing the URL to fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # Sending a GET request to fetch employee details
    response = requests.get(employee_url)

    # Checking if the request was successful
    if response.status_code != 200:
        print("Employee not found.")
        return

    # Parsing the JSON response to get employee data
    employee_data = response.json()
    user_id = employee_data['id']
    username = employee_data['username']

    # Constructing the URL to fetch employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Sending a GET request to fetch employee's TODO list
    response = requests.get(todos_url)

    # Parsing the JSON response to get TODO list data
    todos_data = response.json()

    # Creating a dictionary to store the TODO list data
    data_dict = {str(user_id): []}

    # Iterating over each task in the TODO list
    for task in todos_data:
        # Creating a dictionary for each task
        task_dict = {"task": task['title'], "completed": task['completed'], "username": username}
        # Appending the task dictionary to the list under the user ID key
        data_dict[str(user_id)].append(task_dict)

    # Writing the data to a JSON file
    with open(f"{user_id}.json", mode='w') as file:
        json.dump(data_dict, file)

    print(f"Data exported to {user_id}.json")

if __name__ == "__main__":
    # Checking if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)
    
    # Extracting the employee ID from command-line arguments
    employee_id = sys.argv[1]
    
    # Calling the function to export employee tasks
    export_employee_tasks(employee_id)
