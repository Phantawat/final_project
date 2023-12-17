from datetime import datetime
from database import ReadCSV, DB, Table
import csv

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
        username = input('Username: ')
        password = input('Password: ')
        while True:
            for i in login_search.table:
                if i['username'] == username and i['password'] == password:
                    personal_id = i.get('ID', '')
                    role = i.get('type', '')
                    name = person_search.filter(lambda x: x['ID'] == personal_id).select(['first', 'last'])[0]
                    return [personal_id, name, role]
            print('Login failed. Username or password is incorrect.')
            username = input('Username: ')
            password = input('Password: ')
    else:
        print('Error: Login table not found.')
        return None


def exit():
    # project_key = ['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Member3', 'Member4', 'Advisor', 'Status']
    # myFile = open('Project_table.csv', 'w')
    # writer = csv.writer(myFile)
    # writer.writerow(project_key)
    # myFile.close()
    # myFile = open('Project_table.csv', 'r')
    # myFile.close()
    #
    # persons_key = ['ID', 'first', 'last', 'type']
    # myFile1 = open('persons.csv', 'w')
    # writer = csv.writer(myFile1)
    # writer.writerow(persons_key)
    # myFile1.close()
    # myFile1 = open('persons.csv', 'r')
    # myFile1.close()
    #
    # login_key = ['ID', 'username', 'password', 'type']
    # myFile2 = open('login.csv', 'w')
    # writer = csv.writer(myFile2)
    # writer.writerow(login_key)
    # myFile2.close()
    # myFile2 = open('login.csv', 'r')
    # myFile2.close()

    # persons_key = ['ID', 'first', 'last', 'type']
    # persons_table = my_db.search('persons').table
    # with open('persons.csv', 'a', newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(persons_table)
    pass


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
            LeadStudent.lead_menu(self)
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
            while True:
                if choice == '1':
                    person_table.update(self.student_id, 'role', 'lead')
                    LeadStudent.create_project(self)
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
        print("Student: Responding to invitations")
        pending_invitations = MemberPendingRequestTable().filter(lambda x: x['MemberID'] == self.student_id)
        for invitation in pending_invitations.table:
            print(f"You have received an invitation for Project {invitation['ProjectID']} from {invitation['MemberName']}.")
            choice = input("Do you want to accept? (yes/no): ")
            if choice.lower() == 'yes':
                self.accept_invitation(invitation['ProjectID'])
            else:
                self.deny_invitation(invitation['ProjectID'])
            MemberPendingRequestTable().remove(invitation)
            print("Invitation response recorded.")

    def accept_invitation(self, project_id):
        my_db.search('persons').update(self.student_id, 'role', 'member')
        project_table = ProjectTable()
        project_table.add_member(project_id, self.student_id)
        print("Invitation accepted. You are now a member of the project.")

    def deny_invitation(self, project_id):
        print("Invitation denied. You are not a member of the project.")

    def find_members(self):
        while True:
            member_name = input('Enter member first name: ')
            get_data = my_db.search('persons')
            get_member = get_data.filter(lambda x: x['first'] == member_name)
            if len(get_member.table) != 0:
                print(get_member.table)
            elif len(get_member.table) == 0:
                print("Can't find this person.")
            print('Press (1) continue (2) exit')
            choice = input('Enter number: ')
            if choice == '1':
                continue
            elif choice == '2':
                break

    def submit_final_project_report(self):
        print("Lead: Submitting final project report")


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
                self.add_members_to_project()
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
        member_name = input("Enter member name to invite: ")
        member_id = self.send_invitation(member_name)
        if member_id:
            print(f"Invitation sent to {member_name} with ID: {member_id}")
        else:
            print("Invitation failed. Member not found.")

    def send_invitation(self, member_name):
        get_data = my_db.search('persons')
        get_member = get_data.filter(lambda x: x['first'] == member_name and x['role'] == 'student')
        if len(get_member.table) != 0:
            member_id = get_member.select(['ID']).values()[0]
            response = self.project_table.send_invitation(self.project_id, member_id, member_name)
            return member_id if response else None
        else:
            return None

    def send_request_to_advisors(self):
        print("Lead: Sending request to advisors")

    def create_project(self):
        print("Now, you're a project leader.")
        print('Creating process...')
        print('Do you know your member ID yet?')
        ans = input('Yes/No: ')
        if ans.lower() == 'no':
            self.find_members()
        title = input("Enter project title: ")
        lead = input("Enter lead student ID: ")
        advisor = input("Enter advisor ID: ")
        lead_student = LeadStudent([lead, {'first': '', 'last': ''}, 'lead'])
        project_id = lead_student.project_table.add_project(title, lead, advisor)
        self.projects.append(project_id)
        my_db = initializing()
        person_table = my_db.search('persons')
        person_updated = person_table.update(lead, 'type', 'lead')
        print(f"Role of lead student with ID {lead} updated to 'lead'.")
        print(self.projects)
        lead_student.add_members_to_project()
        print(person_updated)
        return my_db

    def add_members_to_project(self):
        if not self.projects:
            print("Error: No project ID is available.")
            return
        project_id = self.projects[0]
        for i in range(1, 5):
            member_id = input(f"Enter member {i} ID (or press Enter to skip): ")
            if member_id:
                member_name = self.find_member_id_by_name(member_id)
                if member_name:
                    self.project_table.add_member(project_id, member_name)
                    print(f"Member {i} added with ID: {member_id}")
                    my_db.search('persons').update(member_id, 'role', 'member')
                else:
                    print(f"Error: Member with name '{member_name}' not found.")

    def find_member_id_by_name(self, member_name):
        get_data = my_db.search('persons')
        get_member = get_data.filter(lambda x: x['first'] == member_name)
        if len(get_member.table) != 0:
            return get_member.table[0]['ID']
        else:
            return None


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
        self.firstname = self.name['first']
        self.lastname = self.name['last']

    def faculty_home(self):
        print(f'Welcome, {self.role} (Faculty ID: {self.faculty_id}, Name: {self.firstname + " " + self.lastname})')
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

    def see_advisor_requests(self):
        print("Faculty: Seeing requests to be an advisor")
        pending_requests = AdvisorPendingRequestTable().filter(lambda x: x['FacultyName'] == self.name)
        if pending_requests:
            for request in pending_requests.table:
                print(f"Project {request['ProjectID']} has requested you to be an advisor.")
                choice = input("Do you want to accept? (yes/no): ")
                if choice.lower() == 'yes':
                    self.respond_to_advisor_request(request, 'Accepted')
                else:
                    self.respond_to_advisor_request(request, 'Denied')
            print("Advisor requests handled.")
        else:
            print("No pending advisor requests.")

    def respond_to_advisor_request(self, request, response):
        AdvisorPendingRequestTable().update_response(request['ProjectID'], self.faculty_id, response, datetime.now())
        print(f"Advisor request for Project {request['ProjectID']} {response.lower()}.")

    def evaluate_projects(self, project_id):
        project = my_db.search('projects')
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

    def handle_requests(self):
        print(f'{self.role}: Handling requests')
        requests = AdvisorPendingRequestTable().filter(
            lambda x: x['to_be_advisor'] == self.faculty_id and x['Response'] is None)
        if not requests.table:
            print("No pending requests.")
            return
        for request in requests.table:
            project_id = request['ProjectID']
            member_name = \
            my_db.search('persons').filter(lambda x: x['ID'] == request['MemberID']).select(['first', 'last'])[0]
            print(f"Request for Project {project_id} from {member_name}:")
            print(f"Request Date: {request['Response_date']}")
            print("Do you want to accept the request? (yes/no)")
            choice = input()
            response_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if choice.lower() == 'yes':
                response = 'accepted'
                self.project_table.update_advisor(project_id, self.faculty_id)
                print(f"Request accepted. You are now the advisor for Project {project_id}.")
            else:
                response = 'rejected'
                print(f"Request rejected.")
            AdvisorPendingRequestTable().update_response(project_id, self.faculty_id, response, response_date)
            print("Response recorded.")

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
                self.manage_user()
                break
            print('Please try again.')
            choice = input("Enter what you're going to do: ")

    def update_database(self):
        print("Admin: Updating Database")
        print('1. Export Database to CSV')
        print('2. Import Database from CSV')
        choice = input('Enter your choice: ')
        while True:
            if choice == '1':
                self.export_database()
                break
            elif choice == '2':
                self.import_database()
                break
            print('Invalid choice. Please try again.')
            choice = input('Enter your choice: ')

    def export_database(self):
        print('Exporting Database to CSV...')

    def import_database(self):
        print('Importing Database from CSV...')

    def manage_user(self):
        print("Admin: Managing User")
        print('1. Add User')
        print('2. Remove User')
        choice = input('Enter your choice: ')
        while True:
            if choice == '1':
                self.add_user()
                break
            elif choice == '2':
                self.remove_user()
                break
            print('Invalid choice. Please try again.')
            choice = input('Enter your choice: ')

    def add_user(self):
        print('Adding User...')
        username = input('Enter username: ')
        password = input('Enter password: ')
        role = input('Enter role (student/member/lead/faculty/advisor): ')
        login_data = my_db.search('login')
        person_data = login_data.filter(lambda x: x['username'] == username)
        person_id = person_data.table[0]
        if person_id:
            print(f"User with username {username} already exists. Please choose a different username.")
            return
        user_data = {'ID': person_id, 'username': username, 'password': password, 'type': role}
        my_db.search('persons').insert(user_data)
        print(f"User {username} added successfully.")

    def remove_user(self):
        print('Removing User...')
        username = input('Enter username: ')
        lead_projects = my_db.search('projects').filter(lambda x: x['Lead'] == username).select(['ProjectID'])
        if lead_projects:
            print(f"Cannot remove user {username} as they are the lead in the following projects: {lead_projects.values()}.")
            return
        member_projects = my_db.search('projects').filter(lambda x: username in [member['Name'] for member in x['Members']]).select(['ProjectID'])
        if member_projects:
            print(f"Cannot remove user {username} as they are a member in the following projects: {member_projects.values()}.")
            return
        lead_projects = my_db.search('projects').filter(lambda x: len(x['Members']) == 0 and x['Lead'] == username).select(['ProjectID'])
        if lead_projects:
            print(f"Cannot remove the only lead user {username} from the following projects: {lead_projects.values()}.")
            return
        my_db.search('persons').remove_by_key('username', username)
        print(f"User {username} removed successfully.")


    def view_project_details(self):
        project_table = my_db.search('projects')
        print("Project Details:")
        print(project_table)

    def add_member_to_project(self):
        print('Adding Member to Project...')
        project_id = input('Enter project ID: ')
        user_id = input('Enter user ID to add as a member: ')
        project = my_db.search('projects').filter(lambda x: x['ProjectID'] == project_id).select(['Lead', 'Members'])
        if not project:
            print(f"Project with ID {project_id} not found.")
            return
        lead_username = project.values()[0]['Lead']
        members = [member['Name'] for member in project.values()[0]['Members']]
        if user_id == lead_username:
            print(f"User with ID {user_id} is the lead of the project.")
        elif user_id in members:
            print(f"User with ID {user_id} is already a member of the project.")
        else:
            my_db.search('projects').add_member(project_id, user_id)
            print(f"User with ID {user_id} added as a member to project {project_id}.")


