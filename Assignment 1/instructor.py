from user import user

class instructor(user):
    def __init__(self, firstname, lastname, ID):
        super().__init__(firstname, lastname, ID)
    def printSchedule(self):
        print("Printed out your schedule! Kinda...")
    def printClassList(self):
        print("Printed out your class list! Kinda...")
    def searchCourse(self, crn):
        print("You searched for course: ", crn)




