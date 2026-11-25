# relasi aggregation & association
class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []  # agregasi: Nilai dapat berdiri sendiri

    def tambah_nilai(self, nilai: Nilai):
        self.daftar_nilai.append(nilai)

    # Latihan poin f: method rata_rata() pada class Mahasiswa
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0.0
        return round(sum(n.skor for n in self.daftar_nilai) / len(self.daftar_nilai), 2)


class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []  # agregasi

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)


# relasi composition
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


def report_program(prodi: ProgramStudi, semua_mahasiswa: list[Mahasiswa]):
    print(f"Program Studi: {prodi.nama}")
    print("Matakuliah:", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]) or "-")
    print("Mahasiswa dan rata-rata nilai:")
    for m in semua_mahasiswa:
        relevan = [n for n in m.daftar_nilai if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)]
        if relevan:
            avg = sum(n.skor for n in relevan) / len(relevan)
            print(f"  {m.nim} {m.nama}: {round(avg, 2)}")
    print("-" * 40)


if __name__ == "__main__":
    uni = Universitas("Universitas A")

    # Prodi awal + Latihan a: tambah 2 Program Studi baru
    prodi_ti = uni.buat_program("Teknik Informatika")
    prodi_si = uni.buat_program("Sistem Informasi")
    prodi_te = uni.buat_program("Teknik Elektro")

    # Latihan b: minimal 2 Mata Kuliah pada masing-masing Program Studi
    mk1 = MataKuliah("TI101", "Pemrograman Dasar")
    mk2 = MataKuliah("TI102", "Struktur Data")
    prodi_ti.tambah_matakuliah(mk1)
    prodi_ti.tambah_matakuliah(mk2)

    mk3 = MataKuliah("SI201", "Analisis Sistem")
    mk4 = MataKuliah("SI202", "Basis Data")
    prodi_si.tambah_matakuliah(mk3)
    prodi_si.tambah_matakuliah(mk4)

    mk5 = MataKuliah("TE301", "Rangkaian Listrik")
    mk6 = MataKuliah("TE302", "Sistem Kendali")
    prodi_te.tambah_matakuliah(mk5)
    prodi_te.tambah_matakuliah(mk6)

    # Latihan c: buat 3 Mahasiswa & tambahkan beberapa objek Nilai
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")
    m3 = Mahasiswa("23003", "Rizky")

    # relasi association (Mahasiswa berelasi dengan Nilai/kode MK)
    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))

    m2.tambah_nilai(Nilai("TI101", 90))
    m2.tambah_nilai(Nilai("SI201", 88))
    m2.tambah_nilai(Nilai("SI202", 84))

    m3.tambah_nilai(Nilai("SI202", 80))
    m3.tambah_nilai(Nilai("TE301", 86))
    m3.tambah_nilai(Nilai("TE302", 92))

    semua_mahasiswa = [m1, m2, m3]

    # Latihan d: tampilkan daftar mata kuliah dari setiap Program Studi
    print("=== DAFTAR MATA KULIAH TIAP PROGRAM STUDI ===")
    for p in uni.programs:
        daftar_mk = ", ".join([f"{mk.kode} - {mk.nama}" for mk in p.daftar_matakuliah]) or "-"
        print(f"{p.nama}: {daftar_mk}")

    # Latihan e & f: tampilkan daftar nilai dan rata-rata setiap mahasiswa
    print("\n=== DAFTAR NILAI & RATA-RATA MAHASISWA ===")
    for m in semua_mahasiswa:
        rincian_nilai = ", ".join([f"{n.kode_mk}: {n.skor}" for n in m.daftar_nilai]) or "-"
        print(f"{m.nim} - {m.nama} | Nilai: [{rincian_nilai}] | Rata-rata: {m.rata_rata()}")

    # Latihan g: panggil report_program untuk setiap Program Studi
    print("\n=== LAPORAN PROGRAM STUDI ===")
    for p in uni.programs:
        report_program(p, semua_mahasiswa)