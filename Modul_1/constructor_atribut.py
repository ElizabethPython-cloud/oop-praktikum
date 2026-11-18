class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        # Instance attributes
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"{self.merk} ({self.warna}, {self.tahun}) - Bahan bakar: {self.bahan_bakar}"


# Instansiasi object Kendaraan
kendaraan1 = Kendaraan("Toyota Avanza", "Hitam", 2022)
kendaraan2 = Kendaraan("Honda Civic", "Putih", 2024)

# Demonstrasi akses instance attribute (unik per object)
print("\n--- Akses Instance Attribute ---")
print(f"Kendaraan 1: {kendaraan1.merk}, {kendaraan1.warna}, {kendaraan1.tahun}")
print(f"Kendaraan 2: {kendaraan2.merk}, {kendaraan2.warna}, {kendaraan2.tahun}")

# Demonstrasi akses class attribute (dapat diakses lewat class maupun object)
print("\n--- Akses Class Attribute ---")
print(f"Via class  : {Kendaraan.bahan_bakar}")
print(f"Via objek 1: {kendaraan1.bahan_bakar}")
print(f"Via objek 2: {kendaraan2.bahan_bakar}")

# Mengubah class attribute lewat class memengaruhi semua object
Kendaraan.bahan_bakar = "Pertamax"
print("\nSetelah Kendaraan.bahan_bakar diubah ke 'Pertamax':")
print(kendaraan1.info_kendaraan())
print(kendaraan2.info_kendaraan())