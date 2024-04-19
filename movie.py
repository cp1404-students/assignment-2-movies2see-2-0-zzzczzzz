"""..."""


# TODO: Create your Movie class in this file

class Movie:
    """Initial value for class Movie, set watched statue as fault for default"""
    def __init__(self, title, year, category, is_watched=False):
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        """Create return str for Movie, prinit watched or unwatched refering to watch statue"""
        return f"{self.title} ({self.year}) - {self.category} {'(Watched)' if self.is_watched else '(Unwatched)'}"
