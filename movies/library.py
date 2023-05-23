from .data import movies
from .movie import MovieCleaner

class Library:
    def __init__(self):
        self.movies = []
        for movie in movies:
          cleaned_movie = MovieCleaner(movie).generate()
          self.movies.append(cleaned_movie)

    
    def sort_by_name(self):
        self.movies.sort(key=lambda movie: movie.name)