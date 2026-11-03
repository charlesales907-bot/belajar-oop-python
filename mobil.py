class Mobil:

    def __init__(self, roda, mesin, body):
        print("Mobil dibuat")
        self.roda = roda
        self.mesin = mesin
        self.body = body

    def maju(self):
        print("maju..")
    
    def mundur(self):
        print("mundur..")

    def belok(self):
        print("belok..")

    def berhenti(self):
        print("berhenti..")

kijang = Mobil(4,1,1)
kijang.maju()
kijang.mundur()
print(f"roda: {kijang.roda}")