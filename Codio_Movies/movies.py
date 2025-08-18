import os
from random import choice
from statistics import median

import movie_storage as ms
import validate_inputs as v


def exit_application(movies=None, store=None, validate=None) -> None:
    os._exit(os.EX_OK)


def print_movie_list(movie_dict: dict, store=None, validate=None) -> None:
    """retrieve all movies"""
    print(f"\n{len(movie_dict["movies"])} movies in total\n")

    for movie in movie_dict["movies"]:
        print(f"{movie["title"]} ({movie["year"]}): {movie["rating"]}")

    input("\nPress Enter to continue")


def add_movie(movie_dict: dict, store, validate) -> None:
    title = validate.get_valid_new_name(movie_dict)
    year = validate.get_valid_year()
    rating = validate.get_valid_rating()

    store.add_movie(title, year, rating)
    print(f"\nMovie {title} added to list")
    input("\nPress Enter to continue")


def delete_movie(movie_dict: dict, store, validate) -> None:
    """remove movie from dict"""
    movie_name = validate.get_valid_existing_name(movie_dict)

    store.delete_movie(movie_name)
    print(f"\nMovie {movie_name} deleted successfully")

    input("\nPress Enter to continue")


def update_movie(movie_dict: dict, store, validate) -> None:
    """update existing movie in dict"""
    movie_name = validate.get_valid_existing_name(movie_dict)
    rating = validate.get_valid_rating()
    store.update_movie(movie_name, rating)

    print(f"\nMovie {movie_name} successfully updated")
    input("\nPress Enter to continue")


def print_movie_stats(movie_dict: dict, store=None, validate=None) -> None:
    """get avg, median, best(rating), worst(rating) - if same rating, print all with same rating"""
    scores = [float(movie["rating"]) for movie in movie_dict["movies"]]

    average_rating = sum(scores) / len(scores)
    print(f"\nAverage rating: {average_rating:.01f}")

    median_rating = median(scores)
    print(f"Median rating: {median_rating:.01f}")

    best_score = max(scores)
    best_movies = []

    print("Best movie(s):")
    for movie in movie_dict["movies"]:
        if float(movie["rating"]) == best_score:
            best_movies.append(movie["title"])
            print(f"\t{movie["title"]}, {movie["rating"]}")

    worst_score = min(scores)
    worst_movies = []

    print("Worst movie(s):")
    for movie in movie_dict["movies"]:
        if float(movie["rating"]) == worst_score:
            worst_movies.append(movie["title"])
            print(f"\t{movie["title"]}, {movie["rating"]}")

    input("\nPress Enter to continue")


def print_random_movie(movie_dict: dict, store=None, validate=None) -> None:
    """select random movie from dict, show rating"""
    item = choice(movie_dict["movies"])
    print(f"\nYour movie for tonight: {item["title"]}, it's rated {item["rating"]}")

    input("\nPress Enter to continue")


def print_searched_movie(movie_dict: dict, store=None, validate=None) -> None:
    """search movie from dict, from any part of name - show rating when found"""
    movie_search = input("Enter part of movie name: ")

    print()
    movies_found = 0
    for movie in movie_dict["movies"]:
        if movie_search.lower() in movie["title"].lower():
            print(f"{movie["title"]}, {movie["rating"]}")
            movies_found += 1

    if movies_found == 0:
        print(f"\nNo movie with {movie_search} found. Returning to menu")
        return

    input("\nPress Enter to continue")


def print_ranked_movies(movie_dict: dict, store=None, validate=None) -> None:
    """sort and show movies by rating, display sorted rankings"""
    movies_w_rating = {}
    for movie in movie_dict["movies"]:
        movies_w_rating[movie["title"]] = movie["rating"]

    print()
    for _ in range(len(movies_w_rating)):
        top_movie = max(movies_w_rating, key=movies_w_rating.get)
        top_rating = movies_w_rating[top_movie]
        print(f"{top_movie}: {top_rating}")
        movies_w_rating.pop(top_movie)

    input("\nPress Enter to continue")