class ProjectTable(Table):
    def __init__(self):
        super().__init__('projects', [])
        self.member_id_counter = 0

    def add_project(self, title, lead, advisor):
        project = {
            'ProjectID': len(self.table) + 1,
            'Title': title,
            'Lead': lead,
            'Members': [],
            'Advisor': advisor,
            'Status': 'Pending'
        }
        self.table.append(project)
        return project['ProjectID']

    def add_member(self, project_id, member_name):
        project = next((p for p in self.table if p['ProjectID'] == project_id), None)
        member_search = my_db.search('persons')
        if project:
            member_id = member_search.filter(lambda x: x['first'] == member_name).select(['ID'])
            if member_id:
                project['Members'].append({'ID': member_id.values()[0], 'Name': member_name})
                return member_id.values()[0]
            else:
                print(f"Member with name '{member_name}' not found.")
        else:
            print(f"Project with ID {project_id} not found.")

    def send_invitation(self, project_id, member_id, member_name):
        project = next((p for p in self.table if p['ProjectID'] == project_id), None)
        if project:
            member_table = my_db.search('persons')
            member_table.update(member_id, 'role', 'pending_invitation')
            MemberPendingRequestTable().add_request(project_id, member_id, member_name)
            return True
        else:
            return False

    def send_advisor_invitation(self, project_id, faculty_id):
        project = next((p for p in self.table if p['ProjectID'] == project_id), None)
        if project:
            faculty_table = my_db.search('persons')
            faculty_name = faculty_table.filter(lambda x: x['ID'] == faculty_id).select(['first', 'last'])
            if faculty_name:
                response = AdvisorPendingRequestTable().add_request(project_id, faculty_id, faculty_name[0])
                return response
            else:
                print(f"Faculty with ID {faculty_id} not found.")
        else:
            print(f"Project with ID {project_id} not found.")


