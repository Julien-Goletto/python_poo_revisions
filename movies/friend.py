class Friend:
    def __init__(self, name, borrowed_movie=None):
        self.name = name
        self.borrowed_movie = borrowed_movie
        """If a movie is borrowed, let's complete the where attribute with a friend object"""
        if self.borrowed_movie:
            print(f"{name} borrowed {borrowed_movie}")
            borrowed_movie.where = self

    def __str__(self) -> str:
        return f"{self.name}"
    
    def __repr__(self) -> str:
        return self.__str__()
    
class FriendsCleaner:

    NAME_INDEX = 0
    MOVIE_INDEX = 1

    def __init__(self, friends):
        self.friends = friends

    def generate(self, library):

        cleaned_friends = []

        for friend in self.friends:
            name = friend[self.NAME_INDEX]
            print(friend)
            if len(friend) == 1 :
                movie = None
            else: movie = library.find_by_title(friend[self.MOVIE_INDEX])
            
            cleaned_friends.append(Friend(name, movie))

        return cleaned_friends
    
friends = [
    ("Paul", "Blade Runner"),
    ("Lucie",),
    ("Zoé", "Terminator 2 : Le Jugement dernier"),
]