# Python Technical Test of Thryvtechlabs.com
## Project Setup 
for project setup perform the following steps,
1. Create a Python virtual environment.
2. Clone the project by executing the following command:
   ```bash
   git clone https://github.com/urbuddy/Simple-Admin-dashboard.git
   ```
3. Install the requirements:
```bash
pip install -r requirements.txt
```
4.1. The following two files are the solutions to Questions 1 and 2 respectively,

  i. Que1Sol.py  
  ii. Que2Sol.py  

command to execute the file:  
  ```bash
  python {file_name.py}
  ```
4.2. For the 3rd question solution you have to see the project todo_app and set it up as follows to see the result.  
  i. Migrate the Model Changes into DB
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
  ii. Create a super user(admin)
  ```bash
  python manage.py createsuperuser
  ```
  iii. run server
  ```bash
  python manage.py runserver
  ```
  iii. Endpoints to test
  
  For User Login(POST Request)
  ```bash
  http://127.0.0.1:8000/login/
  ```

  For Employers
  1. Add Employee(POST Request)
  ```bash
  http://127.0.0.1:8000/employees/add
  ```
  2. Edit Employee(PATCH Request)
  ```bash
  http://127.0.0.1:8000/employees/<int:employee_id>/edit/
  ```
  3. View Employees(GET Request)
  ```bash
  http://127.0.0.1:8000/employees/
  ```
  4. Delete Employee(DELETE Request)
  ```bash
  http://127.0.0.1:8000/employees/<int:employee_id>/delete/
  ```
  5. Add Task(POST Request)
  ```bash
  http://127.0.0.1:8000/tasks/add/
  ```
  6. Edit Task(PUT Request)
  ```bash
  http://127.0.0.1:8000/tasks/<int:task_id>/edit/
  ```
  7. View Tasks(GET Request)
  ```bash
  http://127.0.0.1:8000/tasks/
  ```
  8. Delete Employee(Delete Request)
  ```bash
  http://127.0.0.1:8000/tasks/<int:task_id>/delete/
  ```

  For Employee
  1. View their Tasks(GET Request)
  ```bash
  http://127.0.0.1:8000/tasks/employee/
  ```
  2. Update the status of the task(PATCH Request)
  ```bash
  http://127.0.0.1:8000/tasks/<int:task_id>/status/
  ```
Note: To Test all those endpoints, you must first create an employer from the admin panel using superuser credentials.
First login with the employer or employee and you receive a token to access all the APIs


