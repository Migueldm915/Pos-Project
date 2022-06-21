import os

def start():
    catalog = readCatalog()


    print("""
=======================================================================================================================
    
███████╗ ██████╗██╗  ██╗ ██████╗  ██████╗ ██╗  ████████╗██╗███╗   ██╗ ██████╗ ███████╗███████╗██████╗ ███████╗██████╗ 
██╔════╝██╔════╝██║  ██║██╔═══██╗██╔═══██╗██║  ╚══██╔══╝██║████╗  ██║██╔════╝ ██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗
███████╗██║     ███████║██║   ██║██║   ██║██║     ██║   ██║██╔██╗ ██║██║  ███╗███████╗█████╗  ██████╔╝█████╗  ██████╔╝
╚════██║██║     ██╔══██║██║   ██║██║   ██║██║     ██║   ██║██║╚██╗██║██║   ██║╚════██║██╔══╝  ██╔══██╗██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████╗██║   ██║██║ ╚████║╚██████╔╝███████║██║     ██║  ██║██║     ██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝                                                                                                                 
            
=======================================================================================================================       
            """)

    key = str(input("Input Any Key: "))

    if key == "admin":
        admin(catalog)

    else:
        customer(catalog)

def customer(catalog):
    cart = dict()
    cartCounter = 0
    mainMenu(catalog, cart, cartCounter)


def mainMenu(catalog, cart, cartCounter):

    print("""
===============================
    
========== Main Menu ==========
    
===============================
 """)

    print("1. Catalog \n2. Basket \n3. Cancel\n")
    try:
        menu_choice = int(input("Input the number of choice: "))
    except ValueError:
        print("Input must be a number")
        mainMenu()

    if menu_choice == 1:
         showCatalog(catalog, cart, cartCounter)
    elif menu_choice == 2:
         basket(catalog, cart, cartCounter)
    elif menu_choice == 3:
         cancel()
    else:
        print("Not on the list")
        mainMenu()

def showCatalog(catalog, cart, cartCounter):

    print("=== Item List ===")
    viewCatalog(catalog)

    buy_YN = str(input("Are you gonna buy? (Y/N): "))

    if buy_YN == "y" or buy_YN == "Y":
        buyersMenu(catalog, cart, cartCounter)
    elif buy_YN == "n" or buy_YN == "N":
        cancel()
    else:
        print("Input must be letter Y or N")
        showCatalog(catalog, cart, cartCounter)

def cancel():
    print("Thank your for coming!")

def buyersMenu(catalog, cart, cartCounter):
    print("-----Buyer's Menu-----")
    print("1. Add Item \n2. Basket \n3. Cancel")

    try:
        menu_choice = int(input("Input the number of choice: "))
    except ValueError:
        print("Input must be a number")
        mainMenu(catalog, cart, cartCounter)

    if menu_choice == 1:
         addItem(catalog, cart, cartCounter)
    elif menu_choice == 2:
         basket(catalog, cart, cartCounter)
    elif menu_choice == 3:
         cancel()
    else:
        print("Not on the list")
        buyersMenu(catalog, cart, cartCounter)

def addItem(catalog, cart, cartCounter):

    viewCatalog(catalog)

    print("Add Items to basket")
    itemCode = int(input("Input item code: "))

    try:
        item = catalog[itemCode]["num"]
        price = catalog[itemCode]["price"]
        cart[cartCounter + 1] = {"price":price, "key":item, "item_code": itemCode}
        cartCounter += 1

    except KeyError:
        print("Item code not in catalog")

    add_YN = str(input("Add again? (Y/N): "))

    if add_YN == "y" or add_YN == "Y":
        addItem(catalog, cart, cartCounter)
    else:
        basket(catalog, cart, cartCounter)

