
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
