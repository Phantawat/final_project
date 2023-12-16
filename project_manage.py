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
    if login_search:
        print('Welcome to Senior project managing program')
        print("Login for letting me know who you are :D")
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


def view_project_details():
    print("Faculty: Seeing details of all projects")
    my_db = initializing()
    project_table = my_db.search('Project_table')
    print(project_table)


class Student:
    def __init__(self, val):
        self.student_id = val[0]
        self.role = val[2]
        self.name = val[1]
        self.firstname = self.name['first']
        self.lastname = self.name['last']
        self.projects = []

    def student_home(self):
        print(f'Welcome, {self.role} (Student ID: {self.student_id}, Name: {self.firstname + " " + self.lastname})')
        if self.role == 'lead':
            LeadStudent.lead_menu(LeadStudent)
        elif self.role == 'member':
            self.member_menu()
        elif self.role == 'student':
            print("You're not in any projects.")
            print('Student Menu:')
            print('1. Create project')
            print('2. Respond to an invitation')
            choice = input('Enter your choice: ')
            my_db = initializing()
            person_table = my_db.search('persons')
            print(person_table)
            while True:
                if choice == '1':
                    person_table.update(self.student_id, 'role', 'lead')
                    LeadStudent.create_project(LeadStudent)
                    break
                elif choice == '2':
                    self.respond_to_invitation()
                    break
                print('Please try again.')
                choice = input('Enter your choice: ')

    def member_menu(self):
        print('Member Menu:')
        view_project_details()

    def respond_to_invitation(self):
        pass


class LeadStudent(Student):
    def __init__(self, val):
        super().__init__(val)
        self.project_table = ProjectTable()

    def lead_menu(self):
        print('Lead Menu:')
        print('1. Create Project')
        print('2. Find Members')
        print('3. Invite Members')
        print('4. Add Members to Project')
        print('5. View and Modify Project Details')
        print('6. Send Request to Advisors')
        print('7. Submit Final Project Report')
        choice = input('Enter your choice: ')
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
                view_project_details()
                break
            elif choice == '6':
                self.send_request_to_advisors()
                break
            elif choice == '7':
                self.submit_final_project_report()
                break
            print('Please try again.')
            choice = input('Enter your choice: ')

    def invite_members(self):
        print("Lead: Inviting members and forming a group")

    def send_request_to_advisors(self):
        print("Lead: Sending request to advisors")

    def create_project(self):
        title = input("Enter project title: ")
        self.project_table.add_project(title, self.student_id, '', '', '', '', '')
        print("Lead: Project created successfully.")

    def find_members(self):
        print("Lead: Finding members")

    def add_members(self):
        print("Lead: Adding members to the project")

    def submit_final_project_report(self):
        print("Lead: Submitting final project report")


class MemberStudent(Student):
    def __init__(self, val):
        super().__init__(val)


