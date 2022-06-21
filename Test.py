def start():
    print("-----Welcome to SchoolTingsFrFr-----")
    key = str(input("Input Any Key: "))

    if key == "admin":
        admin()

    else:
        customer()

def customer():
    mainMenu()

def mainMenu():
    print("-----Main Menu-----")
    print("1. Catalog \n2. Basket \n3. Cancel")
    try:
        menu_choice = int(input("Input the number of choice"))
    except ValueError:
        print("Input must be a number")
        mainMenu()

    if menu_choice == 1:
         catalog()
    elif menu_choice == 2:
         basket()
    elif menu_choice == 3:
         cancel()
    else:
        print("Not on the list")
        mainMenu()

def catalog():

    print("lalabas yung catalog dito")

    buy_YN = str(input("Are you gonna buy? (Y/N): "))

    if buy_YN == "y" or buy_YN == "Y":
        buyersMenu()
    elif buy_YN == "n" or buy_YN == "N":
        cancel()
    else:
        print("Input must be letter Y or N")
        catalog()

def basket():

    print("lalabas yung laman ng basket") #AAYUSIN PA TO
    print("Lalabas yung total dito")

    remove_YN = str(input("Remove an item? (Y/N): "))

    if remove_YN == "y" or remove_YN == "Y":
        removeItem()
    elif remove_YN == "n" or remove_YN == "N":
        checkOut_YN = str(input("Checking out? (Y/N): "))
        if checkOut_YN == "y" or checkOut_YN == "Y":
            checkOut()
        elif checkOut_YN == "n" or checkOut_YN == "N":
            buyerMenu()
        else:
            print("Input must be letter Y or N")
            basket()
    else:
        print("Input must be letter Y or N")
        basket()

def cancel():
    print("Thank your for coming!")

def buyersMenu():
    print("-----Buyer's Menu-----")
    print("1. Add Item \n2. Basket \n3. Cancel")

    try:
        menu_choice = int(input("Input the number of choice"))
    except ValueError:
        print("Input must be a number")
        mainMenu()

    if menu_choice == 1:
         addItem()
    elif menu_choice == 2:
         basket()
    elif menu_choice == 3:
         cancel()
    else:
        print("Not on the list")
        buyersMenu()

def addItem():

    print("babasahin yung file") #AAYUSIN PA TO
    print("papakita yung laman ng file")

    print("Add Items to basket")
    itemCode = int(input("Input item code"))
    print("madadagdag yung item sa basket")
    add_YN = str(input("Add again? (Y/N): "))

    if add_YN == "y" or add_YN == "Y":
        addItem()
    else:
        basket()

def removeItem():

    print("laman ng basket") #AAYUSIN PA TO
    print("remove from basket?")

    itemName = str(input("Input item name: "))
    itemQuantity = int(input("Input quantity: "))

    print("Matatangal yung item na sinulat with the quantity") #AAYUSIN PA TO

    remove_YN = str(input("Remove again? (Y/N): "))

    if remove_YN == "y" or remove_YN == "Y":
        removeItem()
    else:
        basket()

def checkOut():

    print("Content ng basket") #AAYUSIN PA TO
    print("Yung Total")

    amount = int(input("Please pay amount: "))
    print("Yung change from total")

    print("Mag uupdate yung file") #AAYUSIN PA TO

    purchase_YN = str(input("Make another purchase? (Y/N): "))

    if purchase_YN == "y" or purchase_YN == "Y":
        mainMenu()

    else:
        print("Thank you for your patronage")

# --------------------------- Admin ------------------------------

def admin():
    login()

def login():
    print("-----SchoolTingsFrFr Log-In-----")
    username = str(input("Username: "))
    password = str(input("Password: "))

    if username == "AdminEli" and password == "Eli1234":
        setting()
    elif username == "AdminMigs" and password == "Migs1234":
        setting()
    elif username == "AdminBri" and password == "Bri1234":
        setting()
    else:
        try_YN = str(input("Login incorrect, try again? (Y/N)"))

        if try_YN == "y" or try_YN == "Y":
            login()
        else:
            start()

def setting():
    print("-----Settings-----")
    print("1. Check Stocks \n2. Edit Stocks \n3. Return to start")

    try:
        setting_choice = int(input("Input the number of choice"))
    except ValueError:
        print("Input must be a number")
        setting()

    if setting_choice == 1:
         stocks()
    elif setting_choice == 2:
         editStocks()
    elif setting_choice == 3:
         start()
    else:
        print("Not on the list, input number in the list")
        setting()

def stocks():

    print("Babasahin yung File")
    print("papakita yung laman ng file")

    filler = str(input("Input any key to continue"))

    if filler == "SpongeBobNaCircle":
        print("You found an Easter Egg")
    else:
        setting()

def editStocks():
    print("-----Edit Menu-----")
    print("1. Add Items \n2. Remove Items \n3. Change Price \n4.Return to settings")

    try:
        edit_choice = int(input("Input the number of choice"))
    except ValueError:
        print("Input must be a number")
        editStocks()

    if edit_choice == 1:
         adminAdd()
    elif edit_choice == 2:
         adminRemove
    elif edit_choice == 3:
         adminChange()
    else:
        print("Not on the list, input number in the list")
        setting()

def adminAdd():

    print("basahin yung file")

    print("Input yung item name quantity tsaka price")

    print("madadagdag sa file yung new item")

    adminAdd_YN = str(input("Add another item? (Y/N)"))

    if adminAdd_YN == "y" or adminAdd_YN == "Y":
        adminAdd()
    else:
        setting()

def adminRemove():

    print("basahin yung file")

    print("Input yung item name quantity tsaka price")

    print("matatangal sa file yung inputted item")

    adminRemove_YN = str(input("Remove another item? (Y/N)"))

    if adminRemove_YN == "y" or adminRemove_YN == "Y":
        adminRemove()
    else:
        setting()

def adminChange():

    print("basahin yung file")

    print("Input yung item code at new price")

    print("papalitan yung price nung nung item")

    adminChange_YN = str(input("Change another item? (Y/N)"))

    if adminChange_YN == "y" or adminChange_YN == "Y":
        adminChange()
    else:
        setting()

start()
