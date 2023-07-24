import mysql.connector as mys
mycon = mys.connect(host='localhost',user='root',passwd='welcome')

mycursor = mycon.cursor()

mycursor.execute("USE restaurant")

def aboutus():
    
    print("About Us")
    
    print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit,
          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
          ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
          voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
          sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")

    print('\n')
    print('Press the enter key to go back')
    
    back = input()
    if back == '':
        mainmenu()

def menu():
    
    print("Menu")

    print("To view Soups    : Press 1")
    print("To view Salads   : Press 2")
    print("To view Pasta    : Press 3")
    print("To view Pizza    : Press 4")
    print("To view Smoothies: Press 5")
    print("To view Deserts  : Press 6")

    print("To go back       : Press 7")


    ans = int(input())

    if ans == 1:
        mycursor.execute("select * from Soups")
        mydata = mycursor.fetchall()
        print('\n')
        for row in mydata:
            print(row)
        print('\n')
        print('Press the enter key to go back')
        back = input()
        if back == '':
            menu()
            

    if ans == 2:
        mycursor.execute("select * from Salads")
        mydata = mycursor.fetchall()
        print('\n')
        for row in mydata:
            print(row)
        print('\n')
        print('Press the enter key to go back')
        back = input()
        if back == '':
            menu()

    if ans == 3:
        mycursor.execute("select * from Pasta")
        mydata = mycursor.fetchall()
        print('\n')
        for row in mydata:
            print(row)
        print('\n')
        print('Press the enter key to go back')
        back = input()
        if back == '':
            menu()

    if ans == 4:
        mycursor.execute("select * from Pizza")
        mydata = mycursor.fetchall()
        print('\n')
        for row in mydata:
            print(row)
        print('\n')
        print('Press the enter key to go back')
        back = input()
        if back == '':
            menu()

    if ans == 5:
        mycursor.execute("select * from Smoothies")
        mydata = mycursor.fetchall()
        print('\n')
        for row in mydata:
            print(row)
        print('\n')
        print('Press the enter key to go back')
        back = input()
        if back == '':
            menu()

    if ans == 6:
        mycursor.execute("select * from Deserts")
        mydata = mycursor.fetchall()
        print('\n')
        for row in mydata:
            print(row)
        print('\n')
        print('Press the enter key to go back')
        back = input()
        if back == '':
            menu()

    if ans == 7:
        print('\n')
        print(mainmenu())

def order(name,date):

    print("Order for Delivery: ")


    print("To Order in New York      : Press 1")
    print("To Order in Paris         : Press 2")
    print("To Order in Mumbai        : Press 3")
    print("To Order in Tokyo         : Press 4")
    print("To view your past orders  : Press 5")
  

    ans = int(input())
    if ans in (1,2,3,4):
        order1(ans,name,date)
    if ans == 5:
        order2(name)


