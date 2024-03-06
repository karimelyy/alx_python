"""
This script retrieves employee todo data and saves it in JSON format.
"""

import json
import requests
import sys


def save_todo_progress_to_json(employee_id):
    """
    Fetches employee data and stores todo progress in JSON format.
    
    Parameters:
        employee_id (int): The ID of the employee.
    """
    # Construct URL for employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # Fetch employee details
    user_response = requests.get(user_url)

    # Check if the employee exists
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    # Parse response to obtain employee data
    user_data = user_response.json()
    username = user_data["username"]

    # URL for employee's tasks
    tasks_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch employee's tasks
    tasks_response = requests.get(tasks_url)

    # Check if the tasks were fetched successfully
    if tasks_response.status_code != 200:
        print(f"Unable to fetch TODO list for employee with ID {employee_id}.")
        return

    # Parse tasks data
    tasks_data = tasks_response.json()

    # Create JSON data
    json_data = {
        str(employee_id): [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": username,
            }
            for todo in tasks_data
        ]
    }

    # Create a JSON file
    json_filename = f"{employee_id}.json"
    with open(json_filename, "w") as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == "__main__":
    # Get the employee ID from command-line argument
    employee_id = int(sys.argv[1])

    # Call the function to export all data to a JSON file
    save_todo_progress_to_json(employee_id)