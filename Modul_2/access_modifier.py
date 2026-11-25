class ProgramStudi:
    def __init__(self, kode, ketua):
        self.kode = kode                # public
        self._ketua = ketua             # protected
        self.__anggaran = 500000000     # private

    # Getter protected
    def get_ketua(self):
        return self._ketua

    # Setter protected
    def set_ketua(self, nama_baru):
        if not nama_baru:
            raise ValueError("Nama ketua tidak boleh kosong.")
        self._ketua = nama_baru

    # Getter private
    def get_anggaran(self):
        return self.__anggaran

    # Setter private
    def set_anggaran(self, nilai):
        if nilai < 0:
            raise ValueError("Anggaran tidak boleh negatif.")
        self.__anggaran = nilai

    def kurangi_anggaran(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah harus positif.")
        if jumlah > self.__anggaran:
            raise ValueError("Anggaran tidak mencukupi.")
        self.__anggaran -= jumlah
        return self.__anggaran


class Mahasiswa:
    def __init__(self, nim, nama, semester=1, ipk=0.0):
        self.nim = nim                  # public
        self.nama = nama                # public
        self._semester = semester       # protected
        self.__ipk = ipk                # private

    # Getter & Setter semester (protected)
    def get_semester(self):
        return self._semester

    def set_semester(self, semester_baru):
        self._semester = semester_baru

    # Getter & Setter IPK (private)
    def get_ipk(self):
        return self.__ipk

    def set_ipk(self, ipk_baru):
        self.__ipk = ipk_baru


if __name__ == "__main__":
    # Contoh penggunaan ProgramStudi dari modul
    ps = ProgramStudi("TI", "Pak Wayan")
    print("Kode:", ps.kode)
    print("Ketua Prodi:", ps.get_ketua())
    print("Anggaran:", ps.get_anggaran())

    ps.set_ketua("Bu Diah")
    print("Ketua Prodi (baru):", ps.get_ketua())

    ps.kurangi_anggaran(100000000)
    print("Anggaran Tersisa:", ps.get_anggaran())
    print("-" * 40)

    # Latihan Praktikum b: Buat 2 objek Mahasiswa dan tampilkan atributnya
    mhs1 = Mahasiswa("230101", "Rina", 3, 3.65)
    mhs2 = Mahasiswa("230102", "Dimas", 5, 3.20)

    print("Mahasiswa 1 -> NIM:", mhs1.nim, "| Nama:", mhs1.nama,
          "| Semester:", mhs1.get_semester(), "| IPK:", mhs1.get_ipk())
    print("Mahasiswa 2 -> NIM:", mhs2.nim, "| Nama:", mhs2.nama,
          "| Semester:", mhs2.get_semester(), "| IPK:", mhs2.get_ipk())

    # Latihan Praktikum c: Ganti semester dan IPK
    mhs1.set_semester(4)
    mhs1.set_ipk(3.80)
    mhs2.set_semester(6)
    mhs2.set_ipk(3.45)

    print("\nSetelah diubah:")
    print("Mahasiswa 1 -> NIM:", mhs1.nim, "| Nama:", mhs1.nama,
          "| Semester:", mhs1.get_semester(), "| IPK:", mhs1.get_ipk())
    print("Mahasiswa 2 -> NIM:", mhs2.nim, "| Nama:", mhs2.nama,
          "| Semester:", mhs2.get_semester(), "| IPK:", mhs2.get_ipk())