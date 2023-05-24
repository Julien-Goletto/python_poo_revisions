from pprint import pprint
from movies.data import friends
from movies.library import Library
from movies.friend import Friend, FriendsCleaner

my_library = Library()

my_friends = FriendsCleaner(friends).generate(my_library)

pprint(my_library.movies)
pprint(my_friends)
pprint(my_library.find_by_title("Blade Runner").where)