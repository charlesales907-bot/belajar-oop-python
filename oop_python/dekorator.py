class Matematika:
    "@ namanya dekorator"
    "@staticmethod digunakan untuk memanggil method di dalam class tanpa perlu membuat class baru"
    @staticmethod
    def tambah(a,b):
        return a + b

result = Matematika.tambah(3,2)
print(result)


class BankAccount:
    no = " "
    balance = 0
    active = True

    def __init__(self,no,balance=0):
        self.no = no
        self.balance = balance

    "classmethod digunakan untuk membuat objek baru didalam method itu sendiri"
    @classmethod
    def disabled(cls,no, balance=0):
        result = cls(no,balance)
        result.active = False
        return result

bank_account1 = BankAccount("12345",10000)
print(bank_account1.no, bank_account1.balance, bank_account1.active )

bank_account2 = BankAccount.disabled("1234",1000)
print(bank_account2.no, bank_account2.balance, bank_account2.active )


class Category:
    "penggunaan _ untuk menandakan agar atribut ini jangan diakses langsung"
    _name = ""

    "penggunaan fungsi getter"
    @property
    def name(self):
        return self._name

    "penggunaan fungsi setter"
    @name.setter
    def name(self,name):
        if name == "":
            raise ValueError("Nama Tidak boleh kosong")
        self._name = name
        
category1 = Category()
category1.name = "Aldi"
print(category1.name)


def sapaan(fungsi):
    def wrapper():
        print("Halooo kamu")
        fungsi()
        print("selesai")
    return wrapper

"balasan = sapaan(balasan)"
@sapaan 
def balasan():
    print("Halo jugaa")

balasan()

