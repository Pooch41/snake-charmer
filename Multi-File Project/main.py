import file_manager
import product_manager


USER_CHOICE = """
Welcome to the shopping list app!
Enter:
- 'a' to add a new product
- 'l' to list all products
- 'b' to mark a product as bought
- 'd' to delete a product
- 'q' to quit
Your choice: """


def menu():
    """
    Show the main menu, get user choice and call the wanted function
    Stops only when user quits
    """
    file_manager.create_file()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            product_manager.prompt_add_product()
        elif user_input == 'l':
            product_manager.list_products()
        elif user_input == 'b':
            product_manager.prompt_bought_product()
        elif user_input == 'd':
            product_manager.prompt_delete_product()

        user_input = input(USER_CHOICE)


def main():
    menu()


if __name__ == "__main__":
    main()