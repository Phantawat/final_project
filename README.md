# Phantawat Senior managing program
  - project_manage.py: Contains the main program logic and user interface, Includes all of classes in program.
  - database.py: Defines classes related to database management and classes for managing tables.
  - persons.csv: Database for creating tables.
  - login.csv: Database for login the program.
  - Project_Table.csv: A file which was exit from the program.
  - README.md: Documentation file with project information.
  - TODO.md: Documentation file with role information
  - proposal.md: Documentation file with evaluation steps.
  
# To run the project:
  1. Install the required dependencies: (list dependencies)
  2. Open a terminal and navigate to the project directory.
  3. Run the command: python main.py

## Role Action Table

### Student Role

| Action                           | Methods/Classes                             | Completion (%) |
| -------------------------------- | --------------------------------------------| ---------------|
| Create Project                   | `LeadStudent.create_project`                | 100            |
| Respond to Invitation            | `Student.respond_to_invitation`             | 90             |
| View Project Details             | `Student.view_project_details`              | 100            |
| Add Members to Project           | `Student.add_members_to_project`            | 80             |
| Submit Final Project Report      | `Student.submit_final_project_report`       | 100            |

### LeadStudent Role

| Action                           | Methods/Classes                             | Completion (%) |
| -------------------------------- | --------------------------------------------| ---------------|
| Create Project                   | `LeadStudent.create_project`                | 100            |
| Find Members                     | `LeadStudent.find_members`                  | 100            |
| Invite Members                   | `LeadStudent.invite_members`                | 90             |
| Add Members to Project           | `LeadStudent.add_members_to_project`        | 80             |
| View and Modify Project Details  | `LeadStudent.view_project_details`          | 100            |
| Send Request to Advisors         | `LeadStudent.send_request_to_advisors`      | 70             |
| Submit Final Project Report      | `LeadStudent.submit_final_project_report`   | 100            |

### Faculty Role

| Action                           | Methods/Classes                             | Completion (%) |
| -------------------------------- | --------------------------------------------| ---------------|
| See Requests to Be a Supervisor  | `Faculty.see_supervisor_requests`           | 100            |
| Send Deny Response               | `Faculty.handle_requests`                   | 100            |
| See Details of All Projects      | `Faculty.view_project_details`              | 100            |
| Evaluate Projects                | `Faculty.evaluate_projects`                 | 80             |
| Approve Project                  | `Faculty.approve_project`                   | 90             |

### Advisor Role

| Action                           | Methods/Classes                             | Completion (%) |
| -------------------------------- | --------------------------------------------| ---------------|
| See Requests to Be a Supervisor  | `Faculty.see_supervisor_requests`           | 100            |
| See Requests to Be an Advisor    | `Faculty.see_advisor_requests`              | 100            |
| See Details of All Projects      | `Faculty.view_project_details`              | 100            |
| Evaluate Projects                | `Faculty.evaluate_projects`                 | 80             |
| Approve Project                  | `Faculty.approve_project`                   | 90             |

### Admin Role

| Action                           | Methods/Classes                             | Completion (%) |
| -------------------------------- | --------------------------------------------| ---------------|
| Update Database                  | `Admin.update_database`                     | 100            |
| Export Database to CSV           | `Admin.export_database`                     | 100            |
| Import Database from CSV         | `Admin.import_database`                     | 100            |
| Manage User                      | `Admin.manage_user`                         | 100            |
| Add User                         | `Admin.add_user`                            | 100            |
| Remove User                      | `Admin.remove_user`                         | 100            |
| Add Member to Project            | `Admin.add_member_to_project`               | 70             |

| Role  | Action                   | Methods/Classes                             | Completion (%)  |
|-------|--------------------------|---------------------------------------------|-----------------|
| Admin | Read CSV                 | ReadCSV.read_csv                            | 100             |
| Admin | Create Table             | Table.__init__                              | 100             |
| Admin | Insert Entry             | TableManagement.perform_insert              | 100             |



# Missing Features:
  - Approval of Project by Advisor
  - Evaluation of Projects by Faculty

# Known Bugs:
  - Issue with responding to invitations for some students.
  - Evaluation comments not saved properly in the database.
  - Creating projects cannot save in the database.
  - Adding member to Projects not sending invitation to some student.
  - Role might have changed in the csv file.
