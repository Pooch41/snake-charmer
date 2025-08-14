import cartopy.crs as ccrs  # map tools
import cartopy.feature as cfeature  # ^ (for colours and lakes - there were landlocked dots, lakes are the reason)
import matplotlib.pyplot as plt

from load_data import load_data

NUM_OF_COUNTRIES_PER_ROW = 6  # controls size of rows in print_all_countries(), for readability


def print_separator_line():
    """for the user's sanity, call after execution of func is done"""
    print("-" * 80)


def print_all_functions(data=None, num_of_ranks = None) -> None:
    """prints all commands recorded in dispatch"""
    print("All commands:")
    for key in DISPATCH_MAP:
        print("\t" + key)

    print_separator_line()


def print_all_countries(data: dict, num_of_ranks = None) -> None:
    """collects all countries into list, sets the list, lists the set,puts them in alpha order"""
    unique_countries = []
    print("All countries:")
    for item in data["data"]:
        unique_countries.append(item["COUNTRY"])

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


def print_top_countries(data: dict, num_of_ranks = int) -> None:
    """counts countries, then prints out top country, pops it, repeats num_of ranks times"""
    country_count = {}

    for item in data["data"]:
        if item["COUNTRY"] not in country_count:
            country_count[item["COUNTRY"]] = 1
        else:
            country_count[item["COUNTRY"]] += 1

    for i in range(num_of_ranks):
        top_country = max(country_count, key=country_count.get)
        print(f"{i + 1} {top_country} : {country_count[top_country]}")
        country_count.pop(top_country)

    print_separator_line()


def print_ships_by_type(data: dict, num_of_ranks = None) -> None:
    """collects ships by boat type, prints all types with counts"""
    type_count = {}
    print("Ships by boat type:")
    for item in data["data"]:
        if item["TYPE_SUMMARY"] not in type_count:
            type_count[item["TYPE_SUMMARY"]] = 1
        else:
            type_count[item["TYPE_SUMMARY"]] += 1

    for boat_type in type_count:
        print(f"{boat_type} : {type_count[boat_type]}")

    print_separator_line()


def generate_speed_histogram(data: dict, num_of_ranks = None) -> None:
    """generates speed histogram based on input data"""
    speeds = []

    print("Generating speed histogram...")
    for item in data["data"]:
        speeds.append(float(item["SPEED"]))

    plt.hist(sorted(speeds), bins=100, range=(min(speeds), max(speeds)))
    plt.title("Speed Histogram of Ships in Data")
    plt.xlabel("Speed")
    plt.ylabel("Number of Ships")
    plt.show()

    print("Histogram closed.")

    print_separator_line()


def print_searched_ship(data: dict, num_of_ranks = None) -> None:
    """searches for ship(s) by name snippet - may return many."""
    found_ships = []
    search_by = input("Please enter name, or part of name of the ship:")  # not validating cause ship_name == any string
    for item in data["data"]:
        if search_by.lower() in item["SHIPNAME"].lower():
            found_ships.append(item["SHIPNAME"])

    print("Found ship(s):")
    for ship in found_ships:
        if len(ship) == 0:
            print("No ships found.")  # smarter output
        else:
            print("\t" + ship)

    print_separator_line()


def print_by_country_code(data: dict, num_of_ranks = None) -> None:
    """takes in country code (case-insensitive) lists all ship from the country"""
    found_ships = []

    while True:  # validate input
        try:
            search_by = input("Please enter country code:")
            if not search_by.isalpha() or len(search_by) > 3 or len(search_by) < 2: #codes are 3 or 2 characters
                raise ValueError
            break
        except ValueError:
            print("Please enter valid country code.")

    for item in data["data"]:
        if search_by.upper() == item["CODE2"].upper():  # make both upper for to be more error proof
            found_ships.append(item["SHIPNAME"])

    print(f"\n{search_by.upper()} ship(s) found ({len(found_ships)}):")
    for ship in found_ships:
        print("\t" + ship)

    print_separator_line()


def generate_ship_map(data: dict, num_of_ranks = None) -> None:
    """draws a cool map with dots where the ships are"""
    latitudes = []
    longitudes = []
    for item in data["data"]:  # collects locations
        latitudes.append((float(item["LAT"])))
        longitudes.append((float(item["LON"])))

    # source : https://scitools.org.uk/cartopy/docs/v0.15/matplotlib/intro.html
    # source : https://scitools.org.uk/cartopy/docs/v0.15/crs/projections.html#cartopy-projections
    # source : https://scitools.org.uk/cartopy/docs/v0.14/matplotlib/feature_interface.html

    print("Plotting ship locations...")
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND, facecolor = 'lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor = 'lightblue')
    ax.add_feature(cfeature.LAKES, facecolor = 'lightblue', edgecolor = 'black')  # weird ships inland, see if lakes

    ax.scatter(longitudes, latitudes, color = 'red', marker = 'o', s = 3, transform = ccrs.PlateCarree())
    ax.coastlines()
    plt.show()
    print("Map closed.")

    print_separator_line()


DISPATCH_MAP = {
    "help": print_all_functions,
    "show_countries": print_all_countries,
    "top_countries": print_top_countries,
    "ships_by_type": print_ships_by_type,
    "speed_histogram": generate_speed_histogram,
    "search_ship": print_searched_ship,
    "ship_by_country": print_by_country_code,
    "draw_map": generate_ship_map
}


def main():
    ship_data = load_data()
    print("Welcome to the Ships CLI!")

    while True:
        try:
            user_input = input("Enter 'help' to view available commands:\n").lower()

            if user_input not in DISPATCH_MAP:
                raise TypeError

            if user_input == "top_countries":
                while True:
                    try:
                        num_of_ranks = int(input("Enter the number of countries you want to rank:\n"))
                        if num_of_ranks < 1: raise ValueError
                        break

                    except ValueError:
                        print("Please enter a number greater than 0.")

                DISPATCH_MAP[user_input.strip()](ship_data, num_of_ranks)

            else:

                DISPATCH_MAP[user_input.strip()](ship_data)

        except TypeError:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