def removeItem(catalog, cart, cartCounter):

    viewCart(catalog, cart)
    print("remove from basket?")

    itemCode = int(input("Input item code: "))
    cart.pop(itemCode)

    viewCart(catalog, cart)

    remove_YN = str(input("Remove again? (Y/N): "))

    if remove_YN == "y" or remove_YN == "Y":
        removeItem(catalog, cart, cartCounter)
    else:
        basket(catalog, cart, cartCounter)

def basket(catalog, cart, cartCounter):

    viewCart(catalog, cart)

    remove_YN = str(input("Remove an item? (Y/N): "))

    if remove_YN == "y" or remove_YN == "Y":
        removeItem(catalog, cart, cartCounter)
    elif remove_YN == "n" or remove_YN == "N":
        checkOut_YN = str(input("Checking out? (Y/N): "))
        if checkOut_YN == "y" or checkOut_YN == "Y":
            checkOut(catalog, cart, cartCounter)
        elif checkOut_YN == "n" or checkOut_YN == "N":
            buyersMenu(catalog, cart, cartCounter)
        else:
            print("Input must be letter Y or N")
            basket(catalog, cart, cartCounter)
    else:
        print("Input must be letter Y or N")
        basket(catalog, cart, cartCounter)

def checkOut(catalog, cart, cartCounter):
    total = 0
    viewCart(catalog, cart)
    for items in cart.items():
        key = items[1]['key']
        cartItem = cart[key]
        cartPrice = cartItem["price"]
        cartItemCode = cartItem["item_code"]
        currentCatalogItemQty = catalog[cartItemCode]["qty"]
        catalog[cartItemCode]["qty"] = currentCatalogItemQty - 1
        total += int(cartPrice)

    print(f"The total is {total} Php.")

    amount = int(input("Please pay amount: "))
    change = 0
    if amount >= total:
        change = amount - total
        updateCatalog(catalog)
        print(f"Your change is {change} Php")

    else:
        print("insufficient amount")
        checkOut(catalog, cart, cartCounter)


    purchase_YN = str(input("Make another purchase? (Y/N): "))

    if purchase_YN == "y" or purchase_YN == "Y":
        mainMenu(catalog, cart, cartCounter)

    else:
        print("Thank you for your patronage")

# --------------------------- Admin ------------------------------

def admin(catalog):
    login(catalog)

def login(catalog):
    print("-----SchoolTingsFrFr Log-In-----")
    username = str(input("Username: "))
    password = str(input("Password: "))

    if username == "AdminEli" and password == "Eli1234":
        setting(catalog)
    elif username == "AdminMigs" and password == "Migs1234":
        setting(catalog)
    elif username == "AdminBri" and password == "Bri1234":
        setting(catalog)
    else:
        try_YN = str(input("Login incorrect, try again? (Y/N)"))

        if try_YN == "y" or try_YN == "Y":
            login()
        else:
            start()

def setting(catalog):
    print("-----Settings-----")
    print("1. Check Stocks \n2. Edit Stocks \n3. Return to start")

    try:
        setting_choice = int(input("Input the number of choice"))
    except ValueError:
        print("Input must be a number")
        setting()

    if setting_choice == 1:
         stocks(catalog)
    elif setting_choice == 2:
         editStocks(catalog)
    elif setting_choice == 3:
         start()
    else:
        print("Not on the list, input number in the list")
        setting(catalog)

def stocks(catalog):

    viewCatalog(catalog)

    filler = str(input("Input any key to continue"))

    if filler == "SpongeBobNaCircle":
        print("You found an Easter Egg")
    else:
        setting(catalog)

def editStocks(catalog):
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
         adminRemove(catalog)
    elif edit_choice == 3:
         adminChange(catalog)
    else:
        print("Not on the list, input number in the list")
        setting()

