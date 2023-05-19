#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
        
    def get_cost(self):
        return self.cost
        
       
    def get_quantity(self):
        return self.quantity
        


    def __str__(self):
        return f"{self.country} {self.code} {self.product}, {self.quantity} pairs at {self.cost} each"


# This function will open the file
# inventory.txt and read the data from this file, then create a
# shoes object with this data and append this object into the
# shoes list. One line in this file represents data to create one
# object of shoes. You must use the try-except in this function
# for error handling. Remember to skip the first line using your
# code.

shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as f:
            next(f)  # skipping the first line
            for line in f:
                data = line.strip().split(",")
                country = data[0].strip()
                code = data[1].strip()
                product = data[2].strip()
                cost = float(data[3].strip())
                quantity = int(data[4].strip())
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error reading file:", e)


    # This function will allow a user to capture data
    # about a shoe and use this data to create a shoe object
    # and append this object inside the shoe list. 
           
def capture_shoes():

    country = input("Enter the country of origin: ")
    code = input("Enter the code: ")
    product = input("Enter the product name: ")
    
    # getting a valid cost and quantity inputs
    while True:
        try:
            cost = float(input("Enter the cost per pair: "))
            quantity = int(input("Enter the quantity: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    # creating and appending the shoe object to the shoe_list
    shoe_obj = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe_obj)
    print("Shoe added successfully!") 

    
# This function will iterate over the shoes list and
    # print the details of the shoes returned from the __str__
    # function. Optional: you can organise your data in a table format
    # by using Python’s tabulate module.
def view_all():
    for shoe in shoe_list:
        print(shoe)
    
       
# This function will find the shoe object with the lowest quantity,
# which is the shoes that need to be re-stocked. Ask the user if they
#want to add this quantity of shoes and then update it.
#  This quantity should be updated on the file for this shoe.

def re_stock():
   
    # Finding the shoe object with the lowest quantity
    lowest_quantity = float('inf')
    shoe_to_restock = None
    for shoe in shoe_list:
        if shoe.get_quantity() < lowest_quantity:
            lowest_quantity = shoe.get_quantity()
            shoe_to_restock = shoe
    
    if shoe_to_restock is None:
        print("No shoes to restock")
        return

    # Asking user if they want to add this quantity of shoes
    print(f"The shoe with code {shoe_to_restock.code} has the lowest quantity of {lowest_quantity}.")
    add_quantity = input("Do you want to add this quantity of shoes? (yes or no): ")
    
    if add_quantity.lower() == "yes":
        # Updating the quantity of shoes
        new_quantity = lowest_quantity * 2
        shoe_to_restock.quantity = new_quantity

        # Updating the file for this shoe
        with open("inventory.txt", "r+") as file:
            data = file.readlines()
            file.seek(0)
            for line in data:
                if line.startswith(shoe_to_restock.code):
                    updated_line = f"{shoe_to_restock.country} {shoe_to_restock.code} {shoe_to_restock.product} {shoe_to_restock.cost} {shoe_to_restock.quantity}\n"
                    file.write(updated_line)
                else:
                    file.write(line)
            file.truncate()

        print(f"The quantity of shoes with code {shoe_to_restock.code} has been updated to {new_quantity}")
    else:
        print("No changes made.")



# This function will search for a shoe from the list
# using the shoe code and return this object so that it will be printed.

def search_shoe():
    code = input("Enter the code of the shoe you want to search for: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return
    print(f"No shoe with code {code} found.")


#This function will calculate the total value for each item.
#Please keep the formula for value in mind: value = cost * quantity.
#Print this information on the console for all the shoes.

def value_per_item():
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product}: {value}")

 
# this function will determine the product with the highest quantity and
# print this shoe as being for sale.

def highest_qty():
    highest_quantity = 0
    highest_quantity_shoe = None
    for shoe in shoe_list:
        if shoe.quantity > highest_quantity:
            highest_quantity = shoe.quantity
            highest_quantity_shoe = shoe
    if highest_quantity_shoe is not None:
        print(f"The shoe with code {highest_quantity_shoe.code} has the highest quantity of {highest_quantity} and is for sale.")
    else:
        print("No shoes to sell.")




# in your main create a menu that executes each function
#above. This menu should be inside the while loop.
read_shoes_data()
while True:
    print("===== Shoe Inventory System =====")
    print("1. Capture new shoe")
    print("2. View all shoes")
    print("3. Restock shoes")
    print("4. Search for a shoe")
    print("5. Calculate value per item")
    print("6. Find the product with the highest quantity")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        capture_shoes()
    elif choice == "2":
        view_all()
    elif choice == "3":
        re_stock()
    elif choice == "4":
        search_shoe()
    elif choice == "5":
        value_per_item()
    elif choice == "6":
        highest_qty()
    elif choice == "7":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")   

#============end_of_code===================================