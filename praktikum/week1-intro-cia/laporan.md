# Laporan Sejarah Kriptografi & Prinsip CIA
Minggu ke-: 1  
Topik: Intro CIA  
Nama: Zaki Fauzan Sulton  
NIM: 230202792  
Kelas: 5IKRA  

---

## 1. Tujuan
1. Menjelaskan **sejarah dan evolusi kriptografi** dari masa klasik hingga modern.  
2. Menyebutkan **prinsip Confidentiality, Integrity, Availability (CIA)** dengan benar.  
3. Menyimpulkan **peran kriptografi** dalam sistem keamanan informasi modern.  
4. Menyiapkan repositori GitHub sebagai media kerja praktikum.  

---

## 2. Ringkasan Sejarah Kriptografi
Kriptografi adalah ilmu yang mempelajari cara menyembunyikan informasi agar hanya penerima yang sah dapat membacanya. Tujuan utamanya: menjaga kerahasiaan, keaslian, dan keutuhan data.
**Pada era klasik**, kriptografi masih bersifat manual dan sederhana.
Contohnya:
- **Caesar Cipher** mengganti setiap huruf dengan huruf lain yang posisinya bergeser beberapa langkah di alfabet.
- **Vigenère Cipher** menggunakan kata kunci untuk menentukan pola pergeseran huruf.
Metode ini efektif di masa lalu, tetapi bisa dipecahkan dengan analisis frekuensi, yaitu menghitung seberapa sering huruf muncul untuk menebak pola sandi.

**Memasuki era modern**, kriptografi menjadi bidang ilmiah yang melibatkan matematika dan teori informasi.
Salah satu tokoh pentingnya adalah Claude Shannon, yang disebut “bapak kriptografi modern” karena menjelaskan bagaimana pesan bisa diamankan secara logis.
Contohnya:
- **RSA (Rivest–Shamir–Adleman)**, sistem dengan dua kunci: satu publik untuk mengenkripsi dan satu privat untuk mendekripsi.
- **AES (Advanced Encryption Standard)**, sistem kunci simetris di mana pengirim dan penerima memakai kunci yang sama.
Teknik-teknik ini digunakan di internet, kartu ATM, dan sistem login digital.

**Di era kontemporer**, kriptografi menjadi pondasi dunia digital.
- **Teknologi blockchain** memakai kriptografi untuk mencatat transaksi yang tidak bisa diubah, sedangkan **cryptocurrency** seperti Bitcoin memakai tanda tangan digital untuk memverifikasi kepemilikan tanpa bank.
Singkatnya, kriptografi berevolusi dari penyandian sederhana menjadi sistem matematis kompleks yang menjaga keamanan informasi di seluruh dunia modern.

---

## 3. Prinsip CIA
Tiga pilar keamanan informasi:  
- **Confidentiality** → Confidentiality berarti menjaga agar informasi hanya dapat diakses oleh pihak yang berwenang. Tujuannya mencegah kebocoran data kepada orang yang tidak berhak.

    Contohnya:
    - Enkripsi pesan di WhatsApp memastikan hanya pengirim dan penerima yang bisa membaca isi chat.
    - Sistem login dengan username dan password melindungi akses ke akun pengguna.

    Jika prinsip ini gagal, data pribadi bisa disalahgunakan, misalnya kebocoran nomor kartu kredit.  
- **Integrity** → Integrity memastikan bahwa data tidak diubah, disisipkan, atau dihapus tanpa izin selama penyimpanan atau pengiriman. Informasi harus tetap sama seperti aslinya.

    Contohnya:
    - Checksum atau hash function digunakan untuk mengecek apakah file yang diunduh sama persis dengan versi aslinya.
    - Digital signature (tanda tangan digital) menjamin bahwa dokumen tidak diubah setelah disetujui.
    
    Jika integritas rusak, data menjadi tidak dapat dipercaya, bahkan jika kerahasiaannya masih terjaga.  
