import sys
import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    user_url = f"{base_url}/users/{employee_id}"

    # Retrieve employee information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Failed to retrieve employee information.")
        return

    user_data = user_response.json()
    employee_name = user_data["name"]

    # Retrieve employee TODO list
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Failed to retrieve TODO list.")
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    done_tasks = [todo for todo in todos_data if todo["completed"]]
    num_done_tasks = len(done_tasks)

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print("\t", task["title"])


# Check if the employee ID is provided as a command-line argument
if len(sys.argv) != 2:
    print("Please provide the employee ID as a command-line argument.")
else:
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")

