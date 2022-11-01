import mysql.connector

mydb= mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'bloodbankdb')
mycursor = mydb.cursor()

while True:
    print("select an option from menu")
    print("1 add donor")
    print("2 view all donor")
    print("3 search a donor")
    print("4 update the donor")
    print("5 delete a donor")
    print("6 exit")

    choice = int(input("Enter an option: "))
    if(choice==1):
        print("donor enter selected")

        name = input("enter the name")
        bloodgroup = input("enter the bloodgroup")
        unit = input("enter the unit")
        phone = input("enter the number")
        place = input("enter the place")
        sql = 'INSERT INTO `donors`(`name`, `bloodgroup`, `unit`, `phone`, `place`) VALUES (%s,%s,%s,%s,%s)'
        data = (name,bloodgroup,unit,phone,place)
        mycursor.execute(sql , data)
        mydb.commit()
        print("value inserted succesfully")

    elif(choice==2):
        print("view donor selected")
    elif(choice==3):
        print("search donor selected")
    elif(choice==4):
        print("update donor selected")
    elif(choice==5):
        print("delete donor selected")
    elif(choice==6):
        break
