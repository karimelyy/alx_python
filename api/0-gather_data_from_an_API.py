import sys
import requests

def get_employee_data(employee_id):
    # Fetch employee details
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch TODO list for the employee
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_list = todo_response.json()

    # Calculate completed tasks
    completed_tasks = [task for task in todo_list if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_list)

    return employee_name, num_completed_tasks, total_tasks, completed_tasks

def display_progress(employee_name, num_completed_tasks, total_tasks, completed_tasks):
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_name, num_completed_tasks, total_tasks, completed_tasks = get_employee_data(employee_id)
        display_progress(employee_name, num_completed_tasks, total_tasks, completed_tasks)
    except ValueError:
        print("Please provide a valid integer as the employee ID.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")