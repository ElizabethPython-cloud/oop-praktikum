class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def perkenalan_diri(self):
        return (
            f"Halo, saya {self.nama} (NIM: {self.nim}) "
            f"dari jurusan {self.jurusan}, {self.universitas} dengan IPK {self.ipk:.2f}."
        )

    def update_ipk(self, ipk_baru):
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            return f"IPK {self.nama} berhasil diperbarui menjadi {self.ipk:.2f}."
        return "IPK harus berada di antara 0.0 dan 4.0."

    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        if self.ipk >= 3.0:
            return "Sangat Memuaskan"
        if self.ipk >= 2.5:
            return "Memuaskan"
        if self.ipk >= 2.0:
            return "Lulus"
        return "Belum Lulus"


# Instansiasi 3 object mahasiswa dengan data berbeda
mhs1 = Mahasiswa("Tiara", "202512034", "Teknik Informatika", 3.75)
mhs2 = Mahasiswa("Yusuf", "202512046", "Sistem Informasi", 3.20)
mhs3 = Mahasiswa("Fahri", "202512003", "Teknik Elektro", 2.35)

daftar_mahasiswa = [mhs1, mhs2, mhs3]

# Demonstrasi perkenalan_diri() dan predikat_kelulusan()
print("=== Data Awal Mahasiswa ===")
for mhs in daftar_mahasiswa:
    print(mhs.perkenalan_diri())
    print(f"Predikat Kelulusan: {mhs.predikat_kelulusan()}\n")

# Demonstrasi update_ipk()
print("=== Pembaruan IPK ===")
print(mhs2.update_ipk(3.60))
print(f"{mhs2.nama} - Predikat baru: {mhs2.predikat_kelulusan()}")

print(mhs3.update_ipk(2.85))
print(f"{mhs3.nama} - Predikat baru: {mhs3.predikat_kelulusan()}")