def order1(n,name,date):
    
    restaurant = ('New York','Paris','Mumbai','Tokyo')
    place = restaurant[n-1]
    print("Menu")

    print("To view Soups    : Press 1")
    print("To view Salads   : Press 2")
    print("To view Pasta    : Press 3")
    print("To view Pizza    : Press 4")
    print("To view Smoothies: Press 5")
    print("To view Deserts  : Press 6")

    print("To go back       : Press 7")


    ans = int(input())

    if ans == 1:
        mycursor.execute("select * from Soups")
        mydata = mycursor.fetchall()
        print('\n')
        for row in mydata:
            print(row)
        print('\n')
        print('Enter the itemno that you wish to order, or 0 to go back')
        item = int(input())
        if item == 0:
            order1(n,name,date)
        else:
            while item != 0:
                mycursor.execute("select * from menu")
                mydata = mycursor.fetchall()
                for i in mydata:
                        if i[0] == item:
                            dish = i[1] 
                            price = i[2]
                mycursor.execute("insert into orders values('{}','{}','{}',{},'{}')".format(place,name,dish,price,date))
                mycon.commit()
                item = int(input("Enter the item no you wish to order or 0 if the order is complete: "))
            order1(n,name,date)

            

    if ans == 2:
        mycursor.execute("select * from Salads")
        mydata = mycursor.fetchall()
        print('\n')
        for row in mydata:
            print(row)
        print('\n')
        print('Enter the itemno that you wish to order, or 0 to go back')
        item = int(input())
        if item == 0:
            order1(n,name,date)
        else:
            while item != 0:
                mycursor.execute("select * from menu")
                mydata = mycursor.fetchall()
                for i in mydata:
                        if i[0] == item:
                            dish = i[1] 
                            price = i[2]
                mycursor.execute("insert into orders values('{}','{}','{}',{},'{}')".format(place,name,dish,price,date))
                mycon.commit()
                item = int(input("Enter the item no you wish to order or 0 if the order is complete: "))
            order1(n,name,date)
            
    if ans == 3:
        mycursor.execute("select * from Pasta")
        mydata = mycursor.fetchall()
        print('\n')
        for row in mydata:
            print(row)
        print('\n')
        print('Enter the itemno that you wish to order, or 0 to go back')
        item = int(input())
        if item == 0:
            order1(n,name,date)
        else:
            while item != 0:
                mycursor.execute("select * from menu")
                mydata = mycursor.fetchall()
                for i in mydata:
                        if i[0] == item:
                            dish = i[1] 
                            price = i[2]
                mycursor.execute("insert into orders values('{}','{}','{}',{},'{}')".format(place,name,dish,price,date))
                mycon.commit()
                item = int(input("Enter the item no you wish to order or 0 if the order is complete: "))
            order1(n,name,date)
            
    if ans == 4:
        mycursor.execute("select * from Pizza")
        mydata = mycursor.fetchall()
        print('\n')
        for row in mydata:
            print(row)
        print('\n')
        print('Enter the itemno that you wish to order, or 0 to go back')
        item = int(input())
        if item == 0:
            order1(n,name,date)
        else:
            while item != 0:
                mycursor.execute("select * from menu")
                mydata = mycursor.fetchall()
                for i in mydata:
                        if i[0] == item:
                            dish = i[1] 
                            price = i[2]
                mycursor.execute("insert into orders values('{}','{}','{}',{},'{}')".format(place,name,dish,price,date))
                mycon.commit()
                item = int(input("Enter the item no you wish to order or 0 if the order is complete: "))
            order1(n,name,date)
            

    if ans == 5:
        mycursor.execute("select * from Smoothies")
        mydata = mycursor.fetchall()
        print('\n')
        for row in mydata:
            print(row)
        print('\n')
        print('Enter the itemno that you wish to order, or 0 to go back')
        item = int(input())
        if item == 0:
            order1(n,name,date)
        else:
            while item != 0:
                mycursor.execute("select * from menu")
                mydata = mycursor.fetchall()
                for i in mydata:
                        if i[0] == item:
                            dish = i[1] 
                            price = i[2]
                mycursor.execute("insert into orders values('{}','{}','{}',{},'{}')".format(place,name,dish,price,date))
                mycon.commit()
                item = int(input("Enter the item no you wish to order or 0 if the order is complete: "))
            order1(n,name,date)
            

    if ans == 6:
        mycursor.execute("select * from Deserts")
        mydata = mycursor.fetchall()
        print('\n')
        for row in mydata:
            print(row)
        print('\n')
        print('Enter the itemno that you wish to order, or 0 to go back')
        item = int(input())
        if item == 0:
            order1(n,name,date)
        else:
            while item != 0:
                mycursor.execute("select * from menu")
                mydata = mycursor.fetchall()
                for i in mydata:
                        if i[0] == item:
                            dish = i[1] 
                            price = i[2]
                mycursor.execute("insert into orders values('{}','{}','{}',{},'{}')".format(place,name,dish,price,date))
                mycon.commit()
                item = int(input("Enter the item no you wish to order or 0 if the order is complete: "))
            order1(n,name,date)

    if ans == 7:
        print('\n')
        bill(name,date)
        print(order(name,date))



def order2(name):   
    mycursor.execute("select * from orders where name = '%s'"%(name,))
    mydata = mycursor.fetchall()

    print('Item                 Price      Date')

    for row in mydata:
        print(row[2],row[3],row[4])

def bill(name,date):
        mycursor.execute("select item, price from orders where name = '{}' and date = '{}'".format(name,date))
        mydata = mycursor.fetchall()
        a = 0
        for i in mydata:
            print(i)
            a += i[1]
        print("The Total cost is: ",a)
        print('\n')
        print('\n')


def reserve():

    print("Reserve a Table")
    
    print("To Reserve a table in New York  : Press 1")
    print("To Reserve a table in Paris     : Press 2")
    print("To Reserve a table in Mumbai    : Press 3")
    print("To Reserve a table in Tokyo     : Press 4")

    print("To view your reservations       : Press 5")
    print("To cancel your reservation      : Press 6")
    
    print("To go back                      : Press 7")

    ans = int(input())
    restaurant = ('New York','Paris','Mumbai','Tokyo')

    if ans in (1,2,3,4):
        name = input("Enter your name: ")
        number = int(input("Enter the number of people: "))
        time = input("Enter the time (example: 09:30, 18:45 etc.): ")
        date = input("Enter the date in the form DD/MM/YYYY: ")

        place = restaurant[ans-1]

        mycursor.execute("INSERT INTO RESERVATIONS VALUES('{}','{}',{},'{}','{}')".format(place,name,number,time,date))
        mycon.commit()
        print('\n')
        print('Table Reserved!')
        print('\n')

        reserve()

    if ans == 5:
        name = input("Enter name: ")
        mycursor.execute("select * from reservations")
        mydata = mycursor.fetchall()
        print('place,name,number,time,date')
        for row in mydata:
            if row[1] == name:
                print(row)

        print('\n')
        reserve()


    if ans == 6:
        name = input("Enter name: ")
        mycursor.execute("DELETE FROM reservations WHERE name ='%s'"%(name,))
        mycon.commit()

        print('\n')
        print('Reservation Cancelled!')
        print('\n')

        reserve()

    if ans == 7:
        mainmenu()


def mainmenu():

    print("Greetings!!!")
    
    print("To view 'About Us': Press 1")
    print("To view 'Menu': Press 2")
    print("To view 'Order Delivery': Press 3")
    print("To view 'Make a Reservation': Press 4")

    print("To exit Program: Press 5")
    
    
    ans = int(input())

    if ans == 1:
        print(aboutus())

    if ans == 2:
        print(menu())

    if ans == 3:
        name = input("Enter your name: ")
        date = input("Enter date in the form DD/MM/YYYY: ")
        print(order(name,date))

    if ans == 4:
        print(reserve())

    if ans == 5:
        exit()

mainmenu()
