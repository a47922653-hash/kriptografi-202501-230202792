# Laporan Praktikum Kriptografi
Minggu ke-: 3  
Topik: Modular Math  
Nama: Zaki Fauzan Sulton  
NIM: 230202793  
Kelas: 5IKRA  

---

## 1. Tujuan
1. Menyelesaikan operasi aritmetika modular.  
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).  
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Aritmetika modular adalah sistem perhitungan yang menggunakan sisa hasil bagi terhadap suatu bilangan tetap yang disebut **modulus**. Dalam sistem ini, dua bilangan dianggap kongruen jika memiliki sisa yang sama saat dibagi dengan modulus tersebut, ditulis sebagai:

$$
a \equiv b \pmod{n}
$$

Operasi seperti penjumlahan, pengurangan, dan perkalian dilakukan dengan cara mengambil hasil modulo *n*. Prinsip ini menjaga nilai tetap berada dalam rentang 0 hingga *n−1* dan menjadi dasar bagi banyak algoritma komputasi modern, terutama dalam bidang kriptografi.

Konsep penting dalam aritmetika modular adalah **invers modular**, yaitu bilangan *x* yang memenuhi:

$$
a \. x \equiv 1 \pmod{n}
$$

Invers ini hanya ada jika *a* dan *n* relatif prima, yaitu:

$$
\gcd(a, n) = 1
$$

Untuk menghitungnya digunakan **Algoritma Extended Euclidean**, yang tidak hanya mencari *Greatest Common Divisor (GCD)* antara dua bilangan, tetapi juga koefisien yang memungkinkan pencarian invers modular. Invers modular sangat penting dalam algoritma kriptografi seperti **RSA**, karena digunakan dalam proses pembentukan kunci publik dan privat.

Selain itu, **logaritma diskrit** merupakan bagian lain dari aritmetika modular yang berfungsi mencari eksponen *x* pada persamaan:

$$
a^x \equiv b \pmod{n}
$$

Masalah ini sangat sulit diselesaikan untuk modulus besar, dan kesulitannya menjadi dasar keamanan berbagai sistem kriptografi modern seperti **Diffie–Hellman Key Exchange** dan **ElGamal**. Dengan demikian, aritmetika modular bukan hanya konsep matematika dasar, tetapi juga fondasi utama dari keamanan data dalam dunia digital.

---

## 3. Alat dan Bahan
(- Python 3.11.0  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library standar )

---

## 4. Langkah Percobaan
1. Membuat file `modular_math.py` di folder `praktikum/week3-modmath-gcd/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python modular_math.py`.)

---

## 5. Source Code

```python
# modular_math.py

# --- Langkah 1: Aritmetika Modular ---
def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))

# --- Langkah 2: GCD (Euclidean Algorithm) ---
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))

# --- Langkah 3: Extended Euclidean & Invers Modular ---
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))

# --- Langkah 4: Logaritma Diskrit ---
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))
```
)

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program Modular Math:

![Hasil Eksekusi](screenshots/output.png)
)
| Fungsi | Input | Output | Keterangan |
|---------|--------|---------|------------|
| mod_add | 7, 5, 12 | 0 | Operasi penjumlahan modular berhasil |
| mod_mul | 7, 5, 12 | 11 | Perkalian modular sesuai teori |
| mod_exp | 7^128 mod 13 | 3 | Eksponensiasi modular berhasil |
| gcd | 54, 24 | 6 | GCD sesuai hasil perhitungan manual |
| modinv | 3 mod 11 | 4 | Invers modular benar karena 3×4 ≡ 1 (mod 11) |
| discrete_log | 3^x ≡ 4 (mod 7) | x=4 | Hasil sesuai ekspektasi |

Semua hasil sesuai ekspektasi teori. Tidak ditemukan error selama eksekusi.

---

## 7. Jawaban Pertanyaan

1. Apa peran aritmetika modular dalam kriptografi modern?

   Aritmetika modular menjadi dasar semua operasi matematika di kriptografi modern. Sistem seperti RSA, Diffie–Hellman, dan ElGamal menggunakan operasi tambah, kali, dan pangkat dalam ruang modular agar hasil selalu          berada dalam rentang bilangan terbatas. Prinsip ini menjaga kestabilan perhitungan, memungkinkan pembentukan kunci yang sulit ditebak, dan memastikan proses enkripsi–dekripsi dapat dibalik secara aman.
   
3. Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)?

   Invers modular digunakan untuk membentuk kunci privat yang menjadi kebalikan dari kunci publik. Dalam RSA, jika kunci publik adalah e, maka kunci privat d adalah invers modular dari $e$ terhadap $φ(n)$, ditulis sebagai $e \times d \equiv 1 \pmod{\varphi(n)}$. Tanpa invers modular, pesan yang dienkripsi tidak dapat didekripsi kembali, sehingga sistem kunci publik tidak akan berfungsi.
   
5. Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?

    Tantangan utamanya adalah kompleksitas komputasi yang sangat tinggi. Untuk modulus besar (ratusan atau ribuan bit), mencari nilai x yang memenuhi $a^x \equiv b \pmod{n}$ membutuhkan waktu dan sumber daya yang luar biasa besar karena tidak ada algoritma efisien yang diketahui untuk menyelesaikannya. Kesulitan inilah yang membuat banyak algoritma kriptografi modern tetap aman terhadap serangan brute force. 
)
---

## 8. Kesimpulan
Berdasarkan percobaan, seluruh fungsi aritmetika modular, GCD, invers modular, dan logaritma diskrit berhasil dijalankan dengan hasil sesuai teori. Program menunjukkan bagaimana operasi matematika modular menjadi dasar dari sistem kriptografi modern. Melalui praktikum ini, konsep dasar seperti pembatasan nilai, pembentukan kunci, dan kesulitan logaritma diskrit dapat dipahami secara nyata melalui implementasi kode Python.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.   
- 

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
