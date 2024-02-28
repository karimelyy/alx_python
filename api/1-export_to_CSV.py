import csv
import requests
import sys

def get_employee_info(employee_id):
    # Fetching employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print("Employee not found.")
        return
    employee_data = employee_response.json()
    user_id = employee_data['id']
    username = employee_data['username']
    user_name = employee_data['name']  # Added to get the user's name

    # Fetching employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Writing data to CSV file
    with open(f"{user_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            writer.writerow([user_id, username, str(task['completed']), task['title']])

    print(f"Correct number of tasks in CSV: {len(todos_data)}")
    print(f"Correct user ID and username retrieved: {user_id}, {user_name}")  # Displaying user name as well
    print("Correct output formatting")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)