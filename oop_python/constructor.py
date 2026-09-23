class Mahasiswa():
    nama = ""
    nim = ""

    # 1. CONSTRUCTOR (__init__)
    # Method khusus yang otomatis dipanggil saat objek pertama kali dibuat (instansiasi).
    # Bertujuan untuk melakukan inisialisasi / setup awal nilai atribut objek.
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim

    # 2. STRING REPRESENTATION (__str__)
    # Special method yang menentukan tampilan teks saat objek di-print() 
    # atau diubah menjadi string str(objek).
    def __str__(self):
        return f"Mahasiswa: {self.nama} NIM: {self.nim}"

    # 3. OBJECT EQUALITY (__eq__)
    # Special method untuk membandingkan dua objek menggunakan operator kesamaan (==).
    # Mengembalikan True jika kondisi terpenuhi, dan False jika sebaliknya.
    # Parameter 'other' merujuk pada objek lawan yang sedang dibandingkan.
    def __eq__(self, other):
        return self.nim == other.nim and self.nama == other.nama

# Instansiasi objek pertama
mhs = Mahasiswa("Andika", 12345)

print(mhs.nama)
print(mhs.nim)

# Menggunakan __str__: Otomatis memanggil mhs.__str__() saat di-print
print(mhs)

# Instansiasi objek kedua dengan nilai yang sama
mhs2 = Mahasiswa("Andika", 12345)

# Menggunakan __eq__: Otomatis memanggil mhs.__eq__(mhs2)
# Tanpa __eq__, mhs == mhs2 akan bernilai False karena Python mengecek lokasi memori objek.
print(mhs == mhs2)

class BankAccount():
    no = ""
    saldo = 0

    # Constructor dengan Default Argument (saldo=0)
    # Jika saldo tidak diisi saat pemanggilan, nilainya otomatis 0.
    def __init__(self, no, saldo =0):

         # Validasi Data (Error Handling / Guard Clause)
        # Menolak pembuatan objek jika saldo bernilai negatif
        if saldo < 0:
            raise ValueError("Saldo harus positif")

        self.no = no
        self.saldo = saldo

# Objek berhasil dibuat karena saldo bernilai positif
alvin = BankAccount("1234567", 100000)
print(alvin.saldo)
print(alvin.no)

# Baris di bawah ini akan memicu ValueError dan menghentikan program
# valdi = BankAccount("1234543", -11111111) - error

