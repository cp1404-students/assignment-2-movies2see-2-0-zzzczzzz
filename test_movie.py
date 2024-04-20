"""(Incomplete) Tests for Movie class."""
from movie import Movie


def run_tests():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")
    default_movie = Movie("", 0, "")
    print(default_movie)
    assert default_movie.title == ""
    assert default_movie.category == ""
    assert default_movie.year == 0
    assert not default_movie.is_watched

    # Test initial-value movie
    print("Test initial-value movie:")
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", True)
    # TODO: Write tests to show this initialisation works

    print(initial_movie)
    assert initial_movie.title == "Thor: Ragnarok"
    assert initial_movie.category == "Comedy"
    assert initial_movie.year == 2017
    assert initial_movie.is_watched

    # TODO: Add more tests, as appropriate, for each method

    # Test mark_as_watched
    print("Test mark_as_watched:")
    initial_movie.mark_as_unwatched()
    print(initial_movie)
    assert not initial_movie.is_watched
    initial_movie.mark_as_watched()
    print(initial_movie)
    assert initial_movie.is_watched

    # Test mark_as_unwatched
    print("Test mark_as_unwatched:")
    default_movie.mark_as_watched()
    print(default_movie)
    assert default_movie.is_watched
    default_movie.mark_as_unwatched()
    print(default_movie)
    assert not default_movie.is_watched


run_tests()
