from random import choice


def get_valid_rating():
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
    print(f"\n{len(movie_dict)} movies in total\n")

    for movie in movie_dict:
        print(f"{movie}: {movie_dict[movie]}")

    input("\nPress Enter to continue")


def add_movie(movie_dict: dict):
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
    movie_name = input("\nEnter movie name to delete: ")

    try:
        del movie_dict[movie_name]
        print(f"\nMovie {movie_name} successfully deleted")

    except KeyError:
        print(f"\nMovie {movie_name} not found. Returning to menu")

    input("\nPress Enter to continue")


def update_movie(movie_dict: dict):
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
    ratings.sort()
    median_index = int(len(ratings) / 2)
    median_rating = ratings[median_index]
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
    movie, rating = choice(list(movie_dict.items()))
    print(f"\nYour movie for tonight: {movie}, it's rated {rating}")

    input("\nPress Enter to continue")


def get_movie(movie_dict: dict):
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
    cloned_dict = movie_dict.copy()

    print()
    for _ in range(len(movie_dict)):
        top_movie = max(cloned_dict, key=cloned_dict.get)
        top_rating = cloned_dict[top_movie]
        print(f"{top_movie}: {top_rating}")
        cloned_dict.pop(top_movie)

    input("\nPress Enter to continue")


def menu(movie_dict: dict):
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
        except ValueError:
            print("\nPlease enter a number")
            continue

        match user_input:
            case 1:
                get_movie_list(movie_dict)
            case 2:
                add_movie(movie_dict)
            case 3:
                delete_movie(movie_dict)
            case 4:
                update_movie(movie_dict)
            case 5:
                get_movie_stats(movie_dict)
            case 6:
                get_random_movie(movie_dict)
            case 7:
                get_movie(movie_dict)
            case 8:
                get_ranked_movies(movie_dict)
            case _:
                print("\nInvalid choice, please enter number within range 1-8")


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