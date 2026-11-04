"Exception"
"Membuat agar jika ada error di program tidak membuat program berhenti"
"Tapi membuat sebuah notifikasi errornya dimana"

class SaldoTidakCukup(Exception):
    def __init__(self,message):
        self.message = message

    def __str__(self):
        return self.message

class BankAccount:
    def __init__(self, no, saldo=0):
        self.no = no
        self.saldo = saldo

    def tranfer (self,tarik_tunai):

        if tarik_tunai > self.saldo:
            raise SaldoTidakCukup("Saldo Tidak Cukup")

        self.saldo = self.saldo - tarik_tunai

try:
    account1 = BankAccount("123456", 10000)
    account1.tranfer(2000000)
except SaldoTidakCukup as e:
    print(f"Saldo Tidak cukup: {e}")

print("Program Selesai")
  