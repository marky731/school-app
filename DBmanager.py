import mysql.connector
from datetime import datetime
from Connection import connection
from AllClasses import Student, Teacher

class DBmanager:
    # mycursor = connection.cursor()
    def __init__(self):
        self.connection = connection
        self.cursor = connection.cursor() 

    def getStudentById(self, id):
        sql = 'SELECT * from students where id=%s'
        values = (id,)
        self.cursor.execute(sql,values)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj), obj # returns list of class Student
        except mysql.connector.Error as err:
            print('Error: ', err)

    def getStudentByClass(self, classid):
        sql = 'SELECT * from students where classid=%s'
        values = (classid,)
        self.cursor.execute(sql,values)
        try: 
            object = self.cursor.fetchall()
            return Student.CreateStudent(object), object
        except mysql.connector.Error as err:
            print('Error: ', err)

    def addStudent(self, student: Student):
        sql = 'INSERT INTO students(studentnumber,name,surname,birthdate,gender,classid) VALUES (%s,%s,%s,%s,%s,%s)'
        values = (student.studentNumber,student.name,student.surname,student.birhtdate,student.gender,student.classid)
        self.cursor.execute(sql,values)
        try:
            connection.commit()
            print(f"{self.cursor.rowcount} many rows are added. ")
        except mysql.connector.Error as err:
            print('Error my friend: ', err)
            
    def editStudent(self, student: Student):
        sql = 'UPDATE students SET studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classid=%s WHERE id=%s'
        values = (student.studentNumber, student.name, student.surname, student.birhtdate, student.gender, student.classid, student.id)
        self.cursor.execute(sql,values)
        try:
             connection.commit()
             print(f"{self.cursor.rowcount} many rows are added. ")
        except mysql.connector.Error as err:
             print('Error: ', err)

    def addTeacher(self, teacher: Teacher):
        sql = 'INSERT INTO teacher(branch,name,surname,birthdate,gender) VALUES (%s,%s,%s,%s,%s)'
        values = (teacher.branch, teacher.name, teacher.surname, teacher.birhtdate, teacher.gender)
        self.cursor.execute(sql,values)
        try:
            connection.commit()
            print(f"{self.cursor.rowcount} many rows are added. ")
        except mysql.connector.Error as err:
            print('Error my friend: ', err)

    def editTeacher(self, teacher: Teacher):
        sql = 'UPDATE teacher SET branch=%s,name=%s,surname=%s,birthdate=%s,gender=%s WHERE id=%s'
        values = (teacher.branch, teacher.name, teacher.surname, teacher.birhtdate, teacher.gender, teacher.id)
        self.cursor.execute(sql, values)
        try:
            connection.commit()
            print(f'{self.cursor.rowcount} many rows eddited. ')
        except mysql.connector.Error as err:
            print("error : ", err)

    def __del__ (self):
        self.connection.close()
        print('(connection closed)  ')



# db = DBmanager()

# sdnt = db.getStudentById(7)
# # print(sdnt[0])
# sdnt[0].name = 'Polat'
# sdnt[0].surname = 'cakir'
# db.editStudent(sdnt[0])


# print(sdnt[1].name)
# sdnt = db.getStudentByClass(5)
# print(sdnt[0].name)
# print(sdnt[0].surname)

# tchr = Teacher(6, 'science', 'Cengiz', 'Yilmaz', datetime(1982,2,18),'E')
# db.addTeacher(tchr)