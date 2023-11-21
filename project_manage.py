# BEGIN part 1

# import database module
from database import ReadCSV, DB, Table
import random
# define a function called initializing


def generate_random_password():
    # return ''.join(random.choices(string.digits, k=4))
    password = ''
    for i in range(1, 5):
        password += str(random.randint(0, 9))
    return password


def initializing():
    my_db = DB()
    read_csv = ReadCSV('persons.csv')
    persons = read_csv.read_csv()
    persons_table = Table('persons', persons)
    my_db.insert(persons_table)
    login = []
    login_table = Table('login', login)
    for i in persons_table.table:
        login_dict = {}
        person_id = i.get('ID', '')
        username = i.get('fist', '') + '.' + i.get('last', '')[0]
        password = generate_random_password()
        if i.get('type', '') == 'faculty':
            role = 'Faculty'
        else:
            role = 'Member'
        login_dict['person_id'] = person_id
        login_dict['username'] = username
        login_dict['password'] = password
        login_dict['role'] = role
        login.append(login_dict)
    my_db.insert(login_table)
    return my_db

# define a funcion called login


def login():
    my_db = initializing()
    login_search = my_db.search('login')
    print(login_search)
    username = input('Username: ')
    password = input('Password: ')
    for i in login_search.table:
        if i['username'] == username and i['password'] == password:
            personal_id = i.get('person_id', '')
            role = i.get('role', '')
            return [personal_id, role]
        return None

# make calls to the initializing and login functions defined above

initializing()
val = login()
print(val)

# END part 1

# CONTINUE to part 2 (to be done for the next due date)

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # do admin related activities
# elif val[1] = 'advisor':
    # do advisor related activities
# elif val[1] = 'lead':
    # do lead related activities
# elif val[1] = 'member':
    # do member related activities
# elif val[1] = 'faculty':
    # do faculty related activities
