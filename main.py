#importing functions from functions.py
from functions import *

#printing welcome message and options to be chosen from
show_welcome_message()
show_options()
continuing = True
checking = True

#using loop to continue to execute the program till user decides to discontinue
while continuing:
    
    #using loop to validate user input taken as option
    while checking:
        
        #using try, except for handling input that could cause error
        try:
            chooseOptions = int(input("Please enter specific digit indicating a certain function: "))
            while chooseOptions <= 0 or chooseOptions > 4:
                print("Invalid entry ! Please enter a specified number indicating a certain function.\n")
                chooseOptions = int(input("Please enter specific digit indicating a certain function: "))
            checking = False
        except:
            invalid_input()
            checking = True
            
    #showing all the details of the bikes in tabular form if user inputs 1
    if chooseOptions ==  1:
        show_bike_details()
        show_options()
        #assigning True value for continuing to ask for entering options and validate them
        checking = True

    #invoking the functions related to selling bikes if user inputs 2
    elif chooseOptions == 2:
        #printing out selling bike message and asking user to enter details regarding customer
        sellingBike()
        print("Please enter valid details regarding customer: ")
        customerName = input("Enter the name of the customer: ")
        customerLocation = input("Enter the address: ")
        phone_number = input("Enter the contact information: ")

        #invoking return_sold_bikes() function that returns the details of sold bikes in 2D list
        soldBike_data = return_sold_bikes()
        
        totalPrice = 0
        #iterating over the list to find total price
        for bike in soldBike_data:
            totalPrice += int(bike[5])
        #printing sale details and generating a bill for each sale
        print_sale_details(customerName, customerLocation, phone_number, totalPrice, soldBike_data)
        generating_bills("sale", soldBike_data, customerName, customerLocation, totalPrice, phone_number)

        #showing options again after sale
        show_options()
        checking = True

    #invoking the functions related to ordering bikes if user inputs 3
    elif chooseOptions == 3:
        #printing out selling bike message and asking user to enter details regarding shipping company
        orderingBike()
        print("Please enter details regarding shipping company: ")
        shippingName = input("Enter the name of the shipping company: ")
        shippingLocation = input("Enter the location: ")
        phone_number = input("Enter the contact information: ")

        #invoking return_sold_bikes() function that returns the details of ordered bikes in 2D list
        orderBike_data = return_ordered_bikes()
        
        totalPrice = 0
        #iterating over the list to find total price
        for bike in orderBike_data:
            totalPrice += int(bike[5])
        
        #printing order details and generating a bill for each order
        print_order_details(shippingName, shippingLocation, phone_number, totalPrice, orderBike_data)
        generating_bills("order", orderBike_data, shippingName, shippingLocation, totalPrice, phone_number)

        #showing options again after sale
        show_options()
        checking = True

    #invoking the functions related to ordering bikes if user inputs 4
    elif chooseOptions == 4:
        show_exit_message()
        continuing = False

        
