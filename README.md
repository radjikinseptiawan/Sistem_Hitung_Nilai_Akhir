#### Sistem Penghitung Nilai Akhir Mahasiswa
------

![RadjikinSeptiawanFlowChart-1](https://github.com/user-attachments/assets/54076fa0-6a99-46a8-9d4b-e769ac6f6c57)

***Membuat Variabel sebelum looping***
Pada flowchart diatas kita dapat melihat bahwasanya ketika kode dijalankan
program akan membuat sebuah variabel yang bertipe data array atau list. 
Lalu program membuat variabel lain bertipe data integer dan menginisialisasi nilai nya sebagai 0
program memberi nama variabel tersebut dengan nama "no"

***Melakukan perulangan*** 
ketika array atau list dan variabel no sudah di buat maka program akan melakukan perulangan 
yang mana jika no kurang dari 10 maka lakukan perulangan disana program meminta user untuk 
memasukkan nama, NIM,nilai tugas, UAS dan UTS yang masing masing masuk ke variabel nya sendiri sendiri.
lalu setelah selesai menginput nya, program akan melakukan operasi matematika dengan 
```bash
(nilaiTugas * 30%) + (nilaiUTS * 35%) + (nilaiUAS * 35%)
 ```

setelah nya program akan meminta intruksi untuk mengambil keputusan, jika keputusan sama dengan "yes" maka tambahkan data yang sebelumnya
ke dalam array atau list mahasiswa, jika tidak maka tampilkan list mahasiswa perulangan ini akan dilakukan selama 10x oleh program

***Jika array penuh***
jika array penuh program tidak akan melakukan perulangan melainkan akan memberi output berupa
"Tabel Sudah penuh"
