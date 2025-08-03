import json


GROCERIES_FILE = 'groceries.json'


def create_file():
    """
    Creates the json file. If it already exists, do nothing!
    """
    try:
        with open(GROCERIES_FILE, 'x') as file:
            json.dump([], file)  # initialize file as empty list
    except FileExistsError:
        pass


def save_file(products):
    """
    Saves the given product dict to the file, overwriting what's in the file.
    """
    with open(GROCERIES_FILE, 'w') as file:
        json.dump(products, file)


def load_from_file():
    """
    Loads the product dict from the file.
    """
    with open(GROCERIES_FILE, 'r') as json_file:
        return json.load(json_file)