# membuat class hewan 
# cth: class animal:
class Animal:

# membuat method contrusctor
# diisi dengan sebuah atribut, atribut name, age, dan species
    def __init__(self, name:str, age:int, species:str,):
        self.name = name
        self.age = age
        self.species = species
# membuat instance method 
class Cat(Animal):
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"

    def suara(self):
        return "Meow"
myCat = Cat("Neko", 3, "Persian")

print(myCat.deskripsi())
print(myCat.suara())