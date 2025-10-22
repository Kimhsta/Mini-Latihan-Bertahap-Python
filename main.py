class Dosen:
    def __init__(self, nidn, nama):
        if not (nidn.isdigit() and len(nidn) == 10):
            raise ValueError("❌ NIDN harus terdiri dari 10 digit angka.")
        self.nidn = nidn
        self.nama = nama

    def info(self):
        print(f"Dosen {self.nama} - {self.nidn}")


# LATIHAN A — Buat objek Dosen
print("=== LATIHAN A — KELAS DOSEN ===")
try:
    dosen1 = Dosen("1234567890", "Triyono, S.Kom, M.Kom")
    dosen2 = Dosen("0987654321", "Eka Rizki Suwarno S.Kom, M.Sc")
    dosen1.info()
    dosen2.info()
except ValueError as e:
    print(e)

# LATIHAN B — Validasi NIDN (contoh salah)
print("\n=== LATIHAN B — VALIDASI NIDN ===")
try:
    Dosen("1234", "SalahFormat")
except ValueError as e:
    print("Gagal membuat Dosen:", e)


# LATIHAN C — KOMPOSISI (RUANG & KELAS KULIAH)
class Ruang:
    def __init__(self, kode, kapasitas):
        self.kode = kode
        self.kapasitas = kapasitas


class KelasKuliah:
    def __init__(self, kode_kelas, dosen, ruang):
        self.kode_kelas = kode_kelas
        self.dosen = dosen
        self.ruang = ruang
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, nama):
        if len(self.daftar_mahasiswa) < self.ruang.kapasitas:
            self.daftar_mahasiswa.append(nama)
        else:
            print(f"⚠️ Tidak bisa menambah {nama}. "
                  f"Ruang {self.ruang.kode} sudah penuh!")

    def tampilkan_info_kelas(self):
        print(f"\nInformasi Kelas Kuliah:")
        print(f"- Kode Kelas   : {self.kode_kelas}")
        print(f"- Dosen Pengampu : {self.dosen.nama}")
        print(f"- Ruang        : {self.ruang.kode}")
        print(f"- Kapasitas    : {self.ruang.kapasitas} mahasiswa")

    def tampilkan_mahasiswa(self):
        print(f"\nDaftar Mahasiswa di kelas {self.kode_kelas}:")
        for m in self.daftar_mahasiswa:
            print(f"- {m}")

    def tampilkan_mahasiswa_awal_DE(self):
        print("\nMahasiswa dengan nama diawali huruf D atau E:")
        hasil = [m for m in self.daftar_mahasiswa if m[0].upper() in ['D', 'E']]
        if hasil:
            for m in hasil:
                print(f"- {m}")
        else:
            print("Tidak ada mahasiswa dengan huruf awal D atau E.")


# LATIHAN C — Demo
print("\n=== LATIHAN C — KOMPOSISI MINI (KELAS KULIAH) ===")
ruangA = Ruang("R101", kapasitas=29)
kelas = KelasKuliah("TI-23A5", dosen2, ruangA)

daftar_mahasiswa = [
    "Hafan", "Eka", "Aziz", "Irfan", "Minan", "Savina", "Trafika", "Lendra",
    "Luthfi", "Fitra", "Dhiwa", "Kahfi", "Desta", "Viqi", "Arsa", "Domingos",
    "Pratama", "Gigieh", "Faris", "Ridho", "Adit", "Bima", "Fahryan", "Nabil",
    "Najib", "Nathan", "Raihan", "Raka", "Rofi"
]

for nama in daftar_mahasiswa:
    kelas.tambah_mahasiswa(nama)

kelas.tampilkan_info_kelas()
kelas.tampilkan_mahasiswa()


# LATIHAN D — FILTER NAMA D/E
print("\n=== LATIHAN D — FILTER NAMA AWAL D/E ===")
kelas.tampilkan_mahasiswa_awal_DE()
