class BankAccount:
    __no = ""
    __saldo  = 0

    def __init__ (self,no):
        self.__no = no

    @property
    def no(self):
        return self.__no

    @property
    def saldo(self):
        return self.__saldo

    def topUp(self,saldo_topup):
        self.__saldo = self.__saldo + saldo_topup

    def tarik_tunai(self,saldo_tarik_tunai):
        if saldo_tarik_tunai > self.__saldo:
            raise ValueError("Saldo Tidak Cukup")
        
        self.__saldo = self.__saldo - saldo_tarik_tunai


account1 = BankAccount("Aldi")
print(account1.saldo)

account1.topUp(1000)
print(account1.saldo)

account1.tarik_tunai(500)
print(account1.saldo)
