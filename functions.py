import datetime

def show_welcome_message():
    """prints out a welcome message"""
    
    print("\n+======================================================================+")
    print("\t\tWelcome to Bike Management System\t\t")
    print("+======================================================================+\n")

def show_options():
    """prints out options for choosing """
    
    print("Options:")
    print("+------------------------------------------------+")
    print("\tEnter [1] for displaying bikes")
    print("\tEnter [2] for selling bikes")
    print("\tEnter [3] for ordering new bike \n\t\tand adding stock to current bikes")
    print("\tEnter [4] for exiting the program")
    print("+------------------------------------------------+\n")

def sellingBike():
    """prints out a message indicating the beginning of selling bikes functionality"""
    
    print("\n\n\n+-----------------------------------------------+")
    print("\t\tSelling Bikes\t")
    print("+-----------------------------------------------+\n")

def orderingBike():
    """prints out a message indicating the beginning of ordering bikes and adding new bikes functionality"""
    
    print("\n\n\n+-------------------------------------------------------------------------+")
    print("\t\tOrdering new bikes and adding stock to current bikes\t")
    print("+-------------------------------------------------------------------------+\n")
    
def invalid_input():
    """prints out message indicating invalid message when user gives a invalid input"""
    
    print("\nINVALID INPUT. Please select one of the given options.")
    show_options()

def show_exit_message():
    """prints out message indicating termination of program"""
    
    print("\n+===========================================================================================+")
    print("\t\tThank you for using Bike Management System. Have a great day !\t\t")
    print("+===========================================================================================+\n")

def show_bike_details():
    """prints out details of all the available bikes in the stock"""

    print("\n+-----------------------------------------------+")
    print("\tDisplaying our available bikes\t")
    print("+-----------------------------------------------+")
    print("+-----------------------------------------------------------------------------------------------------------------------+")
    print(f'{"Bike ID":<10}{"Bike Name":<25}{"Bike-Company":<44}{"Color":<20}{"Stock":<10}{"Price(In $)":<10}')
    print("+-----------------------------------------------------------------------------------------------------------------------+")
    bike_ID = 1
    #bikes.txt file is read and each line containing a bike is converted into list and is printed out
    file = open("bikes.txt", "r")
    for line in file:
        value = line.split(",")
        print(f'{bike_ID:<10}{value[0]:<25}{value[1]:<44}{value[2]:<20}{value[3]:<10}{value[4]:<10}')
        bike_ID += 1
    print("+-----------------------------------------------------------------------------------------------------------------------+\n")
    file.close()

def bike_details_as2DList():
    """reads bikes.txt file, converting each line into a list and
        appends that list into another list and returns 2D list"""
    
    file = open("bikes.txt", "r")
    bikeList = []
    #iterating over the file 
    for line in file:
        #replacing \n with empty string and converting into list by splitting each line 
        line = line.replace("\n", "") 
        line = line.split(",")
        #adding into bikeList
        bikeList.append(line)
    file.close()
    return bikeList

def validating_bikeID():
    """takes bike ID as input, validates it and returns that bike ID"""
    
    checking = True
    #using loops for taking user input till a valid bike ID is entered as input
    while checking:
        #using try,except for handling input that would result in error
        try:
            bikeID = int(input("Enter the value of bike ID: "))
            while bikeID <= 0 or bikeID > len(bike_details_as2DList()):
                print("Please enter the valid Bike ID!!!")
                show_bike_details()
                bikeID = int(input("Enter the value of bike ID: "))
            checking = False
        except:
            print("Invalid Bike ID ! Please enter a valid Bike ID\n")
            checking = True
    return bikeID

