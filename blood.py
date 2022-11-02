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
    print("6 total units of blood")
    print("7 name the donor with place")


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
        sql = 'SELECT * FROM `donors`'
        mycursor.execute(sql)
        result =  mycursor.fetchall()
        for i in result:
            print(i) 

    elif(choice==3):
        print("search donor selected")

        bloodgroup = input("enter the bloogroup: ")
        sql = "SELECT `id`, `name`,`bloodgroup`, `unit`, `phone`, `place` FROM `donors` WHERE `bloodgroup` ='" +bloodgroup+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)


    elif(choice==4):
        print("update donor selected")
        name = input("enter the name")
        bloodgroup = input("enter the bloodgroup to be updated")
        unit = input("enter the unit to be updated ")
        phone = input("enter the number to be updated")
        place = input("enter the place to be updated")
        sql = "UPDATE `donors` SET `bloodgroup`='"+bloodgroup+"',`unit`='"+unit+"',`phone`='"+phone+"',`place`='"+place+"' WHERE `name`='"+name+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("updated succusfully")

    elif(choice==5):
        print("delete donor selected")
        bloodgroup = input("enter the bloodgroup: ")
        sql = "DELETE FROM `donors` WHERE `bloodgroup` ='"+bloodgroup+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("data deleted successfully")

    elif(choice==6):
         print(" total unit blood")
         sql = "SELECT SUM(`unit`) FROM `donors`"
         mycursor.execute(sql)
         result = mycursor.fetchall()
         print(result)


    elif(choice==7):
        break
