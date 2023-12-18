In database.py :
    i modified the csv-reader to be class.

In project-manage.py :
    I import database module
    - Define a funcion called initializing. In function i created an object to read all csv files that will serve as a persistent state for this program, created all the corresponding tables for those csv files, added all these tables to the database. 
    - Define a funcion called login that add code that performs a login task. In this function will ask a user for a username and password and returns [ID, role] if valid, otherwise returning None
