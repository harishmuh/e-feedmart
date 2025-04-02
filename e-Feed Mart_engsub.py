# ===========================================================================
# E-Feed mart
# Simple simulation app and data management system for aquaculture feed store
# ===========================================================================

# Importing the Tabulate library
from tabulate import tabulate

# Defining header items as components for tabulated menu display
header_items = ["Product Code", "Product", "Manufacturer", "Description", "Stock", "Price"]

# List of feed products
product_list = [
    ["8882", "Fish Feed 'Bintang'", "PT. CPP", "Protein 31%, Fat 5%", 30, 567498],
    ["PROFISH3", "common carp Feed", "PT. Cargill", "Protein 28%", 40, 517498],
    ["SNA12", "Floating Fish Feed", "PT. Sinta Prima", "Protein 33%, Fat 5%", 25, 398999],
    ["SPLA12", "Floating Catfish Feed", "PT. Suri Tani Pemuka", "Protein 32%", 50, 391200]
]

# Welcome menu options for users
welcome_menu = [
    ["Welcome to e-Feed Mart!!"],
    ["Choose your role:"],
    ["1. Fish Feed Seller\n2. Fish Farmer/Feed Buyer\n3. Exit Program"]
]

# Menu options for sellers
seller_menu = [
    ["Welcome to e-Feed Mart!!"],
    ["As a Seller, what would you like to do?"],
    ["1. Display product list\n2. Add feed product stock\n3. Update feed stock\n4. Remove feed stock data\n5. Return to the main menu"]
]

# Menu options for buyers
buyer_menu = [
    ["Welcome to e-Feed Mart!!"],
    ["As a Buyer, what would you like to do?"],
    ["1. View feed product list\n2. Purchase feed products\n3. Return to the main menu"]
]

# Sub-menu options for displaying product lists (Seller)
menu_1_options = [
    ["Select an option below"],
    ["1. Display all feed products\n2. Display product by product code\n3. Display products by lowest price\n4. Display products by highest price\n5. Return to the previous menu"]
]

# Sub-menu options for adding new feed products (Seller)
menu_2_options = [
    ["Select an option below"],
    ["1. Add a new feed product\n2. Return to the previous menu"]
]

# Sub-menu options for updating feed stock (Seller)
menu_3_options = [
    ["Select an option below"],
    ["1. Update feed product list\n2. Return to the previous menu"]
]

# Sub-menu options for removing feed stock (Seller)
menu_4_options = [
    ["Select an option below"],
    ["1. Remove a specific feed product\n2. Remove all feed products\n3. Return to the previous menu"]
]

# Defining functions for menu and sub-menu components

# Function to display all feed products
def display_products():
    print(tabulate(product_list, headers=header_items, tablefmt="fancy_grid"))

# Function to display the main menu for selecting roles (Seller/Buyer) or exiting the program
def display_main_menu():
    print(tabulate(welcome_menu, tablefmt="fancy_grid"))

# Function to display the seller's menu
def display_seller_menu():
    print(tabulate(seller_menu, tablefmt="fancy_grid"))

# Function to display the buyer's menu
def display_buyer_menu():
    print(tabulate(buyer_menu, tablefmt="fancy_grid"))

# Function to display the sub-menu for viewing feed product lists
def menu_1_display():
    print(tabulate(menu_1_options, tablefmt="fancy_grid"))

# Function to display the sub-menu for adding feed products
def menu_2_display():
    print(tabulate(menu_2_options, tablefmt="fancy_grid"))

# Function to display the sub-menu for updating feed stock
def menu_3_display():
    print(tabulate(menu_3_options, tablefmt="fancy_grid"))

# Function to display the sub-menu for removing feed stock
def menu_4_display():
    print(tabulate(menu_4_options, tablefmt="fancy_grid"))

# Function to sort products by ascending price (cheapest to most expensive)
def sort_by_price_asc(products):
    return sorted(products, key=lambda x: x[5])

# Function to sort products by descending price (most expensive to cheapest)
def sort_by_price_desc(products):
    return sorted(products, key=lambda x: x[5], reverse=True)

# Function to run the program and allow the user to select their role
def run_program():
    while True:
        display_main_menu()
        user_choice = input("Please enter the menu number you want to select: ")
        if user_choice == '1':
            seller_actions()
        elif user_choice == '2':
            buyer_actions()
        elif user_choice == '3':
            print("Thank you! See you next time!")
            break
        else:
            print("Please enter a valid option!")

# Function for seller actions
def seller_actions():
    while True:
        display_seller_menu()
        seller_choice = input("Enter the menu number you want to select: ")
        if seller_choice == '1':
            menu_1()
        elif seller_choice == '2':
            menu_2()
        elif seller_choice == '3':
            menu_3()
        elif seller_choice == '4':
            menu_4()
        elif seller_choice == '5':
            print("Thank you! See you next time!")
            break
        else:
            print("Please enter a valid menu option!")

