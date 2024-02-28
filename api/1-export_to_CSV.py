import csv
import requests
import sys

def export_employee_tasks(employee_id):
    # Fetching employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    user_id = employee_data['id']
    username = employee_data['username']

    # Fetching employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(todos_url)
    todos_data = response.json()

    # Writing data to CSV file
    with open(f"{user_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            writer.writerow([user_id, username, str(task['completed']), task['title']])

    print(f"Data exported to {user_id}.csv")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    export_employee_tasks(employee_id)