def adminAdd():

    file = open("catalog.txt")
    check = file.readlines()
    file.close()

    file = open("catalog.txt")
    catalog = file.read()
    file.close()

    print(catalog)

    print("Item adder")

    itemName = str(input("Input Item Name: "))
    itemPrice = str(input("Input Item Price: "))
    itemStock = str(input("Input Item stock amount: "))


    nProduct = catalog + f"\n{len(check)+1},{itemPrice},{itemName},{itemStock}"

    file = open("catalog.txt", 'w')
    file.write(nProduct)
    file.close()

    adminAdd_YN = str(input("Add another item? (Y/N)"))

    if adminAdd_YN == "y" or adminAdd_YN == "Y":
        adminAdd()
    else:
        setting(catalog)

def adminRemove(catalog):

    viewCatalog(catalog)

    file = open("catalog.txt")
    catalog = file.readlines()
    file.close()

    remove= int(input("Input Code"))
    catalog.pop(remove - 1)
    
    parsed = map(parse, catalog)
    parsedCatalog = catalogFromParsed(parsed)

    newKey = 1
    newCatalogDict = dict()

    for itemTuple in parsedCatalog.items():
        item = itemTuple[1]
        item["num"] = newKey
        newCatalogDict[newKey] = item
        newKey+=1

    updateCatalog(newCatalogDict)

    adminRemove_YN = str(input("Remove another item? (Y/N)"))

    if adminRemove_YN == "y" or adminRemove_YN == "Y":
        adminRemove(newCatalogDict)
    else:
        setting(newCatalogDict)

def adminChange(catalog):

    viewCatalog(catalog)

    proCode = int(input("Input Item Code to change price: "))
    newPrice = int(input("Input new price of item: "))

    newCatalog = changePrice(catalog, proCode, newPrice)

    productDictionaryList = newCatalog.items()
    productList = map(productToString, productDictionaryList)
    openMe = open('catalog.txt', "w+")
    openMe.writelines(productList)
    openMe.close()

    adminChange_YN = str(input("Change another item? (Y/N)"))

    if adminChange_YN == "y" or adminChange_YN == "Y":
        adminChange(catalog)
    else:
        setting(catalog)

def parse(string):
    test = string.strip().split(",")
    num = int(test[0])
    price = int(test[1])
    item = test[2]
    qty = int(test[3])

    productDict = dict()
    productDict["num"] = num
    productDict["qty"] = qty
    productDict["item"] = item
    productDict["price"] = price
    return productDict

def changePrice(catalog, key, price):
    productDict = catalog[key]
    productDict["price"] = price
    catalog[key] = productDict
    return catalog

def productToString(productDictTuple):
    productDict = productDictTuple[1]
    qty = productDict["qty"]
    name = productDict["item"]
    price = productDict["price"]
    num = productDict["num"]
    return str(num) + "," + str(price) + "," + name + "," + str(qty) + "\n"

def readCatalog():
    openMe = open('catalog.txt')
    text = openMe.readlines()
    openMe.close()
    test = map(parse, text)
    catalog = catalogFromParsed(test)

    return catalog

def catalogFromParsed(parsed):
    catalog = dict()
    for v in parsed:
        catalog[v["num"]] = v
    return catalog


def updateCatalog(newCatalog):
    productDictionaryList = newCatalog.items()
    productList = map(productToString, productDictionaryList)
    openMe = open('catalog.txt', "w+")
    openMe.writelines(productList)
    openMe.close()

def viewCatalog(catalog):
    for itemTuple in catalog.items():
        item = itemTuple[1]
        price = item["price"]
        quantity = item["qty"]
        product = item["item"]
        key = item["num"]
        print(f"{key}.)   {price} Php {product}.      Stock:{quantity}")

def viewCart(catalog, cart):
    for selectedItem in cart.items():
        cartKey = selectedItem[0]
        key = selectedItem[1]['key']
        catalogItem = catalog[key]
        catalogPrice = catalogItem["price"]
        catalogName = catalogItem["item"]

        print(f"{cartKey}.) {catalogPrice}Php {catalogName}")

        
start()
