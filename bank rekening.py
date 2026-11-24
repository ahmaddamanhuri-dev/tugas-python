class BankAccount:
    def __init__(self, no, saldo=0):
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")
        self.no = no
        self.saldo = saldo

# 1. Objek Martin (Sukses)
martin = BankAccount("1234567", 1000)
print("No Rekening Martin:", martin.no)
print("Saldo Martin:", martin.saldo)
print("Sukses")
print("-" * 30)

# 2. Objek Eko (Error / Saldo negatif)
try:
    eko = BankAccount("1234567", -1000)
    print("No Rekening Ahmad:", eko.no)
    print("Saldo Ahmad:", eko.saldo)
except ValueError as e:
    print("Error pada Ahmad:", e)