import sys
class Emplyoee:
    def __init__(self,eno,ename,esal,eaddr,sortingKey="ENO"):
    self.eno = eno
    self.ename = ename
    self.esal = esal
    self.eaddr = eaddr
    def __lt__(self,other):
        if self.sortingKey == "ENO":
           return self.eno < other.eno
        elif self.sortingKey == "ENAME"
            return self.ename < other.ename
        elif self.sortingKey == "ESAL"
            return self.esal < other.esal
        elif self.sortingKey == "EADDR"
            return self.eaddr < other.eaddr
        else:
            pass

emp1 = Employee(111,'Kruthi',9000,'HYD')
emp2 = Employee(222,'Bruno',8000,'PUNE')
emp3 = Employee(333,'chayu',1000,'KAR')
emp4 = Employee(444,'divi',3000,'BLR')
emp5 = Employee(555,'Ranju',2000,'CHE')

def sort(list):
    while True:
        count = 0
        for x in range(0, len(list) - 1):
            if list[x] < list[x+1]:
                pass

            else:
                count = count + 1
                temp = list[x]
                list[x] = list [x+1]

            if count == 0
               break
            else:
                continue
list = [emp1 , emp2 , emp3 , emp4 , emp5]
while True:
    print("1.Sorting By ENO")
    print("2.Sorting BY ENAME")
    print("3.Sorting By ESAL")
    print("4.Sorting By EADDR")
    print("EXIT")
    option = int(input("Your options :")
    if option == 1:
       Employee.sortingKey = "ENO"
       sort(list)
    elif option == 2:
       Employee.sortingKey = "ENAME"
       sort(list)
    elif option == 3:
       Employee.sortingKey = "ESAL"
       sort(list)
    elif option == 4:
       Employee.sortingKey = "EADDR"
       sort(list)
    elif option == 5:
       Employee.sortingKey = "EXIT"
       sys.exit
    else:
        print("Provide the number from 1 to 5")
    print("ENO\tENAME\tESAL\tEADDR")
    print("----------------------------------------")

    for emp in list:
        print(emp.eno,"\t", emp.ename,"\t", emp.esal,"\t", emp.eaddr,"\t")
    print()



    
             
    
    
