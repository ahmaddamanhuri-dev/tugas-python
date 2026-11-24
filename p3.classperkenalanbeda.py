class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nama, nim): 
        self.nama = nama
        self.nim = nim



mhs = Mahasiswa("Ahmad", "14022500018")
print(mhs.nama)
print(mhs.nim)