# Function for displaying feed product list (Seller)
def menu_1():
    if not product_list:
        print("The product list is empty!")
        return
    while True:
        menu_1_display()
        choice = input("Enter the menu number (1/2/3/4/5): ")
        if choice == '1':
            display_products()
        elif choice == '2':
            product_code = input("Enter the product code: ").upper()
            for item in product_list:
                if item[0] == product_code:
                    print(tabulate([item], headers=header_items, tablefmt="fancy_grid"))
                    break
            else:
                print("Product code not found!")
        elif choice == '3':
            print("Products sorted by price (Lowest to Highest):")
            sorted_products = sort_by_price_asc(product_list)
            print(tabulate(sorted_products, headers=header_items, tablefmt="fancy_grid"))
        elif choice == '4':
            print("Products sorted by price (Highest to Lowest):")
            sorted_products = sort_by_price_desc(product_list)
            print(tabulate(sorted_products, headers=header_items, tablefmt="fancy_grid"))
        elif choice == '5':
            break
        else:
            print("Please enter a valid menu option!")

# Function for adding new feed products (Seller)
def menu_2():
    while True:
        menu_2_display()
        display_products()
        choice = input("Enter the menu number (1/2): ")
        if choice == "1":
            while True:
                new_product_code = input("Enter the new product code: ").upper()
                if any(item[0] == new_product_code for item in product_list):
                    print("Product already exists! Please enter a different product code.")
                else:
                    break
            new_product_name = input("Enter the new product name: ")
            new_manufacturer = input("Enter the manufacturer name: ")
            new_description = input("Enter the product description: ")
            while True:
                new_stock = input("Enter the stock quantity: ")
                if new_stock.isdigit() and int(new_stock) >= 0:
                    new_stock = int(new_stock)
                    break
                else:
                    print("Please enter a valid stock quantity!")
            while True:
                new_price = input("Enter the product price: ")
                if new_price.isdigit() and int(new_price) > 0:
                    new_price = int(new_price)
                    break
                else:
                    print("Please enter a valid price!")
            while True:
                confirm = input("Are you sure you want to save this product? (Y/N): ").upper()
                if confirm == 'Y':
                    product_list.append([new_product_code, new_product_name, new_manufacturer, new_description, new_stock, new_price])
                    print(f"Your product '{new_product_name}' (Code: {new_product_code}) with stock quantity {new_stock} has been saved.")
                    break
                elif confirm == 'N':
                    menu_2_display()
                    break
                else:
                    print("Invalid input, please enter Y or N.")
        elif choice == "2":
            display_main_menu()
            break
        else:
            print("Please enter a valid menu option!")

# Function for sellers to modify the feed product list
# Input options: '1' to update or modify product data, '2' to return to the previous menu
def menu_3():
    if product_list == []:
        print('The product list is empty!')
        return
    while True:
        menu_3_display()
        display_products()
        menu_input_3 = input('Enter the menu number you want (1/2): ')
        
        # Input '1' to modify product data
        if menu_input_3 == '1':
            product_code_update = input('Enter the product code you want to modify: ').upper()
            
            # Find the index of the product to update
            index_to_update = None
            for i, product in enumerate(product_list):
                if product[0] == product_code_update:
                    index_to_update = i
                    break
            
            if index_to_update is not None:
                column_to_update = input("Enter the column name you want to modify: ").capitalize()
                
                if column_to_update in product_headers:
                    new_value = input(f"Enter the new value for column '{column_to_update}': ")
                    
                    # Validation for 'Stock' and 'Price' columns
                    if column_to_update in ['Stock', 'Price']:
                        try:
                            new_value = int(new_value)
                            if new_value <= 0:
                                print("Input must be greater than zero!")
                                continue
                        except ValueError:
                            print("Please enter a valid number!")
                            continue
                    
                    # Validation for 'Product', 'Description', and 'Manufacturer' columns
                    elif column_to_update in ['Product', 'Description', 'Manufacturer']:
                        if new_value.isdigit():
                            print("Product name cannot contain only numbers!")
                            continue
                    
                    while True:
                        confirmation = input("Are you sure you want to update the data? (Y/N) ").upper()
                        if confirmation == 'Y':
                            product_list[index_to_update][product_headers.index(column_to_update)] = new_value
                            print(f"You have updated the product {product_code_update}.")
                            break
                        elif confirmation == 'N':
                            print("Data update canceled.")
                            break
                        else:
                            print("Invalid input!")
                            
                else:
                    print("The column name you entered is not available.")
            else:
                print("The product code you entered is not available.")
        
        # Input '2' to return to the previous menu
        elif menu_input_3 == "2":
            print()
            menu_3_display()
            break
        else:
            print("\nPlease enter a valid menu option!\n")
            continue


