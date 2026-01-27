# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [TinyCoin ERC 20]  
Nama: [Zaki Fauzan Sulton]  
NIM: [230202792]  
Kelas: [5IKRA]  

---

## 1. Tujuan
1. Mengembangkan proyek sederhana berbasis algoritma kriptografi.  
2. Mendokumentasikan proses implementasi proyek ke dalam repository Git.  
3. Menyusun laporan teknis hasil proyek akhir.  

---

## 2. Dasar Teori
TinyCoin (ERC-20) secara teoritis merupakan implementasi smart contract yang mematuhi standar ERC-20 (Ethereum Request for Comment 20) di jaringan blockchain Ethereum. ERC-20 bukanlah sebuah perangkat lunak, melainkan sebuah standar antarmuka (interface standard) yang mendefinisikan serangkaian aturan dan fungsi wajib, seperti totalSupply, balanceOf, transfer, approve, allowance, dan transferFrom. Dengan mengadopsi standar ini, TinyCoin diklasifikasikan sebagai fungible token (token yang dapat dipertukarkan), di mana setiap satu unit TinyCoin memiliki nilai dan properti yang identik dengan unit TinyCoin lainnya, berbeda dengan NFT (ERC-721) yang bersifat unik. Kepatuhan terhadap standar ini menjamin interoperabilitas, yang memungkinkan TinyCoin untuk secara otomatis dikenali dan berinteraksi dengan berbagai dompet digital (wallet), bursa pertukaran (exchange), dan aplikasi terdesentralisasi (DApps) tanpa memerlukan penyesuaian teknis khusus.

Dari sisi mekanisme teknis, smart contract TinyCoin tidak menyimpan token di dalam dompet pengguna secara fisik, melainkan bertindak sebagai buku besar digital (ledger) terpusat secara logika namun terdesentralisasi secara eksekusi. Kontrak ini memelihara struktur data (biasanya berupa mapping) yang memetakan alamat Ethereum pengguna ke saldo token mereka. Setiap kali transaksi terjadi, fungsi dalam kontrak dieksekusi oleh Ethereum Virtual Machine (EVM) untuk memperbarui status (state) saldo internal tersebut. Keamanan dan validitas transaksi TinyCoin bergantung sepenuhnya pada konsensus jaringan Ethereum, di mana setiap perubahan saldo memerlukan tanda tangan digital dari pemilik kunci privat dan pembayaran biaya eksekusi (gas fee) dalam bentuk Ether (ETH).

---

## 3. Alat dan Bahan  
- Metamask
- Wallet
- Remix IDE ETH

---

## 4. Langkah Percobaan
1. Membuat file `TinyCoin.sol` di Remix ETH.
2. Menyalin kode program dari panduan praktikum.
3. Compile sesuai batasan versi sol pada program
4. Deploy contract dan msg send ke wallet yang diinginkan sebagai wallet deployer
5. Import token contract, jika keluar di metamask berarti berhasil
6. Bisa Uji Coba kirim (Klaim gass fee di Sepolia Faucet)

---

## 5. Source Code

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        _mint(msg.sender, initialSupply);
    }
}
```
)

---

## 6. Hasil dan Pembahasan

![Hasil Output](screenshots/output.png)

### Hasil
Smart contract ERC-20 **TinyCoin (TNC)** berhasil dikompilasi dan dideploy menggunakan Remix Ethereum IDE tanpa error. Setelah proses deploy, kontrak muncul pada menu **Deployed Contracts** dan dapat diakses melalui alamat kontrak yang dihasilkan oleh sistem.

Pengujian fungsi standar ERC-20 menunjukkan hasil sebagai berikut:
- Fungsi `name()` mengembalikan nilai **TinyCoin**.
- Fungsi `symbol()` mengembalikan nilai **TNC**.
- Fungsi `decimals()` mengembalikan nilai **18**, sesuai standar ERC-20.
- Fungsi `totalSupply()` mengembalikan nilai `100000000000000000000`, yang merepresentasikan total supply sebesar **100 TNC** setelah dikonversi dengan faktor desimal.

Seluruh token hasil pencetakan awal (initial supply) berhasil diminting dan secara otomatis dialokasikan ke alamat akun deployer.

### Pembahasan
Nilai total supply yang terlihat sangat besar disebabkan oleh mekanisme representasi token ERC-20 yang tidak menggunakan bilangan desimal secara langsung. Dengan nilai `decimals = 18`, setiap 1 TNC direpresentasikan sebagai `10^18` unit internal, sehingga seluruh perhitungan dilakukan dalam bentuk bilangan bulat.

Fungsi `transfer` memungkinkan pemindahan token antar alamat secara langsung, sedangkan mekanisme `approve`, `allowance`, dan `transferFrom` menyediakan sistem kontrol akses berbasis izin untuk penggunaan token oleh pihak ketiga. Hasil pengujian menunjukkan bahwa seluruh fungsi inti ERC-20 berjalan sesuai dengan spesifikasi standar.

Secara keseluruhan, hasil praktikum membuktikan bahwa implementasi smart contract ERC-20 TinyCoin telah sesuai dengan standar OpenZeppelin dan dapat dijadikan sebagai dasar untuk pengembangan token serta aplikasi terdesentralisasi pada tahap selanjutnya.

---

## 7. Jawaban Pertanyaan

1. **Apa fungsi utama ERC20 dalam ekosistem blockchain?**  
   ERC20 berfungsi sebagai standar teknis untuk pembuatan dan pengelolaan token pada blockchain Ethereum sehingga token memiliki antarmuka yang seragam, kompatibel dengan wallet, exchange, dan aplikasi terdesentralisasi (dApp).

2. **Bagaimana mekanisme transfer token bekerja dalam kontrak ERC20?**  
   Transfer token dilakukan melalui fungsi `transfer` untuk pengiriman langsung antar alamat, serta melalui mekanisme `approve` dan `transferFrom` yang memungkinkan pihak ketiga memindahkan token berdasarkan izin (allowance) yang telah diberikan pemilik token.

3. **Apa risiko utama dalam implementasi smart contract dan bagaimana cara mitigasinya?**  
   Risiko utama meliputi bug logika, kesalahan kontrol akses, dan celah keamanan seperti reentrancy, yang dapat dimitigasi dengan penggunaan library terpercaya (misalnya OpenZeppelin), audit kode, pengujian menyeluruh, serta penerapan prinsip least privilege dalam desain kontrak.

---

## 8. Kesimpulan
Smart contract ERC-20 TinyCoin berhasil dikompilasi dan dideploy dengan baik menggunakan Remix IDE serta menunjukkan fungsi-fungsi standar ERC-20 berjalan sesuai spesifikasi. Praktikum ini membuktikan bahwa OpenZeppelin ERC-20 dapat digunakan sebagai fondasi yang stabil untuk pengembangan token dan aplikasi blockchain lanjutan.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

```
commit 5cd3f88b14c2630cd78c12dd2375eafd4d65f965
Author: Zaki Fauzan Sulton <a47922653@gmail.com>
Date:   Tue Jan 27 18:55:08 2026 +0700

    week15-tinycoin-erc20

```
