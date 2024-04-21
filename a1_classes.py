"""..."""
# TODO: Copy your first assignment to this file, then update it to use Movie class

from movie import Movie
from moviecollection import MovieCollection


def main():
    """Main function to manage the movie manager program"""
    movies = load_movies()
    print("Welcome to Movie Manager, my name is Yunseo Choi")
    print(f"{len(movies)} movies loaded")
    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":

        if choice == "D":
            display_movies(movies)
        elif choice == "A":
            add_movie(movies)
        elif choice == "W":
            watch_movie(movies)
        else:
            print("Invalid input")

        print(MENU)

        choice = input("Enter your choice: ").upper()

    save_movies(movies)
    print(f"{len(movies)} saved")


def load_movies():
    """Load movies from file"""
    movies = []
    with open('movies.csv', 'r') as file:
        for line in file:
            title, year, category, watched = line.strip().split(',')
            movie = Movie(title, int(year), category, watched == 'True') # Movie Class used to store in thie line
            movies.append(movie)
    return movies



def save_movies(movies):
    """Save movies to file"""
    with open('movies.csv', 'w') as file:
        for movie in movies:
            file.write(f"{movie.title},{movie.year},{movie.category},{movie.watched}\n")