class MemberPendingRequestTable(Table):
    def __init__(self):
        super().__init__('member_pending_request', [])

    def add_request(self, project_id, member_id, member_name):
        request = {
            'ProjectID': project_id,
            'MemberID': member_id,
            'MemberName': member_name,
            'Response': None,
            'Response_date': None
        }
        self.table.append(request)

    def update_response(self, project_id, member_id, response, response_date):
        for request in self.table:
            if request['ProjectID'] == project_id and request['MemberID'] == member_id:
                request['Response'] = response
                request['Response_date'] = response_date
                break


class AdvisorPendingRequestTable(Table):
    def __init__(self):
        super().__init__('advisor_pending_request', [])

    def add_request(self, project_id, faculty_id, faculty_name):
        request = {
            'ProjectID': project_id,
            'to_be_advisor': faculty_id,
            'FacultyName': faculty_name,
            'Response': None,
            'Response_date': None
        }
        self.table.append(request)
        return True

    def update_response(self, project_id, to_be_advisor, response, response_date):
        for request in self.table:
            if request['ProjectID'] == project_id and request['to_be_advisor'] == to_be_advisor:
                request['Response'] = response
                request['Response_date'] = response_date
                break


while True:
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
    choice = input('Press (enter) exit (0) logout: ')
    if choice.isspace() or choice == '':
        print("You're already exit the program.")
        exit()
        break

