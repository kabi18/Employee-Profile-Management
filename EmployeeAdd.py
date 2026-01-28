import pickle
import sys
def addemployee():


        with open("emp.info","ab") as fp:
            while(True):
                number=int(input("enter the employee id:"))
                name=input("enter the employee name:")
                salary=float(input("enter the employee salary:"))
                compnyname=input("enter the company name:")
                lst=[]
                lst.append(number)
                lst.append(name)
                lst.append(salary)
                lst.append(compnyname)
                pickle.dump(lst,fp)
                print("\tEmployee Data Saved as Record in File Sucessfully")

                ch=input("if you want to add the another employee (yes/no):")
                if(ch.lower()=="no"):
                    break




