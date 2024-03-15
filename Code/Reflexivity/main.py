class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Salut, je m’apele", self.name)

# Créer une instance de la classe Person
person = Person("Abdoul-Wahabu harouna Tiambou", 30)

# Utiliser la réflexivité pour inspecter dynamiquement les attributs de l'objet
print("Attributs de l’objet:")
for attr in dir(person):
    if not attr.startswith("__"):
        print(attr, ":", getattr(person, attr))

# Utiliser la réflexivité pour appeler dynamiquement une méthode de l'objet
method_name = "greet"
if hasattr(person, method_name):
    method = getattr(person, method_name)
    method()


