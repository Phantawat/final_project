# # BEGIN part 1
#
# # import database module
from database import ReadCSV, DB, Table
import csv

# define a funcion called initializing

def initializing():
    my_db = DB()
    project_key = ['ProjectID',	'Title', 'Lead', 'Member1',	'Member2', 'Member3', 'Member4', 'Advisor', 'Status']
    exit(project_key, 'Project_table.csv')
    read_persons = ReadCSV('persons.csv')
    read_login = ReadCSV('login.csv')
    persons = read_persons.read_csv()
    login = read_login.read_csv()
    persons_table = Table('persons', persons)
    login_table = Table('login', login)
    my_db.insert(persons_table)
    my_db.insert(login_table)
    project = []
    project_table = Table('projects', project)
    my_db.insert(project_table)
    return my_db



# define a funcion called login

def login():
    my_db = initializing()
    login_search = my_db.search('login')
    print(login_search)

    if login_search:
        username = input('Username: ')
        password = input('Password: ')
        while True:
            for i in login_search.table:
                if i['username'] == username and i['password'] == password:
                    personal_id = i.get('person_id', '')
                    role = i.get('role', '')
                    return [personal_id, role]
            print('Login failed. Username or password is incorrect.')
            username = input('Username: ')
            password = input('Password: ')
    else:
        print('Error: Login table not found.')
        return None


# define a function called exit
def exit(project_key, project_name):
    myFile = open(project_name, 'w')
    writer = csv.writer(myFile)
    writer.writerow(project_key)
    myFile.close()
    myFile = open(project_name, 'r')
    myFile.close()


class Student:
    def __init__(self, val):
        self.student_id = val[0]
        self.role = val[1]
        self.projects = []

    def student_home(self):
        print(f"Welcome, (Student ID: {self.student_id})")
        print("1. Project Status")
        print("2. Create Project")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.project_status()
        elif choice == '2':
            self.create_project()
        else:
            print("Invalid choice. Please try again.")

    def project_status(self):
        print("Project Status:")
        for project in self.projects:
            print(f"Project ID: {project['project_id']}, Status: {project['status']}")

    def create_project(self):
        project_title = input("Enter the project title: ")
        project_id = len(self.projects) + 1
        project_key = ['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Member3', 'Member4', 'Advisor', 'Status']
        new_project = {key: '' for key in project_key}
        new_project['ProjectID'] = project_id
        new_project['Title'] = project_title
        new_project['Lead'] = self.student_id
        self.projects.append(new_project)
        print(f"Project '{project_title}' created successfully.")

    def accept_invite(self, project):
        # Waiting for implement
        print(f"Invitation accepted! You are now a member of the project '{project['Title']}'.")

    def deny_invite(self, project):
        # Waiting for implement
        print(f"Invitation denied. You are not a member of the project '{project['Title']}'.")

    def invite_member(self):
        my_db = DB()
        project_id = input("Enter the project ID: ")
        project = next((proj for proj in self.projects if proj['ProjectID'] == project_id), None)
        if project:
            member_name = input("Enter the member's name: ")
            invitation = f"You have been invited to join the project '{project['Title']}'"
            print(f"Invitation sent to {member_name}: {invitation}")
            project_table = my_db.search('projects')
            for key in ['Member1', 'Member2', 'Member3', 'Member4']:
                if not project[key]:
                    project_table.update(str(project_id), key, member_name)
                    break
            print(f"{member_name} added to the project '{project['Title']}' as a member.")
            response = input("Do you want to accept the invitation? (yes/no): ").lower()
            if response == 'yes':
                self.accept_invite(project)
            else:
                self.deny_invite(project)
        else:
            print("Project not found. Please enter a valid project ID.")


# class Faculty:
#     def __init__(self):
#         pass
#
#     # Waiting for implement
#
#
# class Admin:


# make calls to the initializing and login functions defined above

initializing()
val = login()

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
# elif val[1] = 'student':
#     Student.student_home(self)
# elif val[1] = 'member':
# see and do member related activities
# elif val[1] = 'lead':
# see and do lead related activities
# elif val[1] = 'faculty':
# see and do faculty related activities
# elif val[1] = 'advisor':
# see and do advisor related activities

# once everything is done, make a call to the exit function
# exit()
