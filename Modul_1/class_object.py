class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} (NIDN: {self.nidn}) mengajar mata kuliah {mata_kuliah}"


# Pembuatan object Dosen
dosen1 = Dosen("Dr. Andi Wijaya", "00112233")
dosen2 = Dosen("Prof. Rina Kusuma", "00445566")

print(dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))
print(dosen2.ajar_mata_kuliah("Struktur Data"))