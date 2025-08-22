import json


class MovieStorage:
    def __init__(self, filepath="data.json"):
        self.file_path = filepath

    def get_movies(self) -> dict:
        """loads movie list from json file"""
        with open('data.json', 'r') as handle:
            return json.load(handle)

    def save_movies(self, movies: dict) -> None:
        """saves changes to json file"""
        with open('data.json', 'w') as handle:
            json.dump(movies, handle, indent=4)

    def add_movie(self, title: str, year: int, rating: float) -> None:
        """adds movie and stats to file"""
        existing_movies = self.get_movies()
        new_movie = {
            'title': title,
            'year': year,
            'rating': rating,
        }
        existing_movies['movies'].append(new_movie)
        self.save_movies(existing_movies)

    def delete_movie(self, title: str) -> None:
        """removes movie from file list"""
        existing_movies = self.get_movies()
        for item in existing_movies['movies']:
            if item['title'].lower() == title.lower():
                existing_movies['movies'].remove(item)
                break

        self.save_movies(existing_movies)

    def update_movie(self, title: str, rating: float) -> None:
        """updates movie rating in list"""
        existing_movies = self.get_movies()
        for item in existing_movies['movies']:
            if item['title'].lower() == title.lower():
                item['rating'] = float(rating)
                break

        self.save_movies(existing_movies)
