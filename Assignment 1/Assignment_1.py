from user import user
from student import student
from instructor import instructor
from admin import admin

engStud = student("Luke", "Bassett", "W001")
print("Info for user: ", engStud.getID(), " - ", engStud.getFirstName(), engStud.getLastName())
engStud.addDropCourse("1390141", True)
engStud.addDropCourse("1390141", False)
engStud.printSchedule()
engStud.setID("W002")
print("Info for user: ", engStud.getID(), " - ", engStud.getFirstName(), engStud.getLastName())

prof = instructor("Marisha", "Rawlins", "W003")
print("Info for user: ", prof.getID(), " - ", prof.getFirstName(), prof.getLastName())
prof.printClassList()
prof.searchCourse("1390141")
prof.printSchedule()

assistant = admin("Cindy", "Rosner", "W004")
print("Info for user: ", assistant.getID(), " - ", assistant.getFirstName(), assistant.getLastName())
assistant.addCourse("Applied Programming Concepts", "Cool programming class", "1390141")
assistant.addRemoveUser(True, "W001")
assistant.addRemoveUser(False, "W001")
assistant.addRemoveUserCourse(True, "W002", "1390131")
assistant.addRemoveUserCourse(False, "W002", "1390141")
assistant.removeCourse("1390141")
assistant.printRoster("1390141")
