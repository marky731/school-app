import mysql.connector
import datetime

class Student:
    def __init__(self,id,studentNumber,name,surname,birthdate,gender,classid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        # if len(name) > 45:
        #     raise Exception("Max 45 characters for 'name' ! ")
        self.surname = surname
        self.birhtdate = birthdate
        self.gender = gender
        self.classid = classid

    @staticmethod
    def CreateStudent(obj):
        list = []
        if isinstance(obj, tuple):
            list.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for tpl in obj:
                list.append(Student(tpl[0],tpl[1],tpl[2],tpl[3],tpl[4],tpl[5],tpl[6]))
        return list
    
class Teacher:
    def __init__(self,id,branch,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.branch = branch
        self.name = name
        self.surname = surname
        self.birhtdate = birthdate
        self.gender = gender

class Class:
    def __init__(self,id,name,teacherid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.name = name
        self.teacherid = teacherid

class ClassLesson:
    def __init__(self,classid,lessonid,teacherid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.classid = classid
        self.teacherid = teacherid
        self.lessonid = lessonid 


class Lesson:
    def __init__(self,id,name):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.name = name


