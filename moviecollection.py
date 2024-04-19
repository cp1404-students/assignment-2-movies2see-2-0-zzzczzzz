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
