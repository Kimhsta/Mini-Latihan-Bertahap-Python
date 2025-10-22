# Mini Latihan Bertahap – Pemrograman Python

Repository ini berisi kumpulan latihan sederhana dalam bahasa **Python** yang dibuat untuk memenuhi tugas mata kuliah **Pemrograman Python** yang diberikan oleh **Bapak Triyono, S.Kom**  
Program Studi **Teknik Informatika – Universitas Duta Bangsa (UDB)**.

Dibuat menggunakan pendekatan **Object-Oriented Programming (OOP)** agar mahasiswa memahami konsep dasar kelas, objek, atribut, dan method.

---

## 🎯 Tujuan Pembelajaran

- Memahami dasar konsep OOP (Class, Object, Method, Atribut)
- Menerapkan validasi data sederhana
- Membangun relasi antar objek (komposisi)
- Menggunakan list untuk mengelola banyak data
- Melakukan pencarian data berdasarkan kondisi tertentu

---

## 🧩 Deskripsi Program

Program terdiri dari tiga kelas utama:

### 1. `Dosen`

Mewakili data seorang dosen.

**Atribut:**

- `nidn` → Nomor Induk Dosen Nasional (harus 10 digit angka)
- `nama` → Nama dosen

**Validasi:**

- Jika `nidn` bukan angka atau tidak berjumlah 10 digit, program akan memunculkan pesan kesalahan `ValueError`.

**Metode:**

- `info()` → Menampilkan informasi dosen dalam format:
  ```bash
  Dosen [nama] - [nidn]
  ```

---

### 2. `Ruang`

Mewakili data ruang kelas.

**Atribut:**

- `kode` → Kode ruang (contoh: R101)
- `kapasitas` → Jumlah maksimum mahasiswa yang dapat ditampung

---

### 3. `KelasKuliah`

Menghubungkan antara **ruang kuliah**, **dosen**, dan **mahasiswa**.

**Atribut:**

- `kode_kelas` → Kode kelas (contoh: TI-23A5)
- `dosen` → Objek dari kelas `Dosen`
- `ruang` → Objek dari kelas `Ruang`
- `daftar_mahasiswa` → List berisi nama-nama mahasiswa yang terdaftar

**Metode:**

- `tambah_mahasiswa(nama)`  
  Menambahkan mahasiswa baru jika kapasitas ruang belum penuh.
- `tampilkan_info_kelas()`  
  Menampilkan informasi kelas (kode, dosen, ruang, kapasitas).
- `tampilkan_mahasiswa()`  
  Menampilkan seluruh mahasiswa yang sudah terdaftar.
- `tampilkan_mahasiswa_awal_DE()`  
  Menampilkan mahasiswa yang namanya diawali huruf **D** atau **E**.

---

## ⚙️ Alur Program

1. **Membuat objek Dosen**

   ```bash
   dosen1 = Dosen("1234567890", "Triyono")
   dosen2 = Dosen("0987654321", "Rizki")
   ```

   Jika `nidn` tidak valid, akan muncul pesan error:

   ```bash
   ❌ NIDN harus terdiri dari 10 digit angka.
   ```

2. **Membuat objek Ruang**

   ```bash
   ruangA = Ruang("R101", 29)
   ```

3. **Membuat objek KelasKuliah**

   ```bash
   kelas = KelasKuliah("TI-23A5", dosen2, ruangA)
   ```

4. **Menambahkan daftar mahasiswa**

   ```bash
   for nama in daftar_mahasiswa:
       kelas.tambah_mahasiswa(nama)
   ```

5. **Menampilkan hasil akhir**
   - Informasi kelas
   - Daftar mahasiswa
   - Mahasiswa yang nama depannya D atau E

---

## 🖥️ Contoh Output Program

```bash
=== LATIHAN A — KELAS DOSEN ===
Dosen Triyono - 1234567890
Dosen Rizki - 0987654321

=== LATIHAN B — VALIDASI NIDN ===
Gagal membuat Dosen: ❌ NIDN harus terdiri dari 10 digit angka.

=== LATIHAN C — KOMPOSISI MINI (KELAS KULIAH) ===
Informasi Kelas Kuliah:
- Kode Kelas   : TI-23A5
- Dosen Pengampu : Rizki
- Ruang        : R101
- Kapasitas    : 29 mahasiswa

Daftar Mahasiswa di kelas TI-23A5:
- Hafan
- Eka
- Aziz
- Irfan
- Minan
- Savina
- Trafika
- Lendra
- Luthfi
- Fitra
- Dhiwa
- Kahfi
- Desta
- Viqi
- Arsa
- Domingos
- Pratama
- Gigieh
- Faris
- Ridho
- Adit
- Bima
- Fahryan
- Nabil
- Najib
- Nathan
- Raihan
- Raka
- Rofi

=== LATIHAN D — FILTER NAMA AWAL D/E ===
Mahasiswa dengan nama diawali huruf D atau E:
- Eka
- Dhiwa
- Desta
- Domingos
```

---

## 💡 Konsep yang Digunakan

- **Object-Oriented Programming (OOP)**
- **Validasi Input (Error Checking)**
- **Exception Handling (try-except)**
- **List dan Perulangan (Looping)**
- **Seleksi berdasarkan huruf awal nama**

---

## 👨‍💻 Pengembang

**Nama:** Eka Rizki Suwarno  
**Kelas:** TI-23A5  
**Dosen Pengampu:** Bapak Triyono, S.Kom  
**Mata Kuliah:** Pemrograman Python  
**Kampus:** Universitas Duta Bangsa (UDB) – Surakarta
