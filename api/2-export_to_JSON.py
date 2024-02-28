import json
import requests
import sys

def export_employee_tasks(employee_id):
    # Fetching employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    if response.status_code != 200:
        print("Employee not found.")
        return
    employee_data = response.json()
    user_id = employee_data['id']
    username = employee_data['username']

    # Fetching employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(todos_url)
    todos_data = response.json()

    # Creating data dictionary
    data_dict = {str(user_id): []}
    for task in todos_data:
        task_dict = {"task": task['title'], "completed": task['completed'], "username": username}
        data_dict[str(user_id)].append(task_dict)

    # Writing data to JSON file
    with open(f"{user_id}.json", mode='w') as file:
        json.dump(data_dict, file)

    print(f"Data exported to {user_id}.json")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    export_employee_tasks(employee_id)
