import json
import mysql.connector

with open("input.json","r") as file:
    data=json.load(file)
mydb=mysql.connector.connect(host="13.126.56.246",user="harsha",password="5Hfnfr24Pw5PBRd",database="Employee_db")
cursor=mydb.cursor()
for item in data:
    qry="insert into employee(name,department,position,salary)values(%s,%s,%s,%s)"
    val=(item["name"],item["department"],item["position"],item["salary"])
    cursor.execute(qry,val)
    mydb.commit()
    
    

def ids():
    qry="select id from employee"
    cursor.execute(qry)
    x=cursor.fetchall()
    ids_list=[]
    for i in x:
        ids_list.append(i[0])
    return ids_list 

def names():
    qry="select * from employee"
    cursor.execute(qry)
    result=cursor.fetchall()
    list_of_names=[]
    for i in result:
        list_of_names.append(i[1]) 
    return list_of_names
def add_employee():
    
    list_of_ids=ids()
    while True:
        id=input("Enter employee id: ")
        if id.isdigit():
            id=int(id)
            if id in list_of_ids:
                print("ID already exists...Try new one")
            else:
                name=input("enter employee name:")
                department=input("enter department name:")
                position=input("enter position name:")
                salary=int(input("enter salary:"))   
                t=(id,name,department,position,salary)
                qry="insert into employee values(%s,%s,%s,%s,%s)"
                cursor.execute(qry,t)
                mydb.commit()
                print("Employee added")
                break 
        else:
            print("Enter a valid id") 

def delete_records():
    print("delete record by...\n1.id\n2.name")
    choice=input("enter the choice(1-2): ")
    while True:
        if choice.isdigit():
            choice=int(choice)
            if 1<=choice<=2:
                break 
            else:
                print("enter the correct choice(1-2)")
        else:
            print("enter a number")
    if choice==1:
        list_of_ids=ids()
        while True:
            id=input("enter id to delete record: ")
            
            if id.isdigit():
                id=int(id)
                if id in list_of_ids:
                    break
                else:
                    print("ID not exist")
            else:
                print("enter a valid id")
        t=(id,)
        qry="delete from employee where id=%s;"        
        
        cursor.execute(qry,t)
        mydb.commit()
        print("record deleted")
    if choice==2:
        while True:
            name=input("enter name to delete record: ").lower()
            list_of_names=names()
            if name in list_of_names:
                qry="delete from employee where name=%s;"
                val=(name,)
                cursor.execute(qry,val)
                mydb.commit()
                print("record deleted")
                break
            else:
                print("Invalid name")
def search_records():
    print("search records by...\n1.id\n2.name")
    
    while True:
        choice=input("enter the choice(1-2): ")
        if choice.isdigit():
            choice=int(choice)
            if 1<=choice<=2:
                break 
            else:
                print("enter the correct choice(1-2)")
        else:
            print("enter a number")
    if choice==1:
        list_of_ids=ids()
        while True:
            id=input("enter id to select record: ")
            
            if id.isdigit():
                id=int(id)
                if id in list_of_ids:
                    break
                else:
                    print("ID not exist")
            else:
                print("enter a valid id")
        t=(id,)
        qry="select * from employee where id=%s;"        
        
        cursor.execute(qry,t)
        for i in cursor:
            print(i)
        
    if choice==2:
        while True:
            name=input("enter name to select record: ").lower()
            list_of_names=names()
            if name in list_of_names:
                qry="select * from employee where name=%s;"
                val=(name,)
                cursor.execute(qry,val)
                for i in cursor:
                    print(i) 
            else:
                print("Enter a valid name")
            break 
def update_employee():
    list_of_ids=ids()
    while True:
        print("Do you want:\n1.update name\n2.update department\n3.update position\n4.update salary")
        choice=input("enter choice(1-4): ")
        if choice.isdigit():
            choice=int(choice)
            if 1<=choice<=4:
                break
            else:
                print("invalid")
        else:
            print("enter a number")
    if choice==1:
        upd_name=input("enter name to update: ")
        list_of_ids=ids()
        while True:
            id=input("enter id: ")
            
            if id.isdigit():
                id=int(id)
                if id in list_of_ids:
                    break
                else:
                    print("ID not exist")
            else:
                print("enter a valid id")
        qry="update employee set name=%s where id=%s"
        val=(upd_name,id)
        cursor.execute(qry,val)
        mydb.commit()
        print("record updated")
    if choice==2:
        upd_dep=input("enter department to update: ")
        list_of_ids=ids()
        while True:
            id=input("enter id: ")
            
            if id.isdigit():
                id=int(id)
                if id in list_of_ids:
                    break
                else:
                    print("ID not exist")
            else:
                print("enter a valid id")
        qry="update employee set department=%s where id=%s"
        val=(upd_dep,id)
        cursor.execute(qry,val)
        mydb.commit()
        print("record updated")
    if choice==3:
        upd_pos=input("enter name to update: ")
        list_of_ids=ids()
        while True:
            id=input("enter id: ")
            
            if id.isdigit():
                id=int(id)
                if id in list_of_ids:
                    break
                else:
                    print("ID not exist")
            else:
                print("enter a valid id")
        qry="update employee set position=%s where id=%s"
        val=(upd_pos,id)
        cursor.execute(qry,val)
        mydb.commit()
        print("record updated")
    if choice==4:
        upd_salary=int(input("enter salary to update: "))
        list_of_ids=ids()
        while True:
            id=input("enter id: ")
            
            if id.isdigit():
                id=int(id)
                if id in list_of_ids:
                    break
                else:
                    print("ID not exist")
            else:
                print("enter a valid id")
        qry="update employee set salary=%s where id=%s"
        val=(upd_salary,id)
        cursor.execute(qry,val)
        mydb.commit()
        print("record updated")

    
            


def main():
    print("1.add employee.\n2.update employee details.\n3.delete records.\n4.select records")
        
    while True:
        choice=input("enter the choice(1-4):")
        if choice.isdigit():
            choice=int(choice)
            if 1<=choice<=4:
                break
            else:
                print("invalid")
        else:
            print("enter a number between(1-2)")
    if choice==1:
        add_employee()
    elif choice==2:
        update_employee()
    elif choice==3:
        delete_records()
    elif choice==4:
        search_records() 

main()

'''qry="select * from employee"
cursor.execute(qry)
result=cursor.fetchall()
for i in result:
    print(i)'''
    
           




    

    

    

