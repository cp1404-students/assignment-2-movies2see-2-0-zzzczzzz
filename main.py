"""
Name:Yunseo Choi
Date:21/04/2024
Brief Project Description:Kivy app for movie managing
GitHub URL:https://github.com/cp1404-students/assignment-2-movies2see-2-0-zzzczzzz/edit/main/main.py
"""
# TODO: Create your main program in this file, using the Movies2SeeApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label

from movie import Movie
from moviecollection import MovieCollection


def get_button_color(is_watched):
    """Return button color based on watched status"""
    return (0.2, 0.8, 0.2, 1) if is_watched else (0.8, 0.2, 0.2, 1)


class MovieApp(App):
    """Main Kivy app class"""

    def __init__(self, **kwargs):
        """Initialize the app"""
        super().__init__(**kwargs)
        self.movie_collection = MovieCollection()

    def build(self):
        """Build the Kivy app"""
        self.title = "Movie Manager"
        self.root = Builder.load_file('app.kv')
        self.root.ids.sort_spinner.bind(text=self.sort_movies)
        self.movie_collection.load_movies("movies.json")
        self.layout_movies()
        return self.root

    def sort_movies(self, spinner, text):
        """Sort the movies based on the selected sorting criteria"""
        sorting_keys = {
            'Title': 'title',
            'Year': 'year',
            'Category': 'category',
            'Watched': 'is_watched'
        }
        key = sorting_keys.get(text)
        if key:
            self.movie_collection.sort(key)
            self.layout_movies()

    def layout_movies(self):
        """Layout movies in the movie list"""
        movies_layout = self.root.ids.movies_layout
        movies_layout.clear_widgets()
        for movie in self.movie_collection.movies:
            movie_button = Button(text=f"{movie.title} ({movie.category}, {movie.year})",
                                  background_color=get_button_color(movie.is_watched))
            movie_button.movie = movie  # Assign movie as an attribute
            movie_button.bind(on_press=self.on_movie_button_press)
            movies_layout.add_widget(movie_button)

            movies_layout.add_widget(Label())

    def on_movie_button_press(self, button):
        """Handler for movie button press event"""
        movie = button.movie
        self.toggle_status(movie)

    def toggle_status(self, movie):
        """Toggle the watched status of a movie"""
        movie.is_watched = not movie.is_watched
        self.layout_movies()

    def add_movie(self, title, category, year):
        """Add a new movie to the collection"""
        if not title or not category or not year:
            self.display_message("All fields must be completed")
            return

        try:
            year = int(year)
        except ValueError:
            self.display_message("Please enter a valid number for the year")
            return

        if category not in ["Action", "Comedy", "Documentary", "Drama", "Fantasy", "Thriller"]:
            self.display_message(
                "Invalid category. Please choose from: Action, Comedy, Documentary, Drama, Fantasy, Thriller")
            return

        new_movie = Movie(title, year, category)
        self.movie_collection.add_movie(new_movie)
        self.layout_movies()
        self.display_message("Movie added!")

    def on_stop(self):
        """Called when the application is about to stop"""
        self.movie_collection.save_movies()

    def display_message(self, message):
        """Display a message in the message label"""
        self.root.ids.message_label.text = message

    def clear_fields(self):
        """Clear text input fields"""
        self.root.ids.title_input.text = ''
        self.root.ids.category_input.text = ''
        self.root.ids.year_input.text = ''
        self.root.ids.message_label.text = ''


if __name__ == "__main__":
    MovieApp().run()

