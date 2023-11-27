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



# define a funcion called login

def login():
    my_db = initializing()
    login_search = my_db.search('login')
    print(login_search)
    username = input('Username: ')
    password = input('Password: ')
    for i in login_search.table:
        while i['username'] != username or i['password'] != password:
            if i['username'] != username:
                print('Username or password is incorrect!')
            elif i['username'] == username and i['password'] != password:
                print('Password is incorrect!')
            username = input('Username: ')
            password = input('Password: ')
        personal_id = i.get('person_id', '')
        role = i.get('role', '')
        return [personal_id, role]
    return None

# define a function called exit
def exit():
    data = initializing()
    projects = data.search('project')
    myFile = open('Project_table.csv', 'w')
    writer = csv.writer(myFile)
    writer.writerow([])
    for dict in projects:
        writer.writerow(dict.values())
    myFile.close()
    myFile = open('Project_table.csv', 'r')
    print(myFile.read())
    myFile.close()
    pass

# make calls to the initializing and login functions defined above

initializing()
val = login()

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
# see and do admin related activities
# elif val[1] = 'student':
# see and do student related activities
# elif val[1] = 'member':
# see and do member related activities
# elif val[1] = 'lead':
# see and do lead related activities
# elif val[1] = 'faculty':
# see and do faculty related activities
# elif val[1] = 'advisor':
# see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit()