def validating_quantity(bikeID):
    """takes quantity as input, validates it by comparing with the stock of bike indicated by
            bike ID taken in parameter and returns quantity"""

    
    checking = True
    #using loops for taking user input till a valid quantity is entered as input
    while checking:
        #using try,except for handling input that would result in error
        try:        
            quantity = int(input("Enter the quantity you want to sell: "))
            print("\n")
            stock = bike_details_as2DList()[bikeID - 1][3]
            while quantity < 0 or quantity > int(stock):
                print("\nOut of bounds. Please enter the valid quantity you want to sell.\n")
                show_bike_details()
                quantity = int(input("Please enter the valid quantity you want to sell: "))
                print("\n")
            checking = False
        except:
            print("Invalid quantity. Please enter the valid quantity that need to be sold.\n")
            checking = True
    return quantity

def validating_order_quantity():
    """takes quantity as input, validates it and returns quantity"""
    
    checking = True
    #using loops for taking user input till a valid quantity is entered as input
    while checking:
        #using try,except for handling input that would result in error
        try:
            quantity = int(input("Enter the quantity to be added to the stock: "))
            print("\n")
            while quantity <= 0:
                print("\nOut of bounds. Please enter the valid quantity to be added to the stock.\n")
                quantity = int(input("Enter the quantity to be added to the stock: "))
                print("\n")
            checking = False
        except:
            print("Invalid entry ! Please enter a valid quantity which you want to order.")
            print("\n")
            checking = True
    return quantity


def selling_bike(bike_id, quantity):
    """takes valid bike ID and quantity as parameter and decreases the stock of bike indicated by
           bike ID in 2D list holding bikes and updates the bikes.txt file"""
    
    bikes = bike_details_as2DList()
    bikes[bike_id - 1][3] = int(bikes[bike_id - 1][3]) - quantity
    update_stock(bikes)

def update_stock(list_2D):
    """takes 2D list as parameter and using 2D list,
        rewrites bikes.txt with updated quantity of the bikes"""
    
    file = open("bikes.txt", "w")
    for list_1D in list_2D:
        file.write(str(list_1D[0]) + "," + str(list_1D[1]) + "," +
                   str(list_1D[2]) + "," + str(list_1D[3]) + "," + str(list_1D[4]) + "\n")
    file.close()

def adding_stock(bike_id, quantity):
    """takes valid bike ID and quantity as parameter and increases the stock of bike indicated by
           bike ID in 2D list holding bikes and updates the bikes.txt file"""
    bikes = bike_details_as2DList()
    bikes[bike_id - 1][3] = int(bikes[bike_id - 1][3]) + quantity
    update_stock(bikes)

def return_ordered_bikes():
    """asks details of bikes to be ordered and returns 2D list holding details of ordered bikes in a transaction"""
    bikes = bike_details_as2DList()
    willContinue = True
    bike_data = []
    #using loop to continue to order bikes till user decides to discontinue
    while willContinue:
        show_bike_details()
        #asking for user input whether bike to be added in the stock
        exists = input("Is the bike to be added already in the stock?\nEnter 'yes' if it is already in the stock and 'no' if you want to add a new bike: ")
        print("\n")
        #asking for details of the new bike if not in the stock and updating it to bikes.txt file and 2D list
        if exists.lower() == "no":
            print("New Addition to the stock: ")
            bikeName = input("Name of the bike: ")
            bikeCompany = input("Name of the company of the bike: ")
            bikeColour = input("Enter the colour of the bike: ")
            bikePrice = input("Enter the price of the bike: ")
            bikeQuantity = input("Enter the quantity of the bike: ")
            totalPrice = int(bikePrice) * int(bikeQuantity)
            newBike = [bikeName, bikeCompany, bikeColour, bikeQuantity, bikePrice]
            bikes.append(newBike)
            update_stock(bikes)
            orderedBike = [bikeName, bikeQuantity, bikePrice, bikeCompany, bikeColour, totalPrice]
            bike_data.append(orderedBike)

        #asking for valid bike ID and quantity and updating the stock with increased quantity of bikes
        elif exists.lower() == "yes":
            print("Please provide valid details regarding bikes:")
            bike_ID = validating_bikeID()
            quantity = validating_order_quantity()
            adding_stock(bike_ID, quantity)
            bike_data.append(returnBikesList(bike_ID, quantity))
        else:
            print("Invalid entry ! Please enter valid input.")
            continue
        #asking if user want to continue the ordering
        wantContinue = input("Do you still want to add more?\nEnter 'no' if you want to finish up ordering and any other key for ordering more bikes: ")
        if wantContinue.lower() == "no":
            willContinue = False
    return bike_data

