class Friend:
    def __init__(self, name, borrowed_movie=None):
        self.name = name
        self.borrowed_movie = borrowed_movie
        """If a movie is borrowed, let's complete the where attribute with a friend object"""
        if self.borrowed_movie:
            borrowed_movie.where = self

    def __str__(self) -> str:
        return f"{self.name}"
    
    def __repr__(self) -> str:
        return self.__str__()