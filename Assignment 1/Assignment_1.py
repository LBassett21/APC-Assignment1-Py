from cgi import print_environ_usage
import sqlite3

#engStud = student("Luke", "Bassett", "W001")
#print("Info for user: ", engStud.getID(), " - ", engStud.getFirstName(), engStud.getLastName())
#engStud.addDropCourse("1390141", True)
#engStud.addDropCourse("1390141", False)
#engStud.printSchedule()
#engStud.setID("W002")
#print("Info for user: ", engStud.getID(), " - ", engStud.getFirstName(), engStud.getLastName())

#prof = instructor("Marisha", "Rawlins", "W003")⌈
#print("Info for user: ", prof.getID(), " - ", prof.getFirstName(), prof.getLastName())
#prof.printClassList()
#prof.searchCourse("1390141")
#prof.printSchedule()

#assistant = admin("Cindy", "Rosner", "W004")
#print("Info for user: ", assistant.getID(), " - ", assistant.getFirstName(), assistant.getLastName())
#assistant.addCourse("Applied Programming Concepts", "Cool programming class", "1390141")
#assistant.addRemoveUser(True, "W001")
#assistant.addRemoveUser(False, "W001")
#assistant.addRemoveUserCourse(True, "W002", "1390131")
#assistant.addRemoveUserCourse(False, "W002", "1390141")
#assistant.removeCourse("1390141")
#assistant.printRoster("1390141")

db = sqlite3.connect('assignment3.db')
cursor = db.cursor()

class user:
    def __init__(self, ID, f, l):
        self.firstname = f
        self.lastname = l
        self.ID = ID
    def setFirstName(self, f):
        self.firstname = f
    def setLastName(self, l):
        self.lastname = l;
    def setID(self, i):
        self.ID = i

class student(user):
    def __init__(self, ID, firstname, lastname, expdgradyr, major, email):
        super().__init__(ID, firstname, lastname)
        self.expdgradyr = expdgradyr
        self.major = major
        self.email = email
    def searchCourse(self, crn):
        print("You looked up CRN: ", crn)
    def addDropCourse(self, crn, ad):
        if ad == True:
            print("You added CRN: ", crn)
        else:
            print("You dropped CRN: ", crn)
    def printSchedule(self):
        print("Printed out your schedule! Kinda...")

class instructor(user):
    def __init__(self, ID, firstname, lastname, title, yearofhire, department, email):
        super().__init__(ID, firstname, lastname)
        self.title = title
        self.yearofhire = yearofhire
        self.department = department
        self.email = email
    def printSchedule(self):
        print("Printed out your schedule! Kinda...")
    def printClassList(self):
        print("Printed out your class list! Kinda...")
    def searchCourse(self, crn):
        print("You searched for course: ", crn)

class Admin(user):
    def __init__(self, ID, firstname, lastname, title, office, email):
        super().__init__(ID, firstname, lastname)
        self.title = title
        self.office = office
        self.email = email
    def addCourse(self, cn, cd, crn):
        print("Added course name: ", cn)
        print("Added course description: ", cd)
        print("Added course number: ", crn)
    def removeCourse(self, crn):
        print("Removed course number: ", crn)
    def addRemoveUser(self, ar):
        if ar == True:
            print("What type of user would you like to add?")
            choice = input("Enter your choice (Admin, Instructor, Student): ")
            if choice == "Admin":
                print("Please enter the following information")
                idn = input("ID number: ")
                fn = input("First name: ")
                ln = input("Last name: ")
                title = input("Title: ")
                office = input("Office: ")
                email = input("Email: ")
                new_admin(idn,fn,ln,title,office,email)
            elif choice == "Instructor":
                print("Please enter the following information")
                idn = input("ID number: ")
                fn = input("First name: ")
                ln = input("Last name: ")
                yoh = input("Year of Hire: ")
                dept = input("Department: ")
                email = input("Email: ")
            elif choice == "Student":
                print("Please enter the following information")
                idn = input("ID number: ")
                fn = input("First name: ")
                ln = input("Last name: ")
                egy = input("Expected graduation year: ")
                major = input("Major: ")
                email = input("Email: ")
            else:
                print("Invalid Input!")
        else:
            print("Please enter the ID of the user")
            removeid = input("ID Number: ")
            cursor.execute("""SELECT ID FROM admin WHERE ID=?""", (removeid,))
            admin_check = cursor.fetchone()
            cursor.execute("""SELECT ID FROM instructor WHERE ID=?""", (removeid,))
            instructor_check = cursor.fetchone()
            cursor.execute("""SELECT ID FROM student WHERE ID=?""", (removeid,))
            student_check = cursor.fetchone()
            if admin_check or instructor_check or student_check:
                confirm = input(f"Are you sure you want to remove user ID: {removeid}. (Yes/No): ")
                if confirm == "Yes":
                        if admin_check:
                            cursor.execute("""DELETE FROM admin WHERE ID=?""", (removeid,))
                            db.commit()
                            print("User removed from the admin table.")
                        if instructor_check:
                            cursor.execute("""DELETE FROM instructor WHERE ID=?""", (removeid,))
                            db.commit()
                            print("User removed from the instructor table.")
                        if student_check:
                            cursor.execute("""DELETE FROM student WHERE ID=?""", (removeid,))
                            db.commit()
                            print("User removed from the student table.")
                else:
                    print("Canceling user removal...")
            else:
                print("User not found in the database")

    def addRemoveUserCourse(self, ar, uid, crn):
        if ar == True:
            print("Added course: ", crn, " for user ID ", uid)
        else:
            print("Removed course: ", crn, " for user ID ", uid)
    def printRoster(self):
        print_database()