def return_sold_bikes():
    """asks details of bikes to be sold and returns 2D list holding details of sold bikes in a transaction"""
    
    againSale = "yes"
    bike_data = []
    #using loop to continue to sell bikes till user decides to discontinue
    while againSale.lower() == "yes":
        show_bike_details()
        print("Please provide valid details regarding bikes:")
        #asking for valid bike ID and quantity and updating the stock with decreased quantity of bikes
        bikeID = validating_bikeID()
        quantity = validating_quantity(bikeID)
        selling_bike(bikeID, quantity)
        bike_data.append(returnBikesList(bikeID,quantity))
        againSale = input("Enter 'yes' if you want to sell again and any other key for finishing up the sale: ")
    return bike_data        

def returnBikesList(bikeID, quantity):
    """takes bike ID and quantity as parameter, gets and
        stores the details of that specific bike in a list and returns the list"""
    
    bikes = bike_details_as2DList()
    bikeName = bikes[bikeID - 1][0]
    bikeCompany = bikes[bikeID - 1][1]
    bikeColour = bikes[bikeID - 1][2]
    bikeUnitPrice = bikes[bikeID - 1][4]
    totalPrice = int(bikeUnitPrice) * int(quantity)
    bike = [bikeName, quantity, bikeUnitPrice, bikeCompany, bikeColour, totalPrice]
    return bike       

def generating_bills(typeOfTransaction, bikeData, name, location, totalPrice,phone) :
    """takes bikeData list, name, location, totalPrice, typeOfTransaction,phone as
        parameters and uses them to create and write a text file indicating a bill"""
    #generating random name as file name for each new bill
    filename = name+"-"+ randomName()
    file = open(filename+ ".txt", "w")
    file.write("\n\n+==================================================================+\n")

    #writing in text file based on the value of typeOfTransaction
    if typeOfTransaction=="sale":
        file.write("\t\t\t\tSale Details\t\n")
    elif typeOfTransaction=="order":
        file.write("\t\t\t\tOrder Details\t\n")
        
    file.write("+==================================================================+\n")

    if typeOfTransaction=="sale":
        file.write("Name of Customer:"+ str(name) +"\n" )
        file.write("Address of Customer:"+ str(location) +"\n" )
        file.write("Phone number:" + str(phone) + "\n")
        file.write("Time of Sale: " + return_time() + "\n")
    elif typeOfTransaction=="order":
        file.write("Name of Shipping Company:"+ str(name) +"\n" )
        file.write("Location of Shipping Company:"+ str(location) +"\n" )
        file.write("Phone number:" + str(phone) + "\n")
        file.write("Time of Order: " + return_time() + "\n")

    file.write("Date: "+ return_date()+"\n")
    file.write("Total Price: "+str(totalPrice)+"\n")
    file.write("\n")
    file.write("Details regarding bikes:\n")
    file.write("+------------------------------------------------------------------------------------------------------------------------------+\n")
    file.write(f'{"Bike Name":<25}{"Quantity":<10}{"Unit Price":<15}{"Bike-Company":<44}{"Color":<20}{"Sale Price(In $)":<10}'"\n")
    file.write("+------------------------------------------------------------------------------------------------------------------------------+\n")
    
    #iterating over bikeData list and writing those values in text file
    for bike in bikeData:
        file.write(f'{bike[0]:<25}{bike[1]:<10}{bike[2]:<15}{bike[3]:<44}{bike[4]:<20}{bike[5]:<10}'"\n")
    file.write("+------------------------------------------------------------------------------------------------------------------------------+\n")
    file.write("====================================================================================================================================\n")
    file.close()

    