# Function for sellers to delete products from the feed product list
# Input options: '1' to delete a specific product, '2' to delete all products, '3' to return to the previous menu
def menu_4():
    if product_list == []:
        print('The product list is empty!')
        return
    while True:
        menu_4_display()
        display_products()
        menu_input_4 = input('Enter the menu number you want (1/2/3): ')
        
        # Input '1' to delete a specific product based on the provided product code
        if menu_input_4 == '1':
            if product_list == []:
                print('The product list is empty!')
                return
            
            product_code_delete = input('Enter the product code to delete: ').upper()
            
            # Find the index of the product to delete
            index_to_delete = None
            for i, product in enumerate(product_list):
                if product[0] == product_code_delete:
                    index_to_delete = i
                    break
            
            if index_to_delete is not None:
                confirmation = input("Are you sure you want to delete this product? (Y/N) ").upper()
                if confirmation == 'Y':
                    del product_list[index_to_delete]
                    print(f"The product with code {product_code_delete} has been deleted.")
                elif confirmation == 'N':
                    print(f"The product with code {product_code_delete} was not deleted.")
                else:
                    print("Invalid input!")
                    continue
            else:
                print("The product code you entered is not available.")
        
        # Input '2' to delete all products in the list
        elif menu_input_4 == "2":
            if product_list == []:
                print('The product list is empty!')
                return
            
            confirmation = input("Are you sure you want to delete all products? (Y/N) ").upper()
            if confirmation == 'Y':
                product_list.clear()
                print("All products have been deleted.")
            elif confirmation == 'N':
                print("Products were not deleted.")
            else:
                print("Invalid input!")
                continue
        
        # Input '3' to return to the previous menu
        elif menu_input_4 == "3":
            break
        else:
            print('Please enter a valid menu option!')


# Function for customers (buyers)
# Buyers can view/print the feed product list and purchase feed
# Input options: '1' to view the product list, '2' to buy feed products, '3' to return to the previous menu
def feed_customer():
    while True:
        display_customer_menu()
        buyer_menu_input = input("Enter the menu number you want to select: ")
        
        # Input '1' to view all available products
        if buyer_menu_input == '1':
            if product_list == []:
                print('The product list is empty!')
                return
            while True:
                menu_1_display()
                menu_input_1 = input('Enter the menu number you want (1/2/3/4/5): ')
                
                # Input '1' to display all products
                if menu_input_1 == '1':
                    display_products()
                
                # Input '2' to display a specific product
                elif menu_input_1 == '2':
                    product_code_input = input('Enter the product code you want: ').upper()
                    for product in product_list:
                        if product[0] == product_code_input:
                            print(tabulate([product], headers=product_headers, tablefmt="fancy_grid"))
                            break
                    else:
                        print("Product code not found!")
                
                # Input '3' to display products sorted by lowest price
                elif menu_input_1 == '3':
                    print("Product list sorted by lowest price:")
                    sorted_lowest_price = sort_by_price_asc(product_list)
                    print(tabulate(sorted_lowest_price, headers=product_headers, tablefmt="fancy_grid"))
                
                # Input '4' to display products sorted by highest price
                elif menu_input_1 == '4':
                    print("Product list sorted by highest price:")
                    sorted_highest_price = sort_by_price_desc(product_list)
                    print(tabulate(sorted_highest_price, headers=product_headers, tablefmt="fancy_grid"))
                
                # Input '5' to return to the previous menu
                elif menu_input_1 == '5':
                    break
                else:
                    print('Please enter a valid menu option!')
        
        # Input '2' to buy available feed products
        elif buyer_menu_input == '2':
            if product_list == []:
                print('The product list is empty!')
                return
            
            display_products()
            product_code_buy = input("Enter the product code you want to buy: ").upper()
            product_found = False
            
            for product in product_list:
                if product[0] == product_code_buy:
                    product_found = True
                    price_per_sack = product[5]  # Product price per sack
                    product_stock = product[4]   # Product stock
                    break
            
            if not product_found:
                print("The product code you entered is not available.")
            else:
                while True:
                    try:
                        quantity_to_buy = int(input("Enter the number of sacks you want to buy: "))
                        if quantity_to_buy <= 0:
                            print("Quantity must be greater than zero.")
                        elif quantity_to_buy > product_stock:
                            print("Insufficient stock.")
                        else:
                            total_price = price_per_sack * quantity_to_buy
                            print(f"Total price: Rp {total_price}")
                            confirm_purchase = input(f"Confirm purchase? (Y/N): ").upper()
                            if confirm_purchase == 'Y':
                                product[4] -= quantity_to_buy
                                print("Thank you for your purchase!")
                            else:
                                print("Transaction canceled.")
                            break
                    except ValueError:
                        print("Please enter a valid number.")
        
        # Input '3' to return to the previous menu
        elif buyer_menu_input == '3':
            print("Thank you!")
            break
        else:
            print('Please enter a valid menu option!')

if __name__ == "__main__":
    program()
