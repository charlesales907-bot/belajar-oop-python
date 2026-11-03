class Kendaraan:

    def __init__(self,merk,tahun):
        self.merk = merk
        self.tahun = tahun

    def info (self):
        return f"Merek: {self.merk}, Tahun: {self.tahun}"

    def nyalakan(self):
        print(f"Merek: {self.merk} bisa dinyalakan")

"cara membuat sebuah child class"
class Mobil(Kendaraan):

    def __init__(self, merk, tahun, jumlah_roda):
        super().__init__ (merk,tahun)
        self.jumlah_roda = jumlah_roda

    def klakson(self):
        print(f"Mobil {self.info()} bisa menggunakan klakson")

class Motor(Kendaraan):

    def klakson(self):
        print(f"Motor {self.info()} bisa menggunakan klakson")

    "Mendefinisikan ulang sebuah method di child class = method overriding"
    "Untuk mengakses method di parent perlu super()"

    def nyalakan(self):
        print(f"Merek: {self.merk} bisa dinyalakan otomatis")


avansa = Mobil("Avansa",2019,4)
avansa.klakson()
avansa.nyalakan()
print(f"Mobil ini punya {avansa.jumlah_roda} roda")

beat = Motor("Beat", 2010)
beat.klakson()
beat.nyalakan()


"Multilevel"
"inheritance chain"
class Karyawan():

    def __init__(self,nama, gaji):
        self.nama = nama
        self.gaji = gaji
class KaryawanTetap(Karyawan):
    pass

class Manager(KaryawanTetap):
    pass


"Multiple Inheritance"
class Berlari:

    def berlari(self):
        print("bisa berlari cepat")

class Berenang:

    def berenang(self):
        print("bisa berenang cepat")

class Atlit(Berlari, Berenang):

    def __init__(self, nama):
        self.nama = nama

eko = Atlit("Eko")
eko.berenang()
eko.berlari()

andi = Karyawan("Andi", 1000)
budi = KaryawanTetap("Budi", 1000)

"Type checking apakah object ini sesuai dengan class yang ditentukan"

print(isinstance(andi, Karyawan))
print(isinstance(budi, Karyawan))