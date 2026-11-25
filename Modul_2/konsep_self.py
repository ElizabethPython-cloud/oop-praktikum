class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    # Latihan a: tambah mahasiswa tanpa duplikasi NIM
    def tambah_mahasiswa(self, mhs):
        if any(item.nim == mhs.nim for item in self.mahasiswa):
            print(f"Mahasiswa dengan NIM {mhs.nim} sudah terdaftar di {self.kode}.")
            return False
        self.mahasiswa.append(mhs)
        return True

    # Latihan b: hapus mahasiswa berdasarkan NIM
    def hapus_mahasiswa(self, nim):
        for i, item in enumerate(self.mahasiswa):
            if item.nim == nim:
                dihapus = self.mahasiswa.pop(i)
                return dihapus
        return None

    # Latihan c: jumlah mahasiswa & daftar nama
    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    def info(self):
        return f"{self.kode} - {self.nama} ({self.jumlah_mahasiswa()} mahasiswa)"


if __name__ == "__main__":
    mk = MataKuliah("TI101", "Pemrograman Dasar")
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")

    mk.tambah_mahasiswa(m1)
    mk.tambah_mahasiswa(m2)
    mk.tambah_mahasiswa(Mahasiswa("23001", "Budi Duplikat"))  # ditolak

    print(mk.info())
    print(mk.daftar_mahasiswa())

    mk.hapus_mahasiswa("23001")
    print(mk.info())
    print(mk.daftar_mahasiswa())