from pprint import pprint

from movies.library import Library
from movies.movie import MovieVHF, MovieDVD, MovieCleaner
from movies.friend import Friend

my_library = Library()
pprint(my_library.movies)

