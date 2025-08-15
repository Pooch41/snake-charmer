from datetime import datetime as dt

MOVIES_INVENTED = 1880  # first motion cameras appeared in this decade
CURRENT_YEAR = dt.now().year

class ValidateInputs:
    @staticmethod
    def get_valid_title(movies: dict, exists: bool) -> str:
        movie_titles = []
        for movie in movies["movies"]:
            movie_titles.append(movie["title"].lower())

        while True:
            try:
                name = input("\nEnter movie name: ")
                if len(name) < 1:
                    raise ValueError("Please enter a name!")
                if exists:
                    if name.lower() not in movie_titles:
                        raise ValueError("Movie doesn't exists!")
                else:
                    if name.lower() in movie_titles:
                        raise ValueError("Movie name already exists!")

                break
            except ValueError as e:
                print(e)
        return name


    def get_valid_existing_name(self, movies: dict) -> str:
        """get a name (case-insensitive) of an existing movie"""
        name = self.get_valid_title(movies, True)
        return name


    def get_valid_new_name(self, movies: dict) -> str:
        """name not an empty string, to prevent accidental enter taps, and that it's not existing"""
        name = self.get_valid_title(movies, False)
        return name

    @staticmethod
    def get_valid_year() -> int:
        """validate that release year is a number and is within bounds"""
        year = 0
        while True:
            try:
                year = int(input(f"\nEnter movie release year, full years ({MOVIES_INVENTED} to {CURRENT_YEAR}): "))
                if year < MOVIES_INVENTED or year > CURRENT_YEAR:
                    raise ValueError()
                break
            except ValueError:
                print("\nInvalid year, please enter a number within range")

        return year

    @staticmethod
    def get_valid_rating() -> float:
        """validate that rating is a number and is within bounds"""
        rating = 0
        while True:
            try:
                rating = float(input("\nEnter movie rating, decimals allowed (1-10): "))
                if rating < 1 or rating > 10:
                    raise ValueError()
                break
            except ValueError:
                print("\nInvalid rating, please enter a number within range")

        return rating
