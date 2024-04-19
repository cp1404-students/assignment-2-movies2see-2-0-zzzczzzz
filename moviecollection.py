"""..."""


# TODO: Create your MovieCollection class in this file

from movie import Movie
import json
from operator import itemgetter


class MovieCollection:
    def __init__(self):
        """Initial value for MovieCollection, emtpy string for movies"""
        self.movies = []

    def add_movie(self, title, year, category):
        """Add movie, error check each variable, import class Movie for storing"""
        if title == "" or year == "" or category == "":
            return "All fields must be completed"

        try:
            year = int(year)
        except ValueError:
            return "Please enter a valid number for the year"

        if category not in ["Action", "Comedy", "Documentary", "Drama", "Fantasy", "Thriller"]:
            return "Invalid category. Please choose from: Action, Comedy, Documentary, Drama, Fantasy, Thriller"

        movie = Movie(title, year, category)
        self.movies.append(movie)

    def get_number_of_unwatched_movies(self):
        """Calculate number of unwatched movies using sum"""
        return sum(movie.is_watched for movie in self.movies if not movie.is_watched)

    def get_number_of_watched_movies(self):
        """Calculate number of watched movies using sum"""
        return sum(movie.is_watched for movie in self.movies if movie.is_watched)

    def load_movies(self):
        """Load movies from file movies.json, use class Movie for proper load"""
        with open("movies.json", 'r') as file:
            movies_data = json.load(file)
            for movie_data in movies_data:
                movie = Movie(movie_data['title'], movie_data['year'], movie_data['category'], movie_data['is_watched'])
                self.movies.append(movie)

    def save_movies(self):
        """create new list with adding all new movies and exisiting moves, save them in json file"""
        movies_data = []
        for movie in self.movies:
            movies_data.append({
                'title': movie.title,
                'year': movie.year,
                'category': movie.category,
                'is_watched': movie.is_watched
            })
        with open("movies.json", 'w') as file:
            json.dump(movies_data, file)

    def sort(self, key):
        """sort movies by title using itemgetter"""
        self.movies.sort(key=itemgetter(key, 'title'))

