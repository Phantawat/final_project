# # BEGIN part 1
#
# # import database module
from database import ReadCSV, DB, Table
import csv

# define a funcion called initializing

def initializing():
    my_db = DB()
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


def login():
    my_db = initializing()
    login_search = my_db.search('login')
    person_search = my_db.search('persons')
    print(login_search)
    if login_search:
        username = input('Username: ')
        password = input('Password: ')
        while True:
            for i in login_search.table:
                if i['username'] == username and i['password'] == password:
                    personal_id = i.get('ID', '')
                    role = i.get('role', '')
                    name = person_search.filter(lambda x: x['ID'] == personal_id).select(['first', 'last'])[0]
                    return [personal_id, name, role]
            print('Login failed. Username or password is incorrect.')
            username = input('Username: ')
            password = input('Password: ')
    else:
        print('Error: Login table not found.')
        return None


# define a function called exit
def exit():
    project_key = ['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Member3', 'Member4', 'Advisor', 'Status']
    myFile = open('Project_table.csv', 'w')
    writer = csv.writer(myFile)
    writer.writerow(project_key)
    myFile.close()
    myFile = open('Project_table.csv', 'r')
    myFile.close()


class Student:
    def __init__(self, val):
        self.student_id = val[0]
        self.role = val[2]
        self.name = val[1]
        self.projects = []

    def student_home(self):
        print(f"Welcome, {self.role} (Student ID: {self.student_id}, Name: {self.name})")
        if self.role == 'lead':
            self.lead_menu()
        elif self.role == 'member':
            self.member_menu()

    def lead_menu(self):
        print("Lead Menu:")
        print("1. Create Project")
        print("2. Find Members")
        print("3. Invite Members")
        print("4. Add Members to Project")
        print("5. View and Modify Project Details")
        print("6. Send Request to Advisors")
        print("7. Submit Final Project Report")
        choice = input("Enter your choice: ")
        while True:
            if choice == '1':
                self.create_project()
                break
            elif choice == '2':
                self.find_members()
                break
            elif choice == '3':
                self.invite_members()
                break
            elif choice == '4':
                self.add_members()
                break
            elif choice == '5':
                self.view_project_details()
                break
            elif choice == '6':
                self.send_request_to_advisors()
                break
            elif choice == '7':
                self.submit_final_project_report()
                break
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")

    def member_menu(self):
        print("Member Menu:")
        self.view_project_details()

    def create_project(self):
        print("Lead: Creating a project")

    def find_members(self):
        print("Lead: Finding members")

    def invite_members(self):
        print("Lead: Inviting members")

    def add_members(self):
        print("Lead: Adding members to the project")

    def view_project_details(self):
        print("Viewing and modifying project details")

    def send_request_to_advisors(self):
        print("Lead: Sending request to advisors")

    def submit_final_project_report(self):
        print("Lead: Submitting final project report")


class LeadStudent(Student):
    def __init__(self, val):
        super().__init__(val)

    def lead_menu(self):
        print("Lead Menu:")
        print("1. Create Project")
        print("2. Find Members")
        print("3. Invite Members")
        print("4. Add Members to Project")
        print("5. View and Modify Project Details")
        print("6. Send Request to Advisors")
        print("7. Submit Final Project Report")
        choice = input("Enter your choice: ")
        while True:
            if choice == '1':
                self.create_project()
                break
            elif choice == '2':
                self.find_members()
                break
            elif choice == '3':
                self.invite_members()
                break
            elif choice == '4':
                self.add_members()
                break
            elif choice == '5':
                self.view_project_details()
                break
            elif choice == '6':
                self.send_request_to_advisors()
                break
            elif choice == '7':
                self.submit_final_project_report()
                break
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")

    def invite_members(self):
        print("Lead: Inviting members and forming a group")


class MemberStudent(Student):
    def __init__(self, val):
        super().__init__(val)

class Faculty:
    def __init__(self, val):
        self.faculty_id = val[0]
        self.role = val[2]
        self.name = val[1]
        self.projects = []

    def faculty_home(self):
        print(f"Welcome, {self.role} (Faculty ID: {self.faculty_id}, Name: {self.name})")
        if self.role == 'faculty':
            self.normal_faculty_menu()
        elif self.role == 'advisor':
            self.advisor_menu()

    def normal_faculty_menu(self):
        print("Normal Faculty Menu:")
        print("1. See Requests to Be a Supervisor")
        print("2. Send Deny Response")
        print("3. See Details of All Projects")
        print("4. Evaluate Projects")
        choice = input("Enter your choice: ")
        while True:
            if choice == '1':
                self.see_supervisor_requests()
                break
            elif choice == '2':
                self.send_response()
                break
            elif choice == '3':
                self.see_project_details()
                break
            elif choice == '4':
                self.evaluate_projects()
                break
            print("Please try again.")
            choice = input("Enter your choice: ")

    def advisor_menu(self):
        print("Advisor Menu:")
        print("1. See Requests to Be a Supervisor")
        print("2. Send Response")
        print("3. See Details of All Projects")
        print("4. Evaluate Projects")
        print("5. Approve Project")
        choice = input("Enter your choice: ")
        while True:
            if choice == '1':
                self.see_supervisor_requests()
                break
            elif choice == '2':
                self.send_response()
                break
            elif choice == '3':
                self.see_project_details()
                break
            elif choice == '4':
                self.evaluate_projects()
                break
            elif choice == '5':
                self.approve_project()
                break
            print("Please try again.")
            choice = input("Enter your choice: ")


    def see_supervisor_requests(self):
        print("Faculty: Seeing requests to be a supervisor")

    def send_response(self):
        print("Advisor: Sending accept response")

    def see_project_details(self):
        print("Faculty: Seeing details of all projects")

    def evaluate_projects(self):
        print("Faculty: Evaluating projects")

    def approve_project(self):
        print("Advisor: Approving project")

class Admin:
    def __init__(self, my_db):
        self.my_db = my_db

    def admin_home(self):
        print("Admin Menu:")
        print("1. Update Database")
        print("2. Manage User")
        choice = input("Enter what you are going to do: ")
        while True:
            if choice == '1':
                self.update_database()
                break
            elif choice == '2':
                self.update_database()
                break
            elif choice == '3':
                self.manage_user()
                break
            print("Invalid choice. Please try again.")
            choice = input("Enter what you are going to do: ")

    def update_database(self):
        # Logic to update user information in the database
        pass

    def manage_user(self):
        # Logic to perform other database management tasks
        pass




# make calls to the initializing and login functions defined above

initializing()
val = login()
student = Student(val)
admin = Admin()
faculty = Faculty(val)

if val[2] == 'admin':
    admin.admin_home()
elif val[2] == 'student':
    student.student_home()
elif val[2] == 'member':
    student.student_home()
elif val[2] =='lead':
    student.student_home()
elif val[2] == 'faculty':
    faculty.faculty_home()
elif val[2] == 'advisor':
    faculty.faculty_home()

# once everything is done, make a call to the exit function
# exit()
