def validate_phone_number(phone_number):
    if phone_number.startswith('+'):
        phone_number = phone_number[1:]

    if phone_number.count('-') > 1:
        return False

    parts = phone_number.split('-')

    for part in parts:
        if not part.isdigit():
            return False

    digit_count = sum(len(part) for part in parts)
    if not (6 <= digit_count <= 11):
        return False

    return True


def add_contact(save_to):
    add_name = input("\nEnter the name of the contact: ")


    while True:
        add_number = input(f"\nEnter {add_name}'s the phone number: ")
        if validate_phone_number(add_number):
            break
        else:
            print(f"{add_number} is not a valid phone number. It should contain only digits, one optional hyphen (-), or a plus sign (+) at the start. It must contain 6 to 11 digits.")

    print(f"\n{add_name} has been added to your contacts.")

    save_to[add_name] = add_number


def remove_contact(save_to):
    remove_name = input("\nEnter the name of the contact: ")

    try:
        del save_to[remove_name]
        print(f"\nContact {remove_name} has been removed.")
    except KeyError:
        print(f"\nContact {remove_name} not found")


def get_contact(save_to):
    search_contact = input("\nEnter the name of the contact to search for: ")

    if search_contact in save_to:
        print(f"\n{search_contact}'s number is {save_to[search_contact]}.")
    else:
        print(f"\nContact {search_contact} not found")


def get_phonebook(save_to):
    print("Phone book:")

    for key in save_to:
        print(f"    -{key}: {save_to[key]}")


def menu(save_to):
    print ("Welcome to the phone book app!")

    while True:
        print("""\nSelect an action:

           1. Add a contact
           2. Remove a contact
           3. Search for a contact
           4. View the phone book
           5. Exit""")

        try:
            user_input = input("\n Enter your choice (1 - 5): ")
        except ValueError:
            print(f"\n{user_input} is not a valid choice. Please select a number between 1 and 5.")

        match user_input:
            case "1":
                add_contact(save_to)
            case "2":
                remove_contact(save_to)
            case "3":
                get_contact(save_to)
            case "4":
                get_phonebook(save_to)
            case "5":
                print("\nGoodbye!")
                break
            case _:
                print(f"\n{user_input} is not a valid choice. Please select a number between 1 and 5.")


def main():
    phone_book = {}
    menu(phone_book)


if __name__ == '__main__':
    main()