from sqlalchemy import create_engine, text
from sys import exit
CURRENT_YEAR = 2025
MIN_YEAR = 500

def get_all_books():
    """Abstraction to retrieve all books with title, author name, publication year,
    !!!specific to this database!!!"""
    engine = create_engine('sqlite:///textbook.sqlite3')
    with engine.connect() as connection:
        results = connection.execute(text
                                     ('SELECT b.title, b.publication_year, a.name '
                                      'FROM books as b '
                                      'JOIN authors as a ON b.author_id = a.author_id '))
        rows = results.fetchall()
        return rows

def get_valid_year(word: str) -> int:
    year = 0
    while True:
        try:
            start_input = int(input(f"Please enter {word} of year range: "))
            if start_input < MIN_YEAR or start_input > CURRENT_YEAR:
                raise ValueError
            year = start_input
            break
        except ValueError:
            print("Error: invalid number!")
    return year

def print_all_books():
    rows = get_all_books()
    print(f"Returned {len(rows)} result(s): ")
    pub_year = 0
    for row in rows:
        dict_row = row._mapping
        if dict_row['publication_year'] == pub_year:
            pass
        else:
            pub_year = dict_row['publication_year']
            print(f"Published in {pub_year}: ")
        print(f"\t-{dict_row['title']} ({dict_row['name']})")


def search_titles():
    search_input = input("Enter a search term for book titles: ")
    rows = get_all_books()

    output_list = []
    for row in rows:
        dict_row = row._mapping
        if search_input.lower().strip() in dict_row['title']:
            output_list.append(dict_row)

    print(f"Returned {len(output_list)} result(s): ")
    for item in output_list:
        print(f"{item['title']} ({item['publication_year']}) by {item['name']}")

def search_years():
    while True:
        user_check = input("1. Search starting from year "
                           "| 2. Search ending before year "
                           "| 3. Search between years")
    
    start_year = get_valid_year("start")
    end_year = get_valid_year("end")



    engine = create_engine('sqlite:///textbook.sqlite3')
    with engine.connect() as connection:
        results = connection.execute(text
                                     ('SELECT b.title, b.publication_year, a.name '
                                      'FROM books as b '
                                      'JOIN authors as a ON b.author_id = a.author_id '))
        rows = results.fetchall()

def print_help():
    print("Available commands:")
    for disp_key in DISPATCH.keys():
        print(f"\t{disp_key}")

def quit_cli():
    print("Exiting, goodbye!")
    exit(0)


DISPATCH = {
    "print_all": print_all_books,
    "title_search": search_titles,
    "year_search": search_years,
    "help": print_help,
    "quit": quit_cli
}

def main():
    while True:
        try:
            user_input = input("Please enter command! 'help' for help: ")
            if user_input not in DISPATCH:
                raise ValueError
            DISPATCH[user_input]()
        except ValueError:
            print("Error, non-existent command.")


if __name__ == "__main__":
    main()
