from user import user

class admin(user):
    def __init__(self, firstname, lastname, ID):
        super().__init__(firstname, lastname, ID)
    def addCourse(self, cn, cd, crn):
        print("Added course name: ", cn)
        print("Added course description: ", cd)
        print("Added course number: ", crn)
    def removeCourse(self, crn):
        print("Removed course number: ", crn)
    def addRemoveUser(self, ar, uid):
        if ar == True:
            print("Added user ID: ", uid)
        else:
            print("Removed user ID", uid)
    def addRemoveUserCourse(self, ar, uid, crn):
        if ar == True:
            print("Added course: ", crn, " for user ID ", uid)
        else:
            print("Removed course: ", crn, " for user ID ", uid)
    def printRoster(self, crn):
        print("Roster for CRN: ", crn, " ...")