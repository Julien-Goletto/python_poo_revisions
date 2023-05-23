class Movie:
    def __init__(self, name, release_date):
        self.name = name
        self.release_date = release_date
        """attribute initialisation"""
        self.where = None

    def __str__(self) -> str:
        return f"{self.name} ({self.release_date})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
class MovieVHF(Movie):
    type = 'vhf'

    def __init__(self, name, release_date):
        super().__init__(name, release_date)
        self.magnetic_tape = True

class MovieDVD(Movie):
    type = 'dvd'

    def __init__(self, name, release_date):
        super().__init__(name, release_date)
        self.mega_bytes = 4700

class MovieCleaner:
    NAME_AND_DATE_INDEX = 0
    TYPE_INDEX = 1

    def __init__(self, movie_data):
        self.movie_data = movie_data

    def generate(self):
        name = self.generate_name()
        release_date = self.generate_release_date()
        type = self.generate_type()

        for Film in [MovieVHF, MovieDVD]:
            if type == Film.type:
                return Film(name, release_date)
    
    def generate_name(self):
        title_and_date = self.movie_data[self.NAME_AND_DATE_INDEX]
        return title_and_date[: title_and_date.index("(")].strip()
    
    def generate_release_date(self):
        title_and_date = self.movie_data[self.NAME_AND_DATE_INDEX]
        return title_and_date[title_and_date.index("(") :].strip().replace("(", "").replace(")", "")
    
    def generate_type(self):
        return self.movie_data[self.TYPE_INDEX].lower()