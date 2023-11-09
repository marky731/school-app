from DBmanager import DBmanager as dbm
from AllClasses import Student, Teacher
import datetime
db = dbm()
print('(connection created)  ')
print('wellcome to the app! ')
print('1 for search a student by id')
print('2 for list students of a class')
print('3 for add a student')
# print('4 for edit a existing student')
# print('5 foradd a teacher')
# print('6 for edit a existing teacher')  ## these will be written later
print('0 for terminate')
while True:
    print("----------------------------------")
    operation = int(input("choice: "))
    if operation == 0:
        print('Have a nice day :) ')
        break
    elif operation ==1:
        id = int(input("ID of the student: "))
        std_obj, std_list = db.getStudentById(id)
        print(std_list)
    elif operation ==2:
        print('ID of the class: \n1 = 10/A\n2 = 10/B\n3 = 10/C\n4 = 10/D')
        id = int(input("ID: "))
        std_obj, std_list = db.getStudentByClass(id)
        for student in std_list:
            print(student)
    elif operation ==3:
        stdnt = Student(None,None,None,None,None,None,None)

        number = input("stundent number: ")
        stdnt.studentNumber = number

        name = input("stundent name: ")
        stdnt.name = name

        surname = input("stundent surname: ")
        stdnt.surname = surname

        birthdate = input("stundent birthdate: ")
        dataFormat = '%Y/%m/%d'
        birth = datetime.datetime.strptime(birthdate, dataFormat)
        stdnt.birhtdate = birth

        gender = input("stundent gender: ")
        stdnt.gender = gender

        classid = input("stundent class id: ")
        stdnt.classid = classid

        db.addStudent(stdnt)
    # elif operation ==4:
    #     pass
    # elif operation ==5:
    #     pass
    # elif operation ==6:
    #     pass   ## these will be written later

