import mysql.connector as ms
mycon = ms.connect(host = "localhost",user = "root",passwd = "welcome" ,database="emp")
if mycon.is_connected():
    print("Python connected to Sql")
cursor = mycon.cursor()
def intro():
    print("Enter 1 to access Emp database, Enter 2 to access Client database, Enter 3 to access restaurant ")
    z = int(input("Enter which database should be accessed "))
    if z == 1:
        emp()
    elif z ==2:
        client()
    elif z==3:
        menu_choosing()
    else:
        print("Invalid Database")
def u(t,x):
    sql = "select expenses from hotelc where roomno = {}".format(x)
    cursor.execute(sql)
    mydata = cursor.fetchall()
    z = mydata[0]
    tp = list(z)
    hp = z[0]
    n = t + hp
    cursor.execute("update hotelc set expenses = {} where roomno = {}".format(n,x))
    cursor.execute("Select*from hotelc")
    data = cursor.fetchall()
    for i in data:
         print(i)
# Employee Data
def emp():
    print("WELCOME TO THE HOTEL DATABASE MANAGMENT SYSTEM")
    cursor.execute("Select*from hotel")
    mydata = cursor.fetchall()
    for i in mydata:
        print("id:",i[0],"name:",i[1],"department:",i[2],"salary:",i[3])
    def update():
        x = int(input("Enter emp id whose salary is to be changed : "))
        n = int(input("Enter updated salary: "))
        cursor.execute("update hotel set salary = {} where empid = {}".format(n,x))
        cursor.execute("Select*from hotel")
        data = cursor.fetchall()
        for i in data:
            print("id:",i[0],"name:",i[1],"department:",i[2],"salary:",i[3])
    def delete():
        y = int(input("Enter emp id whose record is to be deleted : "))
        cursor.execute("delete from hotel where empid = {}".format(y))
        cursor.execute("Select*from hotel")
        d = cursor.fetchall()
        for i in d:
            print("id:",i[0],"name:",i[1],"department:",i[2],"salary:",i[3])
    def rec():
        ans = "y"
        while ans == "y":
            empid = int(input("Enter emp ID : "))
            Name = str(input("Enter emp Name : "))
            Dept = str(input("Enter emp Department : "))
            salary = int(input("Enter emp Salary : "))
            sql = "insert into hotel values({},'{}','{}',{})".format(empid,Name,Dept,salary)
            cursor.execute(sql)
            mycon.commit()
            print("Record Saved")
            print("Do you want to enter more records")
            ans = str(input("Enter y or n: " ))
            cursor.execute("Select*from hotel")
            mydata = cursor.fetchall()
            for i in mydata:
               print("id:",i[0],"name:",i[1],"department:",i[2],"salary:",i[3])
    def search():
        x = int(input("Empid to search: "))
        sql = "select*from hotel where empid = {}".format(x)
        cursor.execute(sql)
        d = cursor.fetchall()
        for i in d:
            print("id:",i[0],"name:",i[1],"department:",i[2],"salary:",i[3])
    #def constraint():
        #x = input("insert letters in name ")
        #sql = "select*from school where name like '{}'%".format(x)
        #cursor.execute(sql)
        #d = cursor.fetchall()
        #for i in d:
            #print(i)
    tur = "yes"
    while tur == "yes":
        print("To update record enter - 1, To delete record enter - 2, To enter more records - 3, To search a record - 4 , To exit - 5")
        hjkl = int(input("Enter number: "))
        if hjkl == 1:
            update()
        elif hjkl == 2:
            delete()
        elif hjkl == 3:
            rec()
        elif hjkl == 4:
            search()
        elif hjkl ==5:
            intro()
        else:
            print("Invalid Operation")
        tur = input("Continue operation. Enter yes to continue")
#client data
def client():
    print("WELCOME TO THE HOTEL CUSTOMER DATABASE MANAGMENT SYSTEM")
    cursor.execute("Select*from hotelc")
    mydata = cursor.fetchall()
    for i in mydata:
       print("roomno:",i[0],"name:",i[1],"duration of stay:",i[2],"expeses:",i[3])
    #here we will update the expenses whenevr the client order something
    def update():
            x = int(input("Enter client room number  whose expense is to be changed : "))
            n = int(input("Enter updated expenses: "))
            cursor.execute("update hotelc set expenses = {} where roomno = {}".format(n,x))
            cursor.execute("Select*from hotelc")
            data = cursor.fetchall()
            for i in data:
                print("roomno:",i[0],"name:",i[1],"duration of stay:",i[2],"expeses:",i[3])
    def rec():
        ans = "y"
        while ans == "y":
            roomno = int(input("Enter client roomno : "))
            Name = str(input("Enter client Name : "))
            durationofstay = str(input("Enter Cleint Stay duration : "))
            roomprice = int(input("Enter Client Room Price : "))
            expenses = int(input("Enter client expenses : "))
            sql = "insert into hotelc values({},'{}','{}',{},{})".format(roomno,Name,durationofstay,roomprice,expenses)
            cursor.execute(sql)
            mycon.commit()
            print("Record Saved")
            print("Do you want to enter more records")
            ans = str(input("Enter y or n: " ))
        cursor.execute("Select*from hotelc")
        mydata = cursor.fetchall()
        for i in mydata:
            print("roomno:",i[0],"name:",i[1],"duration of stay:",i[2],"expeses:",i[3])
    def search():
        x = int(input("cleint roomno to search: "))
        sql = "select*from hotelc where roomno = {}".format(x)
        cursor.execute(sql)
        d = cursor.fetchall()
        for i in d:
            print("roomno:",i[0],"name:",i[1],"duration of stay:",i[2],"expeses:",i[3])
    #def constraint():
        #x = input("insert letters in name ")
        #sql = "select*from school where name like '{}'%".format(x)
        #cursor.execute(sql)
        #d = cursor.fetchall()
        #for i in d:
            #print(i)
    tur = "yes"
    while tur == "yes":
        print("To update record enter - 1, To enter more records - 3, To search a record - 4, To exit - 5 ")
        hjkl = int(input("Enter number: "))
        if hjkl == 1:
            update()
        elif hjkl == 3:
            rec()
        elif hjkl == 4:
            search()
        elif hjkl ==5:
            intro()
        else:
            print("Invalid Operation")
        tur = input("Continue operation. Enter yes to continue")
#restaurant ordering and billing module
def menu_choosing():
    def instre():
        print("Press 1 to order the food item and quantity")
        print("Press 2 to exit")
    print("-"*80)
    cursor.execute("select*from menu")
    mydata = cursor.fetchall()
    for i in mydata:
        print(i)
    ans="y"
    while ans!="n":
        instre()
        option1=int(input("..."))
        if option1==1:
            item_list=[]
            itans="y"
            bill=0
            while itans=="y":
                    x=int(input("What food item would you like to buy?(write the food item code here)"))
                    quant=int(input("What quantity of it do you want?"))
                    sql = "select price from menu where id = {}".format(x)
                    cursor.execute(sql)
                    mydata = cursor.fetchall()
                    z = mydata[0]
                    tp = list(z)
                    hp = z[0]
                    bill = bill + hp*quant
                    itans = input("Want to order more:")
            print("your total bill is ",bill)
            print("Would you like to pay now or later?")
            print("Enter 1 to pay now and enter 2 to pay later")
            ghty = int(input("Enter"))
            if ghty ==1:
                print('Your transaction has successfully completed')
            if ghty ==2:
                print('This has been added to your expenses')
                hytr = int(input("Please enter your room number"))
                u(bill,hytr)
        elif option1 == 2:
            intro()
intro()


                    
