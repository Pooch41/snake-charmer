import cartopy.crs as ccrs  # map tools
import cartopy.feature as cfeature  # ^ (for colours and lakes - there were landlocked dots, lakes are the reason)
import matplotlib.pyplot as plt

from load_data import load_data

NUM_OF_COUNTRIES_PER_ROW = 6  # controls size of rows in print_all_countries(), for readability


def quit_cli(data=None, ranks=None) -> None:
    """print message and exits CLI"""
    print("Exitting Ships CLI... Bye!")
    raise SystemExit


def print_separator_line() -> None:
    """for the user's sanity, call after execution of func is done"""
    print("-" * 80)


def collect_data_in_keyword(data: dict, keyword: str, item_type: type | None = None) -> list:
    """helper function - collect all in item[keyword] - data from csv file"""
    output_list = []
    if item_type is None:
        for item in data["data"]:
            output_list.append(item[keyword])
    else:
        for item in data["data"]:
            output_list.append(item_type(item[keyword]))
    return output_list


def count_by_keyword(data: dict, keyword: str) -> dict:
    """helper function - count by keyword - data from csv file"""
    output_dict = {}
    for item in data["data"]:
        if item[keyword] not in output_dict:
            output_dict[item[keyword]] = 1
        else:
            output_dict[item[keyword]] += 1
    return output_dict


def print_all_functions(data=None, ranks=None) -> None:
    """prints all commands recorded in dispatch"""
    print("All commands:")
    for key in DISPATCH_MAP:
        print("\t" + key)

    print_separator_line()


def print_all_countries(data: dict, ranks=None) -> None:
    """collects all countries into list, sets the list, lists the set,puts them in alpha order"""
    unique_countries = collect_data_in_keyword(data, "COUNTRY")
    print("All countries:")

    unique_countries = sorted(list(set(unique_countries)))

    num_in_row = 0
    for country in unique_countries:
        num_in_row += 1
        if num_in_row == NUM_OF_COUNTRIES_PER_ROW:
            print(country + ",")
            num_in_row = 0
        else:
            print(country, end=", ")

    print_separator_line()


def print_top_countries(data: dict, num_of_ranks: int) -> None:
    """counts countries, then prints out top country, pops it, repeats num_of ranks times"""
    while True:
        try:
            if num_of_ranks < 1:
                raise TypeError
            break
        except (TypeError, ValueError):
            print("Please enter a number that is equal or greater than 1.")
    country_count = count_by_keyword(data, "COUNTRY")

    for i in range(num_of_ranks):
        top_country = max(country_count, key=country_count.get)
        print(f"{i + 1} {top_country}: {country_count[top_country]}")
        country_count.pop(top_country)

    print_separator_line()


def print_ships_by_type(data: dict, ranks=None) -> None:
    """collects ships by boat type, prints all types with counts"""
    type_count = count_by_keyword(data, "TYPE_SUMMARY")
    print("Ships by type:")

    type_count = sorted(type_count.items(), key=lambda x: x[1], reverse=True)
    for boat_type in type_count:
        print(f"{boat_type[0]}: {boat_type[1]}")
    print_separator_line()


def generate_speed_histogram(data: dict, ranks=None) -> None:
    """generates speed histogram based on input data"""
    speeds = collect_data_in_keyword(data, "SPEED", float)
    print("Generating speed histogram...")
    plt.hist(sorted(speeds), bins=100, range=(min(speeds), max(speeds)))
    plt.title("Speed Histogram of Ships in Data")
    plt.xlabel("Speed")
    plt.ylabel("Number of Ships")
    plt.show()

    print("Histogram closed.")

    print_separator_line()


def print_searched_ship(data: dict, ranks=None) -> None:
    """searches for ship(s) by name snippet - may return many."""
    found_ships = []
    search_by = input("Please enter name, or part of name of the ship: ")  # not validating cause ship_name == any string
    for item in data["data"]:
        if search_by.lower() in item["SHIPNAME"].lower():
            found_ships.append(item["SHIPNAME"])

    if len(found_ships) == 0:
        print(f"No ships found with '{search_by}' in name found.")
    else:
        print("Found ship(s):")
        for ship in found_ships:
            print("\t" + ship)

    print_separator_line()


def print_of_country_code(data: dict, ranks=None) -> None:
    """takes in country code (case-insensitive) lists all ship from the country"""
    found_ships = []

    while True:  # validate input
        try:
            search_by = input("Please enter country code: ")
            if not search_by.isalpha() or len(search_by) > 3 or len(search_by) < 2:  # codes are 3 or 2 characters
                raise ValueError
            break
        except ValueError:
            print("Please enter valid country code.")

    for item in data["data"]:
        if search_by.upper() == item["CODE2"].upper():  # make both upper for to be more error proof
            found_ships.append(item["SHIPNAME"])

    print(f"\n{search_by.upper()} ship(s) found ({len(found_ships)}): ")
    for ship in found_ships:
        print("\t" + ship)

    print_separator_line()


def generate_ship_map(data: dict, ranks=None) -> None:
    """draws a cool map with dots where the ships are"""
    latitudes = collect_data_in_keyword(data, "LAT", float)
    longitudes = collect_data_in_keyword(data, "LON", float)

    # source : https://scitools.org.uk/cartopy/docs/v0.15/matplotlib/intro.html
    # source : https://scitools.org.uk/cartopy/docs/v0.15/crs/projections.html#cartopy-projections
    # source : https://scitools.org.uk/cartopy/docs/v0.14/matplotlib/feature_interface.html

    print("Plotting ship locations...")
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    ax.add_feature(cfeature.LAKES, facecolor='lightblue', edgecolor='black')  # weird ships inland, see if lakes

    ax.scatter(longitudes, latitudes, color='red', marker='o', s=3, transform=ccrs.PlateCarree())
    ax.coastlines()
    plt.show()
    print("Map closed.")

    print_separator_line()


DISPATCH_MAP = {
    "exit": quit_cli,
    "help": print_all_functions,
    "show_countries": print_all_countries,
    "top_countries": print_top_countries,
    "ships_by_type": print_ships_by_type,
    "speed_histogram": generate_speed_histogram,
    "search_ship": print_searched_ship,
    "ship_of_country": print_of_country_code,
    "draw_map": generate_ship_map
}


def main() -> None:
    ship_data = load_data()
    print("Welcome to the Ships CLI!")
    ranks = 0

    while True:
        try:
            user_input = input("Enter 'help' to view available commands:\n").lower()
            if user_input not in DISPATCH_MAP:
                raise TypeError
            if user_input == "top_countries":
                while True:
                    try:
                        ranks = int(input("Enter the number of countries you want to rank:\n"))
                        if ranks <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print("Ranks are only allowed to be whole, positive numbers. Please try again.")
            DISPATCH_MAP[user_input.strip()](ship_data, ranks)
        except TypeError:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
