import re

class UserException(Exception):
    pass

class UserNameLengthUserException(UserException):
    def __init__(self, message="Le nom d'utilisateur doit comporter au moins 3 caractères", *args, **kwargs):
        super().__init__(message, *args, **kwargs)

class UnsecuredPasswordUserException(UserException):
    def __init__(self, message="Le mot de passe n'est pas sécurisé", *args, **kwargs):
        super().__init__(message, *args, **kwargs)

REGEX_PATTERN = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

def is_name_length_sufficient(name):
  if len(name) <= 3:
      raise UserNameLengthUserException()

def is_password_secure(password):
    if not re.fullmatch(REGEX_PATTERN, password):
        raise UnsecuredPasswordUserException()    

class User:
    def __init__(self, username, password):
        is_name_length_sufficient(username)
        is_password_secure(password)

        self.username = username
        self.password = password

    def __str__(self) -> str:
        return f"Username: {self.username}, Password: {self.password}"
    def __repr__(self) -> str:
        return f"Username: {self.username}, Password: {self.password}"

def main():
    users = [
        # User("Ju", "JemapelleJulien!1"),
        # User("Julien", "toto"),
        User("Audrey", "JemapelleAudrey!1"),
    ]
    print(users)

main()