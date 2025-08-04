from random import choice
from statistics import median


def get_valid_rating():
    """validate that rating is a number and is within bounds"""
    rating = 0
    while rating < 1 or rating > 10:
        try:
            rating = float(input("\nEnter movie rating (1-10): "))

            if rating < 1 or rating > 10:
                raise ValueError()

        except ValueError:
            print("\nInvalid rating, please enter a number within range")

    return rating


def get_movie_list(movie_dict: dict):
    """retrieve all movies"""
    print(f"\n{len(movie_dict)} movies in total\n")

    for movie in movie_dict:
        print(f"{movie}: {movie_dict[movie]}")

    input("\nPress Enter to continue")


def add_movie(movie_dict: dict):
    """add movie to dict"""
    name = ""

    while len(name) < 1:
        name = input("\nEnter movie name: ")
        if len(name) < 1:
            print("\nMovie name must be at least one character long!")

    if name in movie_dict:
        print(f"\nMovie {name} already exists! Returning to menu.")
    else:
        rating = get_valid_rating()
        movie_dict[name] = rating
        print(f"\nMovie {name} successfully added.")

    input("\nPress Enter to continue")


def delete_movie(movie_dict: dict):
    """remove movie from dict"""
    movie_name = input("\nEnter movie name to delete: ")

    try:
        del movie_dict[movie_name]
        print(f"\nMovie {movie_name} successfully deleted")

    except KeyError:
        print(f"\nMovie {movie_name} not found. Returning to menu")

    input("\nPress Enter to continue")


def update_movie(movie_dict: dict):
    """update existing movie in dict"""
    movie_name = input("\nEnter movie name to update: ")

    if movie_name in movie_dict:
        rating = get_valid_rating()
        movie_dict[movie_name] = rating
        print(f"\nMovie {movie_name} successfully updated")

    else:
        print(f"\nMovie {movie_name} not found. Returning to menu")

    input("\nPress Enter to continue")


def get_movie_stats(movie_dict: dict):
    """get avg, median, best(rating), worst(rating) - if same rating, print all with same rating"""

    average_rating = 0
    for movie in movie_dict:
        average_rating += movie_dict[movie]
    average_rating /= len(movie_dict)
    print(f"\nAverage rating: {average_rating:.01f}")

    ratings = []
    for movie in movie_dict:
        ratings.append(movie_dict[movie])
    median_rating = median(ratings)
    print(f"Median rating: {median_rating}")

    best_score = max(movie_dict.values())
    best_movies = []
    for movie in movie_dict:
        if movie_dict[movie] == best_score:
            best_movies.append(movie)
    print("Best movie(s):")
    for movie in best_movies:
        print(f"\t{movie}, {movie_dict[movie]}")

    worst_score = min(movie_dict.values())
    worst_movies = []
    for movie in movie_dict:
        if movie_dict[movie] == worst_score:
            worst_movies.append(movie)
    print("Worst movie(s):")
    for movie in worst_movies:
        print(f"\t{movie}, {movie_dict[movie]}")

    input("\nPress Enter to continue")


def get_random_movie(movie_dict: dict):
    """select random movie from dict, show rating"""
    movie, rating = choice(list(movie_dict.items()))
    print(f"\nYour movie for tonight: {movie}, it's rated {rating}")

    input("\nPress Enter to continue")


def get_movie(movie_dict: dict):
    """search movie from dict, from any part of name - show rating when found"""
    movie_search = input("Enter part of movie name: ")

    movies_found = 0
    for movie in movie_dict:
        if movie_search.lower() in movie.lower():
            print(f"\n{movie}, {movie_dict[movie]}")
            movies_found += 1

    if movies_found == 0:
        print(f"\nNo movie with {movie_search} found. Returning to menu")
        return

    input("\nPress Enter to continue")


def get_ranked_movies(movie_dict: dict):
    """sort and show movies by rating, display sorted rankings"""
    cloned_dict = movie_dict.copy()

    print()
    for _ in range(len(movie_dict)):
        top_movie = max(cloned_dict, key=cloned_dict.get)
        top_rating = cloned_dict[top_movie]
        print(f"{top_movie}: {top_rating}")
        cloned_dict.pop(top_movie)

    input("\nPress Enter to continue")


def menu(movie_dict: dict):
    """menu function -  show actions, select, execute, return to menu"""
    menu_dispatch = {
        1: get_movie_list,
        2: add_movie,
        3: delete_movie,
        4: update_movie,
        5: get_movie_stats,
        6: get_random_movie,
        7: get_movie,
        8: get_ranked_movies,
    }

    while True:

        print("""\nMenu:
        1. List movies
        2. Add movie
        3  Delete movie
        4. Update movie
        5. Stats
        6. Random movie
        7. Search movie
        8. Movies sorted by rating""")

        try:
            user_input = int(input("\nEnter choice (1-8): "))
            if user_input < 1 or user_input > 8:
                raise ValueError
        except ValueError:
            print("\nPlease enter a number")
            continue

        menu_dispatch[user_input](movie_dict)



def main():
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    menu(movies)


if __name__ == "__main__":
    main()