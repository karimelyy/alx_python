import requests
import sys

def get_employee_info(employee_id):
    # Fetching employee details
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetching TODO list for the employee
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todos_data = todos_response.json()

    # Calculating completed tasks
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    # Printing employee progress
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py [employee_id]")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)