def print_movies_by_year(movie_dict: dict, store=None, validate=None) -> None:
    """sort movies by year - reverse? ask user"""
    list_reversed = False
    while True:
        user_input = input("\n1 for Newest -> Oldest, 2 for Oldest -> Newest: ")
        if user_input.lower() == "1":
            list_reversed = True
            break
        if user_input.lower() == "2":
            break
        else:
            print("\nPlease enter '1' or '2'")

    movies_w_year = {}
    for movie in movie_dict["movies"]:
        movies_w_year[movie["year"]] = movie["title"]

    i = 1
    print()
    for year in sorted(movies_w_year, reverse=list_reversed):
        print(f"{i}. {movies_w_year[year]}, {year}")
        i += 1

    input("\nPress Enter to continue")


def filter_movies_alternating(movies: list, name_of_key: str, number: int or float, reverse=False) -> list:
    """filters input list by category name of key, value number, reverse True (1900 >>>), reverse False (<<<< 1900)"""
    new_movies = []
    if reverse:
        for movie in movies:
            if float(movie[name_of_key]) < float(number):
                new_movies.append(movie)
    else:
        for movie in movies:
            if float(movie[name_of_key]) > float(number):
                new_movies.append(movie)
    return new_movies


def get_valid_year_or_skip(movie_dict: dict, word: str, reverse=False) -> dict:
    """year validator, takes reasonable years, processes input."""
    filtered_movies = movie_dict
    while True:
        try:
            user_input = input(f"\nEnter {word} year (Enter to skip): ")
            if user_input == "":
                break
            if float(user_input) < v.MOVIES_INVENTED or float(user_input) > v.CURRENT_YEAR:
                raise ValueError()
            else:
                filtered_movies = filter_movies_alternating(movie_dict, "year", user_input, reverse)
            break
        except ValueError:
            print(f"\nInvalid year, please enter a number within range {v.MOVIES_INVENTED} - {v.CURRENT_YEAR}")

    return filtered_movies


def get_filtered_movies(movie_dict: dict, store=None, validate=None) -> None:
    """master filter function, first prompts for rank requirement, then year filters"""
    qualified_movies = movie_dict["movies"]
    while True:
        try:
            min_rating = input("\nEnter minimum rating for movie(Enter to skip): ")
            if min_rating == "":
                break
            elif float(min_rating) < 1 or float(min_rating) > 10:
                raise ValueError()
            else:
                qualified_movies = filter_movies_alternating(qualified_movies, "rating", float(min_rating), False)
                break
        except ValueError:
            print("\nInvalid rating, please enter a number within range")

    qualified_movies = get_valid_year_or_skip(qualified_movies, "start", False)
    qualified_movies = get_valid_year_or_skip(qualified_movies, "end", True)

    print()
    for movie in qualified_movies:
        print(f"{movie["title"]} ({movie["year"]}, {movie["rating"]})")

    input("\nPress Enter to continue")


DISPATCH_MAP = {
    0: exit_application,
    1: print_movie_list,
    2: add_movie,
    3: delete_movie,
    4: update_movie,
    5: print_movie_stats,
    6: print_random_movie,
    7: print_searched_movie,
    8: print_ranked_movies,
    9: print_movies_by_year,
    10: get_filtered_movies,
}


def main():
    """main function, acts  as menu -  show actions, select, execute, return to menu"""
    store = ms.MovieStorage()
    validate = v.ValidateInputs()

    while True:

        print("""\nMenu:
        0.  Exit
        1.  List movies
        2.  Add movie
        3   Delete movie
        4.  Update movie
        5.  Stats
        6.  Random movie
        7.  Search movie
        8.  Movies sorted by rating
        9.  Movies sorted by year
        10. Movies filtered by multiple parameters of choice""")

        try:
            user_input = int(input("\nEnter choice (0-10): "))
            if user_input < 0 or user_input > 10:
                raise ValueError

            movies = store.get_movies()
        except ValueError:
            print("\nPlease enter a number")
            continue

        DISPATCH_MAP[user_input](movies, store, validate)


if __name__ == "__main__":
    main()
