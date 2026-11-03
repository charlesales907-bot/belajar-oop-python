class Hewan:

    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Hewan bersuara")

class Anjing(Hewan):

    def suara(self):
        print(f"{self.nama}: guk guk")

class Kucing (Hewan):

    def suara(self):
        print(f"{self.nama}: meow meow")

class Sapi (Hewan):

    def suara(self):
        print(f"{self.nama}: moo...")

hewan_list = [
    Anjing("Anjing"),
    Kucing("Kucing"),
    Sapi("Sapi")
]

for hewan in hewan_list:
    hewan.suara()

"Duck Typing"
class Mobil:
    def start(self):
        print("Mobil Berjalan")

class Motor:
    def start(self):
        print("Motor Berjalan")

class Perahu:
    def start(self):
        print("Perahu Berjalan")

def operasikan_kendaraan(kendaraan):
    kendaraan.start()

kendaraan_list = [
    Mobil(),
    Motor(),
    Perahu()
]

for kendaraan in kendaraan_list:
    operasikan_kendaraan(kendaraan)

"Operator Overloading"

class Apple:
    def __init__(self, jumlah):
        self.jumlah = jumlah

    def __add__(self, other):
        return Apple(self.jumlah + other.jumlah)

    def __str__(self):
        return f"Apple:{self.jumlah}"


apple1 = Apple(10)
apple2 = Apple(20)
apple3 = apple1 + apple2
print(apple3)


"Abstract Base Class"
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def luas():
        pass

class Persegi_panjang(Shape):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

class Persegi(Shape):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

luas_bangun = [
    Persegi_panjang(10,4),
    Persegi(10)
]

for i in luas_bangun:
    print(i.luas())