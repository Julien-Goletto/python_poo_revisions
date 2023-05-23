from abc import ABC

class File(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def display(self):
        print(f"Fichier : {self.name}")

class ImageFile(File):
    pass

class JPEGImageFile(ImageFile):
    def display(self):
        super().display()
        print('Image au format JPEG')

class PNGImageFile(ImageFile):
    def display(self):
        super().display()
        print('Image au format PNG')

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
        print(f"Published by {self.author}, the {self.creation_date}")
        print(self.text)

# Post with an attached file (image)
class FilePost(Post):
    def __init__(self, text, author, creation_date, file):
      super().__init__(text, author, creation_date)
      self.file = file

    def display(self):
        super().display()
        print("Attached file :")
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
        del thread.posts[thread.posts.index(post)]


# Test

# jpeg_1 = JPEGImageFile("mon image 1", 80)

# png_1 = PNGImageFile("mon image 2", 160)
# print(png_1.display())

# user = User('Julien', 'monmotdepasse')
# user.register()
# user.login()
# thread = user.create_thread("J'aime les financiers au chocolat", "Aujourd'hui", "Aujourd'hui j'ai mangé un financier au restaurant, c'était délicieux ! Et vous, aimez-vous ces gâteaux ?")

# admin = Moderator('Moderator', 'jesuisadminlol')
# admin.post_message(thread, "C'est un de mes gâteaux préférés, OMG", "Demain", jpeg_1)
# admin.edit(thread.posts[1], "C'est MON gâteau préféré, OMG !!!")

# thread.display()

# Utilisation chapitre final
def main():
  # Créez 1 utilisateur et un modérateur.
  users = {
      "user" : User('Julien', 'monmotdepasse'), 
      "admin" : Moderator('Moderator', 'jesuisadminlol'),
  }

  # L’utilisateur crée un fil de discussion (vous pouvez inventer les messages).
  thread = users["user"].create_thread(
      "J'aime les financiers au chocolat",
      "Aujourd'hui", "Aujourd'hui j'ai mangé un financier au restaurant, c'était délicieux ! Et vous, aimez-vous ces gâteaux ?"
  )

  # Le modérateur répond dans ce fil.
  jpeg_1 = JPEGImageFile("mon image 1", 80)
  users["admin"].post_message(thread, "C'est un de mes gâteaux préférés, OMG", "Demain", jpeg_1)

  # L’utilisateur répond dans ce même fil par un message hors sujet❗
  hs_post = users["user"].post_message(thread, "Par contre le céleri je n'y arrive pas, désolé", "Hier")

  # Le modérateur répond que c’est hors sujet, puis supprime le message de l’utilisateur et son dernier message.
  users["admin"].post_message(thread, "Attention, ici on parle de gâteau, tu es hors sujet et je vais devoir supprimer ce message", "Le surlendemain")
  users["admin"].delete(thread, hs_post)

  # L’utilisateur répond dans le fil en joignant une image.
  png_1 = PNGImageFile("mon image 2", 160)
  users["user"].post_message(thread, "Oui pardon, je me suis trompé de thread, quel distrait je fais !", "L'an dernier")

  thread.display()

main()