- **Availability** → Availability berarti informasi dan sistem selalu tersedia kapan pun dibutuhkan oleh pengguna yang berhak. Tujuannya memastikan layanan tetap berjalan meski terjadi gangguan.

    Contohnya:
    - Server bank memiliki sistem cadangan (backup) dan load balancing agar tetap aktif walau satu server rusak.
    - Situs web besar menggunakan sistem anti–DDoS attack agar tidak mudah lumpuh karena serangan trafik berlebihan.
    
    Jika aspek ini gagal, sistem bisa tidak dapat diakses walau datanya aman dan utuh.
  
---

## 4. Dokumentasi
- Buat screenshot evidence setup repo GitHub (`repo name`, `initial commit`). Simpan di folder `screenshots/`.  
- Lampiran screenshot
  ```markdown
  ![Setup GitHub](screenshots/repo_setup.png)

---

## 5. Quiz Singkat
Jawab pertanyaan berikut:  
1. Siapa tokoh yang dianggap sebagai bapak kriptografi modern?

    Tidak ada satu orang tunggal yang bisa disebut bapak kriptografi modern. Namun, dua tokoh yang paling berpengaruh adalah Claude Shannon dan Alan Turing.
    - Claude Shannon (1949) mengubah kriptografi menjadi ilmu matematika melalui teori informasi dan konsep confusion serta diffusion yang menjadi dasar enkripsi modern.
    - Alan Turing memimpin pemecahan sandi Enigma pada Perang Dunia II, membuktikan peran komputer dalam kriptanalisis dan keamanan digital.
   
    Tokoh lain yang juga berperan besar:
    - Al-Kindi (abad ke-9), penemu metode analisis frekuensi.
    - Leon Battista Alberti (abad ke-15), pencipta sandi polialfabetik.
    - Rivest, Shamir, dan Adleman (1977), pengembang algoritma RSA yang menjadi dasar sistem kunci publik modern.
   
    Kesimpulan: Shannon sering dianggap tokoh utama secara teoretis, tetapi kriptografi modern lahir dari kontribusi banyak ilmuwan di berbagai zaman. 
3. Sebutkan algoritma kunci publik yang populer digunakan saat ini.

   Beberapa algoritma kunci publik paling populer dan masih digunakan luas hingga sekarang antara lain:
    - RSA (Rivest–Shamir–Adleman), Berdasarkan faktorisasi bilangan prima besar. Digunakan untuk enkripsi, autentikasi, dan tanda tangan digital.

      Contoh penggunaan: keamanan data di protokol HTTPS dan transaksi digital.
    - Diffie–Hellman Key Exchange, Digunakan untuk pertukaran kunci rahasia di jaringan tanpa harus mengirim kunci langsung. Menjadi dasar bagi banyak protokol keamanan seperti TLS.
    - ECC (Elliptic Curve Cryptography), Menggunakan matematika kurva eliptik untuk memberikan keamanan tinggi dengan ukuran kunci kecil. Umum dipakai pada perangkat seluler dan blockchain karena efisien.
    
    Semua algoritma ini menggunakan dua kunci berbeda:
    Kunci publik untuk enkripsi (boleh dibagikan ke siapa saja) dan Kunci privat untuk dekripsi (hanya milik pemilik data).
5. Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
   | Aspek | Kriptografi Klasik | Kriptografi Modern |
    |-------|--------------------|--------------------|
    | **Dasar Teknik** | Berdasarkan **substitusi** dan **transposisi huruf** (contoh: Caesar Cipher, Vigenère Cipher). | Berdasarkan **matematika kompleks** dan **komputasi digital** (contoh: RSA, AES). |
    | **Kunci** | Menggunakan **satu kunci rahasia** bersama pengirim dan penerima. | Menggunakan **dua kunci berbeda** — publik dan privat (pada sistem asimetris). |
    | **Keamanan** | Bergantung pada **kerahasiaan metode** (mudah dipecahkan dengan analisis frekuensi). | Bergantung pada **kerahasiaan kunci** dan **kompleksitas algoritma**. |
    | **Implementasi** | Dilakukan secara manual untuk pesan teks sederhana. | Diimplementasikan secara digital untuk komunikasi, data, dan jaringan. |

    **Kesimpulan:**  
    Kriptografi klasik berfokus pada penyandian huruf, sedangkan kriptografi modern berbasis teori matematika dan algoritma komputer yang memberikan keamanan tinggi di era digital.

   ---