class Faculty:
    def __init__(self, val):
        self.faculty_id = val[0]
        self.role = val[2]
        self.name = val[1]
        self.projects = []
        self.project_table = ProjectTable()

    def faculty_home(self):
        print(f'Welcome, {self.role} (Faculty ID: {self.faculty_id}, Name: {self.name})')
        if self.role == 'faculty':
            self.normal_faculty_menu()
        elif self.role == 'advisor':
            self.advisor_menu()

    def normal_faculty_menu(self):
        print('Normal Faculty Menu:')
        print('1. See Requests to Be a Supervisor')
        print('2. Send Deny Response')
        print('3. See Details of All Projects')
        print('4. Evaluate Projects')
        choice = input('Enter your choice: ')
        while True:
            if choice == '1':
                self.see_supervisor_requests()
                break
            elif choice == '2':
                self.send_response()
                break
            elif choice == '3':
                view_project_details()
                break
            elif choice == '4':
                self.evaluate_projects(self.project_table.table_name)
                break
            print('Please try again.')
            choice = input('Enter your choice: ')

    def advisor_menu(self):
        print('Advisor Menu:')
        print('1. See Requests to Be a Supervisor')
        print('2. Send Response')
        print('3. See Details of All Projects')
        print('4. Evaluate Projects')
        print('5. Approve Project')
        choice = input('Enter your choice: ')
        while True:
            if choice == '1':
                self.see_supervisor_requests()
                break
            elif choice == '2':
                self.send_response()
                break
            elif choice == '3':
                view_project_details()
                break
            elif choice == '4':
                self.evaluate_projects(self.project_table.table_name)
                break
            elif choice == '5':
                self.approve_project()
                break
            print('Please try again.')
            choice = input('Enter your choice: ')

    def see_supervisor_requests(self):
        print("Faculty: Seeing requests to be a supervisor")

    def send_response(self):
        print("Advisor: Sending accept response")

    def evaluate_projects(self, project_id):
        project = self.project_table.search('projects', project_id)
        if project:
            print(f"Project Details:\n{project}")
            evaluation = input("Provide your evaluation comments: ")
            print(f"Project status set to 'Evaluating'.")
            self.project_table.update_status(project_id, 'Evaluating')
            approval = input("Do you approve the project? (yes/no): ").lower()
            if approval == 'yes':
                print("Project approved.")
                self.project_table.update_status(project_id, 'Approved')
            else:
                print("Project not approved.")
                self.project_table.update_status(project_id, 'Not Approved')
        else:
            print("Project not found.")

    def approve_project(self):
        print("Advisor: Approving project")


class Admin:
    def __init__(self, my_db):
        self.my_db = my_db

    def admin_home(self):
        print('Welcome back, Admin Menu:')
        print('1. Update Database')
        print('2. Manage User')
        choice = input('Enter what you are going to do: ')
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
            print('Please try again.')
            choice = input("Enter what you're going to do: ")

    def update_database(self):
        # Logic to update user information in the database
        pass

    def manage_user(self):
        # Logic to perform other database management tasks
        pass


class ProjectTable(Table):
    def __init__(self):
        super().__init__('projects', [])

    def add_project(self, title, lead, member1, member2, member3, member4, advisor):
        project = {
            'ProjectID': len(self.table) + 1,
            'Title': title,
            'Lead': lead,
            'Member1': member1,
            'Member2': member2,
            'Member3': member3,
            'Member4': member4,
            'Advisor': advisor,
            'Status': 'Pending'
        }
        self.table.append(project)


class MemberPendingRequestTable(Table):
    def __init__(self):
        super().__init__('member_pending_request', [])

    def add_request(self, project_id, to_be_member):
        request = {
            'ProjectID': project_id,
            'to_be_member': to_be_member,
            'Response': None,
            'Response_date': None
        }
        self.table.append(request)

    def update_response(self, project_id, to_be_member, response, response_date):
        for request in self.table:
            if request['ProjectID'] == project_id and request['to_be_member'] == to_be_member:
                request['Response'] = response
                request['Response_date'] = response_date
                break


class AdvisorPendingRequestTable(Table):
    def __init__(self):
        super().__init__('advisor_pending_request', [])

    def add_request(self, project_id, to_be_advisor):
        request = {
            'ProjectID': project_id,
            'to_be_advisor': to_be_advisor,
            'Response': None,
            'Response_date': None
        }
        self.table.append(request)

    def update_response(self, project_id, to_be_advisor, response, response_date):
        for request in self.table:
            if request['ProjectID'] == project_id and request['to_be_advisor'] == to_be_advisor:
                request['Response'] = response
                request['Response_date'] = response_date
                break


my_db = initializing()
val = login()
student = Student(val)
admin = Admin(my_db)
faculty = Faculty(val)

if val[2] == 'admin':
    admin.admin_home()
elif val[2] == 'student' or val[2] == 'member' or val[2] == 'lead':
    student.student_home()
elif val[2] == 'faculty' or val[2] == 'advisor':
    faculty.faculty_home()

exit()
