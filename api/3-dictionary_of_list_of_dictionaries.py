#!/usr/bin/python3
"""
Fetches user and todo information from JSONPlaceholder API and exports to JSON.
"""

from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    # URL for retrieving user information
    user_url = "https://jsonplaceholder.typicode.com/users"
    
    # Fetch user data
    user_output = get(user_url).json()

    # Initialize dictionary to store all user data
    main_data = {}
    
    # Iterate through each user to retrieve their todo tasks
    for user in user_output:
        tasks = []

        # URL for retrieving user-specific tasks
        tasks_url = f"https://jsonplaceholder.typicode.com/users/{user.get('id')}/todos"
        
        # Fetch tasks for the current user
        tasks_output = get(tasks_url).json()

        # Iterate through each task to extract relevant information
        for todo in tasks_output:
            tasks_dict = {}
            tasks_dict.update(
                {
                    "username": user.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                }
            )
            tasks.append(tasks_dict)

        # Store user tasks in the main data dictionary
        main_data.update({user.get("id"): tasks})

    # Export all user tasks to a JSON file
    with open("todo_all_employees.json", "w") as f:
        dump(main_data, f)