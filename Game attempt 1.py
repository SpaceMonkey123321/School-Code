import csv
def addone():
    f=open('14.csv', 'a')
    writer= csv.writer(f)
    name= input('Enter employee name: ')
    code= int(input("Enter employee code: "))
    age= int(input('Enter employee age: '))
    emp= [name, code, age]
    writer.writerow(emp)
    f.close()
def addmany():
    count= int(input('How many records would you like to add? '))
    employees=[]
    for i in range(count):
    f=open('14.csv', 'a')
    writer= csv.writer(f)
    name= input('Enter employee name: ')
    code= int(input("Enter employee code: "))
    age= int(input('Enter employee age: '))
    emp= [name, code, age]
    employees.append(emp)
    writer.writerows(employees)
    f.close()
def showfile():
    f=open('14.csv', 'r')
    reader= csv.reader(f)
    for i in reader:
    print(i)
    20
while True:
    answer= input("""Add a record(A1)\nAdd multiple Records(ADD)\nShow file(SHOW)\nWhat
    would you like to do with the table employees?""")
    if answer=='A1':
        addone()
    elif answer=='ADD':
        addmany()
    elif answer=='SHOW':
        showfile()



