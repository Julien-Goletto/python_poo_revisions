from .data import movies, friends
from .movie import MovieCleaner

class Library:
    def __init__(self):
        self.movies = []
        for movie in movies:
            cleaned_movie = MovieCleaner(movie).generate()
            self.movies.append(cleaned_movie)
    
    def sort_by_name(self):
        self.movies.sort(key=lambda movie: movie.name)

    def find_by_title(self, movie_title):
        return next((movie for movie in self.movies if movie.name == movie_title), None)