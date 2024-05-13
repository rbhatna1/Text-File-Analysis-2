import pickle,os

def space(): #To make it look good and have proper demarcations
    print()
    print("**********************************************************")
    print()
    
def adding():
    Mcode=int(input("enter the Mcode"))
    Mname=str(input("Enter the Mname"))
    Housetype=str(input("Enter the Housetype"))
    Noofphones=int(input("enter the No of Rooms"))
    Cost=int(input("enter the Cost"))
    with open("society.dat","ab+") as A:
        list1=[Mcode,Mname,Housetype,Noofphones,Cost]
        pickle.dump(list1,A)
        print("The data has been added")
        A.close()
            
def displaying():
    try:
        with open("society.dat","rb") as A:
            try:
                while True:
                    ele=pickle.load(A)
                    print(ele)
            except EOFError:
                A.close()
    except:
        print("The file doesn't exist")
            
def searchingforrooms():
    n=int(input("Enter the number of rooms"))
    with open("society.dat","rb") as A:
        try:
            while True:
                rec=pickle.load(A)
                if rec[3]>n:
                    print(rec)
        except:
            A.close()
            
def searchingforhigduplex():
    with open("society.dat","rb") as A:
        try:
            while True:
                rec=pickle.load(A)
                if rec[2].upper() in ["HIG","DUPLEX"]:
                    print(rec)
        except:
            A.close()
    
def deleting():
    with open("society.dat","rb") as A:
        with open("society2.dat","wb") as B:
            Flag=True
            try:
                while True:
                    rec=pickle.load(A)
                    if rec[3]==1:
                        Flag=False
                        continue
                    else:
                        pickle.dump(rec,B)
            except:
                A.close()
                B.close()
                if Flag is True:
                    print("The given element doesn't exist in the file")
                os.remove("society.dat")
                os.rename("society2.dat","society.dat")
    
def addingtodelux():
    with open("society.dat","rb") as A:
        with open("Delux.dat","ab") as B:
            Flag=True
            try:
                while True:
                    rec=pickle.load(A)
                    if rec[2].upper() in ["VILLA","DUPLEX"]:
                        pickle.dump(rec,B)
                        Flag=Flase
            except:
                if Flag is False:
                    print("The given element has been printed in the Delux.dat")
                A.close()
                B.close()

def modify():
    with open("society.dat","rb") as A:
        with open("society2.dat","wb") as B:
            Flag=True
            try:
                while True:
                    rec=pickle.load(A)
                    if rec[3]==4:
                        cost=int(input("Enter the cost"))
                        list1=[rec(0),rec(1),rec(2),rec(3),cost]
                        pickle.dump(list1,B)
                        Flag=False
                    else:
                        pickle.dump(rec,B)
            except:
                A.close()
                B.close()
                if Flag is True:
                    print("The given element doesn't exist in the file")
                os.remove("society.dat")
                os.rename("society2.dat","society.dat")
                    
def addingatposition():
    position=int(input("enter the Mcode"))
    Mname=str(input("Enter the Mname"))
    Housetype=str(input("Enter the Housetype"))
    Noofphones=int(input("enter the No of Rooms"))
    Cost=int(input("enter the Cost"))
    recn=[position,Mname,Housetype,Noofphones,Cost]
    with open("society.dat","rb") as A:
        with open("society2.dat","wb") as B:
            Flag=True
            try:
                while True:
                    rec=pickle.load(A)
                    if rec[0]>position and Flag is True:
                        pickle.dump(recn,B)
                        Flag=False
                    pickle.dump(rec,B)
            except:
                A.close()
                B.close()
                if Flag is True:
                    print("The given element doesn't exist in the file")
                os.remove("society.dat")
                os.rename("society2.dat","society.dat")
                
choice=0

