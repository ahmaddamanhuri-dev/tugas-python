class Sekolah:
    pass

class Siswa:
    pass

Kepala_sekolah = Sekolah()
Orang_tua = Siswa()

print(type(Kepala_sekolah))
print(type(Orang_tua))

Sir_adam = Sekolah()
Abdul = Siswa()

print(type(Sir_adam))
print(type(Abdul))

Kepala_sekolah = Sekolah()
Kepala_sekolah.umur = 25
Kepala_sekolah.nama = "Ahmad"

print(Kepala_sekolah.umur)
print(Kepala_sekolah.nama)

Orang_tua = Siswa()
Orang_tua.umur = 50
Orang_tua.nama = "Haji Damanhuri"

print(Orang_tua.umur)
print(Orang_tua.nama)