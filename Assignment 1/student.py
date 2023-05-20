from user import user

class student(user):
    def __init__(self, firstname, lastname, ID):
        super().__init__(firstname, lastname, ID)
    def searchCourse(self, crn):
        print("You looked up CRN: ", crn)
    def addDropCourse(self, crn, ad):
        if ad == True:
            print("You added CRN: ", crn)
        else:
            print("You dropped CRN: ", crn)
    def printSchedule(self):
        print("Printed out your schedule! Kinda...")