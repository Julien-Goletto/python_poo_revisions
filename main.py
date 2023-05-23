"""Contacts.

Séparez le programme en plusieurs modules et packages,
en ajoutant les fichiers __init__.py et les imports si necessaire.

Vérifiez que le programme s'éxecute correctement en lancant main.py depuis la racine
du projet.
"""

from contact.user import User
from contact.textcontact import TextContactSystem
from contact.owlcontact import OwlContactSystem
from contact.helpers import send_mass_messages

# Our main program.
alice = User("Alice", TextContactSystem("0102030405"))
bob = User("Bob", OwlContactSystem("4 Privet Drive"))

user_list = [alice, bob]
send_mass_messages("Hello {name}, Comment vas-tu?", user_list)
send_mass_messages(
    "Salut {name}. Tes informations de contact sont-elles corrects?"
    " Nous avons celles-ci: {contact_info}.",
    user_list,
)