while choice!=9:
    print("Choose from one of the following options")
    print("1)Appending data into the file")
    print("2)Displaying the records present in the file. If the file does not exist, an appropriate message should be displayed")
    print("3)Searching for records where no of rooms is less than n")
    print("4)Display those records of housetype “HIG” and “Duplex”")
    print("5)Delete the record of that member where no of rooms is 1")
    print("6)Copy the records of housetype “Villa” and “Duplex” to Delux.dat")
    print("7)Modify the record of 4 room flat by updating its cost")
    print("8)Insert a new record at the position specified by the user. If the position does not exist, the record should be added at the end")
    print("9)To exit the loop")
    choice=int(input("Enter the choice"))
    
    if choice==1:
        space()
        adding()
        space()
        
    elif choice==2:
        space()
        displaying()
        space()
        
    elif choice==3:
        space()
        searchingforrooms()
        space()
        
    elif choice==4:
        space()
        searchingforhigduplex()
        space()
        
    elif choice==5:
        space()
        deleting()
        space()
    
    elif choice==6:
        space()
        addingtodelux()
        space()
        
    elif choice==7:
        space()
        modify()
        space()
        
    elif choice==8:
        space()
        addingatposition()
        space()

def space(): #To make it look good and have proper demarcations
    print()
    print("**********************************************************")
    print()
    
def insert2():
    Empno=int(input("enter the Empno"))
    Ename=str(input("Enter the Ename"))
    Dept=str(input("Enter the Department"))
    Desig=int(input("enter the Designation"))
    Salary=int(input("enter the Salary"))
    list1=[Empno,Ename,Dept,Desig,Salary]
    with open("salary.dat","rb") as A:
        with open("salary2.dat","wb") as B:
            Flag=True
            try:
                while True:
                    rec=pickle.load(A)
                    if rec[0]>Empno and Flag is True:
                        pickle.dump(rec,B)
                        Flag=False
                    pickle.dump(rec,B)
            except:
                A.close()
                B.close()
                if Flag is True:
                    print("The given element doesn't exist in the file")
                os.remove("salary.dat")
                os.rename("salary2.dat","salary.dat")
    
def display2():
    try:
        with open("salary.dat","rb") as A:
            try:
                while True:
                    ele=pickle.load(A)
                    print(ele)
            except EOFError:
                A.close()
    except:
        print("The file doesn't exist")
        
def counting():
    with open("salary.dat","rb") as A:
        count=0
        try:
            while True:
                rec=pickle.load(A)
                if rec[2].upper() in ["HR"]:
                    count+=1
        except:
            A.close()
        print("The count is",count) 
            
def displaymanagers():
    with open("salary.dat","rb") as A:
        try:
            while True:
                rec=pickle.load(A)
                if rec[3]=="Manager" and rec[2]=="HR":
                    print(rec)
        except:
            A.close()
            
def maxsalary():
    with open("salary.dat","rb") as A:
        Flag=True
        try:
            while True:
                rec=pickle.load(A)
                if Flag is True:
                    maxsalary=rec[4]
                    maxrec=rec
                    Flag=False
                elif maxsalary<rec[4]:
                    maxsalary=rec[4]
                    maxrec=rec
        except:
            A.close()
        print("The record is",maxrec)
        
def deleting2():
    empno=int(input("Enter the Empno of the record to be deleted"))
    with open("salary.dat","rb") as A:
        with open("salary2.dat","wb") as B:
            Flag=True
            try:
                while True:
                    rec=pickle.load(A)
                    if rec[0]==empno:
                        Flag=False
                        continue
                    else:
                        pickle.dump(rec,B)
            except:
                A.close()
                B.close()
                if Flag is True:
                    print("The given element doesn't exist in the file")
                os.remove("salary.dat")
                os.rename("salary2.dat","salary.dat")
    
choice=0

while choice!=7:
    print("Choose from one of the following options")
    print("1)Insert records into the sorted file")
    print("2)Read and Display all the records")
    print("3)Display the records of Managers from Admin department")
    print("4)Count the number of employees in HR department")
    print("5)Display the record of employee earning the maximum salary")
    print("6)Delete the record of employee whose empno is input by the user")
    print("7)To exit the loop")
    choice=int(input("Enter the choice"))
    
    if choice==1:
        space()
        insert2()
        space()
        
    elif choice==2:
        space()
        display2()
        space()
        
    elif choice==3:
        space()
        counting()
        space()
        
    elif choice==4:
        space()
        displaymanagers()
        space()
        
    elif choice==5:
        space()
        maxsalary()
        space()
    
    elif choice==6:
        space()
        deleting2()
        space()