def add_admin():
    admin_list = []
    cursor.execute("""SELECT * FROM admin""")
    all_admin_info = cursor.fetchall()

    for admin_info in all_admin_info:
        ID, first_name, last_name, title, office, email = admin_info
        existing_admin = next((Admin for Admin in admin_list if Admin.ID == ID), None)
        if existing_admin:
            continue

        newadmin = Admin(ID, first_name, last_name, title, office, email)
        admin_list.append(newadmin)

    return admin_list

def add_student():
    student_list = []
    cursor.execute("""SELECT * FROM student""")
    all_student_info = cursor.fetchall()

    for student_info in all_student_info:
        ID, first_name, last_name, expectedgradyear, major, email = student_info
        existing_student = next((student for student in student_list if student.ID == ID), None)
        newstudent = student(ID, first_name, last_name, expectedgradyear, major, email)
        student_list.append(newstudent)

    return student_list

def add_instructor():
    instructors = []
    cursor.execute("""SELECT * FROM instructor""")
    all_instructor_info = cursor.fetchall()

    for instructor_info in all_instructor_info:
        ID, first_name, last_name, title, yearofhire, department, email = instructor_info
        newinstructor = instructor(ID, first_name, last_name, title, yearofhire, department, email)
        instructors.append(newinstructor)

    return instructors

def new_admin(ID, firstname, lastname, title, office, email):
    cursor.execute("""SELECT ID FROM admin WHERE ID=?""", (ID,))
    existing_id = cursor.fetchone()

    if existing_id: 
        print("Error: User with ID", ID, "already exists.")
    else:
        cursor.execute("""INSERT INTO admin (ID, NAME, SURNAME, TITLE, OFFICE, EMAIL) VALUES (?,?,?,?,?,?)""",(ID,firstname,lastname,title,office,email))
        db.commit()


def print_database():
    admin_objects = add_admin()
    student_objects = add_student()
    instructor_object = add_instructor()
    print("----- Students -----")
    for student in student_objects:
        print(student.ID,student.firstname,student.lastname,student.expdgradyr,student.major,student.email)

    print("----- Instructors -----")
    for instructor in instructor_object:
        print(instructor.ID,instructor.firstname,instructor.lastname,instructor.title,instructor.yearofhire,instructor.department,instructor.email)

    print("----- Admins -----")
    for Admin in admin_objects:
        print(Admin.ID, Admin.firstname, Admin.lastname, Admin.title, Admin.office, Admin.email)


admin_objects = add_admin()
student_objects = add_student()
instructor_object = add_instructor()
print_database()

cursor.execute("""PRAGMA table_info(admin)""")
columns = cursor.fetchall()

column_names = [column[1] for column in columns]
print("Column Names:")
for column_name in column_names:
    print(column_name)

access_granted = False
logged_in_user = None

while not access_granted:
    print("------ Login Screen ------")
    username = input("Please enter email: ")
    password = input("Please enter id number: ")

    found_un = any(admin.email == username for admin in admin_objects)
    found_pw = any(str(admin.ID) == password for admin in admin_objects if admin.email == username)

    if found_un and found_pw:
        print("Welcome")
        access_granted = True
        logged_in_user = next((admin for admin in admin_objects if admin.email == username), None)
    else:
        print("Incorrect username or password, try again")


while True:
    print("Welcome to the admin control pannel, what would you like to do?")
    print("1. Add/Remove User")
    print("2. Update User")
    print("3. Print all...")
    print("4. Add/Remove Course")
    print("5. Update Course")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("Would you like to add or remove a user?")
        choice = input("Enter add or remove: ")
        if choice == "add":
            logged_in_user.addRemoveUser(True)
        elif choice == "remove":
            logged_in_user.addRemoveUser(False)
        else:
            print("Invalid Choice")
    elif choice == "2":
        print("Test2")
    elif choice == "3":
        print("Test3")
    elif choice == "4":
        print("Test4")
    elif choice == "5":
        print("Test5")
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

