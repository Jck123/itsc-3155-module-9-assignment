# TODO: Feature 2
from src.repositories.movie_repository import movie_repository_singleton
from src.models.movie import Movie

def test_create_movie():
    movie = movie_repository_singleton.create_movie('Spider-Man: No Way Home', 'Jon Watts', 5)
    assert type(movie) == Movie
    assert movie.title == 'Spider-Man: No Way Home'
    assert movie.director =='Jon Watts'
    assert movie.rating ==5
    assert movie_repository_singleton.get_movie_by_title('Spider-Man: No Way Home') != None