def return_date():
    """imports datetime and returns a string as date after concatenating year,month and day """
    nowDateTime = datetime.datetime.now()
    return str(nowDateTime.year) + "-" + str(nowDateTime.month) + "-" + str(nowDateTime.day) 

def return_time():
    """imports datetime and returns a string as time after concatenating hour, minute and second """
    
    nowDateTime = datetime.datetime.now()
    return str(nowDateTime.hour) + ":" + str(nowDateTime.minute) + ":" + str(nowDateTime.second)

def randomName():
    """imports datetime and returns a string as random name after concatenating different values relating to date and time """
    
    nowDateTime = datetime.datetime.now()
    nowYear = nowDateTime.year
    nowMonth = nowDateTime.month
    nowDay = nowDateTime.day
    nowHour = nowDateTime.hour
    nowMinute = nowDateTime.minute
    nowSecond = nowDateTime.second
    nowMicrosecond = nowDateTime.microsecond
    return str(nowDay) + str(nowMonth) + str(nowYear) + str(nowHour) + str(nowMinute) + str(nowSecond) + str(nowMicrosecond) 


def print_sale_details(name, location, phone, price, soldBikes):
    """takes name, location, phone, price and soldBikes list as parameter and
            prints out these details regarding customer and sold bikes in tabular form"""
    print("\n\n\n+==================================================================+")
    print("\t\t\tSale Details\t")
    print("+==================================================================+")
    print("Name of Customer: "+ name)
    print("Address: " + location)
    print("Phone number: " + phone)
    print("Total Price: $" ,price)
    print("Date: "+ return_date())
    print("Time of Sale: " + return_time())
    print("\n")
    print("Details regarding sold bikes: ")
    print("+-----------------------------------------------------------------------------------------------------------------------------+")
    print(f'{"Bike Name":<25}{"Quantity":<10}{"Unit Price":<15}{"Bike-Company":<44}{"Color":<20}{"Sale Price(In $)":<10}')
    print("+-----------------------------------------------------------------------------------------------------------------------------+")
    #iterating over soldBikes list and printing out those values
    for bike in soldBikes:
        print(f'{bike[0]:<25}{bike[1]:<10}{bike[2]:<15}{bike[3]:<44}{bike[4]:<20}{bike[5]:<10}')
    print("+-----------------------------------------------------------------------------------------------------------------------------+\n")
    print("+=================================================================================================================================+\n\n\n\n")

def print_order_details(name, location, phone, price, orderedBikes):
    """takes name, location, phone, price and orderedBikes list as parameter and
            prints out these details regarding shipping company and ordered bikes in tabular form"""
    
    print("\n\n\n+==================================================================+")
    print("\t\t\tOrder Details\t")
    print("+==================================================================+")
    print("Name of Shipping Company: "+ name)
    print("Location: " + location)
    print("Phone number: " + phone)
    print("Total Price: $" ,price)
    print("Date: "+ return_date())
    print("Time of Order: " + return_time())
    print("\n")
    print("Details regarding the ordered bikes: ")
    print("+------------------------------------------------------------------------------------------------------------------------------+")
    print(f'{"Bike Name":<25}{"Quantity":<10}{"Unit Price":<15}{"Bike-Company":<44}{"Color":<20}{"Cost Price(In $)":<10}')
    print("+------------------------------------------------------------------------------------------------------------------------------+")
    #iterating over orderedBikes list and printing out those values
    for bike in orderedBikes:
        print(f'{bike[0]:<25}{bike[1]:<10}{bike[2]:<15}{bike[3]:<44}{bike[4]:<20}{bike[5]:<10}')
    print("+------------------------------------------------------------------------------------------------------------------------------+\n")
    print("+=================================================================================================================================+\n\n\n\n")









