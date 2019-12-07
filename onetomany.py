class course:
 def __init__(self,cid,cname,cprice):
   self.cid = cid
   self.cname = cname
   self.cprice = cprice

class Student:
 def __init__(self,sid,sName,saddr,coursesList):
    self.sid = sid
    self.sName = sName
    self.saddr = saddr
    self.coursesList = coursesList

    def getStudentDetails(self):
        print("Student details  :")
        print("----------------------------")
        print("Student Id :",self.sid)
        print("Student name :",self.sName)
        print("Student saddr :",self.saddr)
        print("cid\tcname\tcprice")
        print("--------------")
        for course in self.courseList:
            print(course.cid,end="\t")
            print(course.cname,end="\t")
            print(course.cprice,end="\n")
        print()

course1 = course("C-111","C",1000)
course2 = course("C-222","C++",2000)
course3 = course("C-333","JAVA",5000)
course4 = course("C-444","PYTHON",6000)
courseList = [course1,course2,course3,course4]

std1 = Student("S-111", "AAA", "BNG", courseList)
std2 = Student("S-222", "BBB", "BNG", courseList)
std3 = Student("S-333", "CCC", "BNG", courseList)
std4 = Student("S-444", "DDD", "BNG", courseList)

std1.getStudentDetails()
std2.getStudentDetails()
std3.getStudentDetails()
std4.getStudentDetails()


        

