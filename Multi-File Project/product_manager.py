import file_manager

def prompt_add_product():
    """
    Ask the user which product to add and call the insert function
    """
    name = input('Enter the new product name: ')
    quantity = input('Enter the new product quantity: ')
    insert_product(name, quantity)


def insert_product(name, quantity):
    """
    Gets a product name and quantity to add.
    Loads the current file, adds to the dict and re-saves the file.
    """
    products = file_manager.load_from_file()
    products.append({'name': name, 'quantity': quantity, 'bought': False})
    file_manager.save_file(products)


def list_products():
    """
    Loads the current file and prints all products to the screen.
    """
    for product in file_manager.load_from_file():
        bought = 'YES' if product['bought'] == True else 'NO'  # product[3] will be a falsy value (0) if not bought
        print(f"{product['name']} ({product['quantity']} â€” Bought: {bought}")


def prompt_bought_product():
    """
    Asks the user what product he bought and calls the update function
    """
    name = input('Enter the name of the product you just bought: ')
    mark_product_as_bought(name)


def mark_product_as_bought(name):
    """
    Gets a product name to mark as bought.
    Loads the product file, updates the bought product and re-saves the file.
    """
    products = file_manager.load_from_file()
    for product in products:
        if product['name'] == name:
            product['bought'] = True
    file_manager.save_file(products)


def prompt_delete_product():
    """
    Asks the user what product he wants to delete calls the delete function
    """
    name = input('Enter the name of the product you wish to delete: ')
    delete_product(name)


def delete_product(name):
    """
    Gets a product name to remove.
    Loads the product file, removes the wanted product and re-saves the file.
    """
    products = file_manager.load_from_file()
    products = [product for product in products if product['name'] != name]
    file_manager.save_file(products)