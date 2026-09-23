# ==============================================================================
# ENCAPSULATION (PENGKAPSULAN)
# Pembungkusan data (atribut) dan perilaku (method) ke dalam satu kesatuan (class).
# ==============================================================================

# CLASS (Blueprint / Cetakan)
# Template untuk membuat objek. Mendefinisikan atribut dan method yang dimiliki objek.

class Kampus:
    """Blueprint untuk membuat data Kampus."""
    
    # Class Attribute (Atribut yang ditempel langsung ke Class)
    # Catatan: Atribut ini akan dibagikan (shared) ke semua instance/objek.
    nama = " "
    alamat = " "

class Mahasiswa:
    """Blueprint untuk membuat data Mahasiswa."""
    
    # Class Attribute (Secara umum di Python, atribut unik tiap mahasiswa 
    # idealnya diinisialisasi di dalam method __init__)
    nim = 0
    nama = ""

    # METHOD (Fungsi di dalam Class)
    # Parameter 'self' wajib ada sebagai parameter pertama.
    # 'self' merujuk pada objek (instance) spesifik yang sedang memanggil method tersebut.
    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")

        """
        Method dengan parameter tambahan.
        Catatan: Nama parameter bebas (misal: 'nama_lawan_bicara'), tetapi 
        posisi pertama HARUS 'self' agar tidak bingung dengan atribut self.nama.
        """
    def hello(self, nama):
        print("hallo",nama,"nama saya adalah",self.nama)    

# ==============================================================================
# OBJECT / INSTANCE
# Objek nyata hasil cetakan dari sebuah Class.
# ==============================================================================

# Instansiasi: Membuat objek 'kampus1' dan 'kampus2' dari class Kampus
kampus1 = Kampus()
print(kampus1.nama)
print(kampus1.alamat)

kampus2 = Kampus()

# Cek tipe data objek (output: <class '__main__.Kampus'>)
print(type(kampus1))
print(type(kampus2))

# INSTANCE ATTRIBUTE
# Memberikan nilai/properti khusus yang menempel pada objek spesifik tertentu.
# Format: nama_objek.nama_atribut = nilai

#objek 1: mahasiswa 1
mahasiswa1 = Mahasiswa()
mahasiswa1.nim = 12345
mahasiswa1.nama = "budi"
mahasiswa1.perkenalan()
mahasiswa1.hello("Charles")

print(mahasiswa1.nim)
print(mahasiswa1.nama)

#Objek 2: mahasiswa 2
mahasiswa2 = Mahasiswa()
mahasiswa2.nim = 45678
mahasiswa2.nama = "andi"
mahasiswa2.perkenalan()
mahasiswa2.hello("Charles")

print(mahasiswa2.nim)
print(mahasiswa2.nama)

print(type(mahasiswa1))
print(type(mahasiswa2))