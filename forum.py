class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def display(self):
        print(f"Fichier : {self.name}")

class ImageFile(File):
    pass

# Thread has a title, a creation_date and a post collection
class Thread:
    def __init__(self, title, creation_date, post):
        self.title = title
        self.creation_date = creation_date
        self.posts = [post]

    def display(self):
        print('----- Thread -----')
        print(f"{self.title}, date: {self.creation_date}")
        for post in self.posts:
            print(post.display())
            print()
            print('----------------------------------------')
    def add_post(self, post):
        self.posts.append(post)

# Post has a text, an author and a creation_date.
class Post:
    def __init__(self, text, author, creation_date):
        self.text = text
        self.author = author
        self.creation_date = creation_date
    
    def display(self):
        print(f"Published by{self.author}, the {self.creation_date}")
        print(self.text)

# Post with an attached file (image)
class FilePost(Post):
    def __init__(self, text, author, creation_date, file):
      self.text = text
      self.author = author
      self.creation_date = creation_date
      self.file = file

    def display(self):
        print(f"Published by{self.author}, the {self.creation_date}")
        print(self.text)
        self.file.display()  

# User has a name, password. It can register, connect, create_thread, post_message
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def register(self):
        print(f"User account {self.name} has been created.")

    def login(self):
        print(f"Welcome back {self.name}.")

    def create_thread(self, title, creation_date, first_post_text):
        post = Post(first_post_text, self.name, creation_date)
        return Thread(title, creation_date, post)
    
    def post_message(self, thread, text, creation_date, file=None):
        if file:
            post = FilePost(text, self.name, creation_date, file)
        else:
            post = Post(text, self.name, creation_date)

        thread.add_post(post)
        return post
    
    def __str__(self):
        return self.name

# Moderator is derived from User. It can also modify_post and delete_post
class Moderator(User):
    def edit(self, post, text):
        post.text = text
    def delete(self, thread, post):
        del thread[thread.posts.index(post)]
