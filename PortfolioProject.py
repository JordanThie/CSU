# This is AUTOMANAGER a program for auto dealers to store and modify vehicle inventory
# Created by Jordan Thie 2021

inventory = {} # Dictionary to store values

class Automobile: # Class for auto values
    def __init__(self, make, model, color, year, mileage, vin):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
        self.vin = vin



# Program main function welcome and menu option list
def main():
    print('\n ***WELCOME TO AUTOMANAGER*** \n \n Please Select a Menu Option\n')

    print('1 -- Add a new vehicle')
    print('2 -- Update a vehicle')
    print('3 -- Delete a vehicle')
    print('4 -- View all vehicles')
    print('5 -- Export vehicles')
    print('Q -- Quit program')

    while True:
        try:
            option = (input('Type your choice: ')) # Asks user to select a menu option

# Add a new vehicle
            if option == 1:
                print('Add a new vehicle to the inventory')

                make = input('Enter the vehicle make:')
                inventory['Make'] = make

                model = input('Enter the vehicle model:')
                inventory['Model'] = model

                color = input('Enter vehicle color:')
                inventory['Color'] = color

                year = input('Enter vehicle year:')
                inventory['State'] = year

                mileage = int(input('Enter the vehicle mileage:'))
                inventory['Mileage'] = mileage

                vin = int(input('Enter the VIN:'))
                inventory['VIN'] = vin

                print('The following vehicle has been added to the inventory:')
                print(inventory)

# Update vehicles:
            elif option == 2:
                print('Update an item from the inventory')

                print(inventory)

                itemreplace = input("Enter the name of the attribute you wish to replace:")
                itemupdate = input("Enter the new information for that attribute:")
                inventory[itemreplace] = itemupdate

                print(inventory)

# Delete Vehicle Keys
            elif option == 3:
                print("Which vehicle would you like to delete?")
                print(inventory)

                delete_key = input("Enter the VIN of the vehicle you wish to delete.")
                if delete_key in inventory:
                    del inventory[delete_key]
                else:
                    print("Please enter a valid VIN.")
                print('Current Inventory',inventory)

# Display vehicle inventory
            elif option == 4:
                print('Current Inventory:', inventory)

# Export vehicle inventory
            elif option == 5:
                output = open("inventory.txt", "w")
                for item in inventory:
                    output.write("%s\n" % item)
                print('Text file \'inventory.txt\' has been created.')

            elif option == 'Q':
                print('Goodbye!')

# General error exception
        except:
                print('That option is not valid. Please try again.')



main() # Calls the main function to begin the program