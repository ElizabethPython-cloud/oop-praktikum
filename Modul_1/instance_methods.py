class ManajerInventori:
    def __init__(self):
        self.inventori = {}

    def tambah_barang(self, nama_barang, jumlah):
        if jumlah <= 0:
            return "Jumlah barang harus positif"
        self.inventori[nama_barang] = self.inventori.get(nama_barang, 0) + jumlah
        return f"Berhasil menambah {jumlah} {nama_barang}. Stok: {self.inventori[nama_barang]}"

    def hapus_barang(self, nama_barang, jumlah=None):
        if nama_barang not in self.inventori:
            return f"Barang {nama_barang} tidak ditemukan di inventori"
        if jumlah is None:
            del self.inventori[nama_barang]
            return f"Barang {nama_barang} dihapus dari inventori"
        if jumlah <= 0:
            return "Jumlah pengurangan harus positif"
        if jumlah > self.inventori[nama_barang]:
            return f"Stok {nama_barang} tidak mencukupi (tersedia: {self.inventori[nama_barang]})"
        self.inventori[nama_barang] -= jumlah
        sisa = self.inventori[nama_barang]
        if sisa == 0:
            del self.inventori[nama_barang]
        return f"Berhasil mengurangi {jumlah} {nama_barang}. Sisa stok: {sisa}"

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong"
        daftar = "\n".join(f"- {barang}: {stok}" for barang, stok in self.inventori.items())
        return f"Daftar Inventori:\n{daftar}"


# Demonstrasi ManajerInventori
print("\n--- Manajer Inventori ---")
gudang = ManajerInventori()
print(gudang.tambah_barang("Laptop", 10))
print(gudang.tambah_barang("Mouse", 25))
print(gudang.tambah_barang("Laptop", 5))
print(gudang.hapus_barang("Laptop", 3))
print(gudang.hapus_barang("Mouse"))
print(gudang.lihat_inventori())