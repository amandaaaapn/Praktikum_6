# Praktikum 6

Nama : Amanda Puspa Negara

NIM : 312210129

Kelas : TI.22.A1

## DAFTAR ISI <br>
| No | Description | Link |
|-----|------|-----|
|1|Latihan|[Click Here](#latihan)|
|2|Praktikum 6|[Click Here](#praktikum6)|
|3|Flowchart Praktikum 6|[Click Here](#flowchart-praktikum-6)

### Latihan

Ubahlah kode di bawah ini menjadi fungsi menggunakan lambda

        import math

        def a(x):
        return x**2

        def b(x, y):
        return math.sqrt(x**2 + y**2)

        def c(*args):
        return sum(args)/len(args)

        def d(s):
        return "".join(set(s))
        
### Rumus :

        import math
        def a(x):
            return x**2
            a = lambda x : x ** 2
        print(2)\

        def b(x,y):
            return math.sqrt(x*2 + y*2)
            b = lambda x,y : x * 2 + y * 2
        print(2 , 2)

        def c(*args):
            return sum(args)/len(args)
            c = lambda *args : sun(args)/len(args)
        print(5, -6, 7, 8)

        def d(s):
            return "".join(set(s))
        d = lambda s: "".join(set(s))
        print("AMANDA PUSPA NEGARA")
        
### Program :

![Screenshot (121)](https://user-images.githubusercontent.com/115678845/205914246-1a0dadd3-2905-4e90-9d87-fdeb8be5d0c6.png)

### Hasil Run :

![Screenshot (128)](https://user-images.githubusercontent.com/115678845/205914726-6a1763b6-b6ab-4375-8003-93ddc4316dfa.png)

### Praktikum 6

Buat program sederhana dengan mengaplikasikan penggunaan fungsi yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan :

- Fungsi tambah() untuk menambah data.
- Fungsi tampilkan() untuk menampilkan data.
- Fungsi hapus(nama) untuk menghapus data berdasarkan nama.
- Fungsi ubah(nama) untuk mengubah data berdasarkan nama.
- Buat Flowchart dan Penjelasan Programnya pada README.md.
- Commit dan push repository ke github.

### Rumus :

        from os import system
        s_nama = []
        s_nim = []
        s_tugas = []
        s_uts = []
        s_uas = []
        s_akhir = []


        def judul():
            print('==================================')
            print('|     Daftar Nilai Mahasiswa     |')
            print('==================================')


        def menu():
            system('cls')
            print('=====================================')
            print('Input Data Nilai Mahasiswa'.center(40))
            print('=====================================')
            print('|    1. Tambah Data                 |')
            print('|    2. Tampilkan Data Mahasiswa    |')
            print('|    3. Ubah Data Mahasiswa         |')
            print('|    4. Hapus Data Mahasiswa        |')
            print('|    5. Selesai                     |')
            print('=====================================')
            choose = input('Pilih Menu  : ')
            if choose == '1':
                tambah()
            elif choose == '2':
                tampilkan()
            elif choose == '3':
                ubah()
            elif choose == '4':
                hapus()
            elif choose == '5':
                selesai()
            else:
                tidak = input('Menu Tidak Ada')
                system('cls')
                menu()


        def tambah():
            system('cls')
            judul()
            print('Tambah Data'.center(40))
            print('==================================')
            nama = input('Nama     : ')
            s_nama.append(nama)
            nim = input('NIM       : ')
            s_nim.append(nim)

            system('cls')
            judul()
            print('Tambah Data'.center(40))
            print('==================================')
            tugas = float(input('Nilai Tugas    : '))
            s_tugas.append(tugas)

            uts = float(input('Nilai UTS        : '))
            s_uts.append(uts)

            uas = float(input('Nilai UAS        : '))
            s_uas.append(uas)

            total = tugas * 0.30 + uts * 0.35 + uas * 0.35
            s_akhir.append(total)
            print('Data Tersimpan'.center(40))
            kembali = input('Kembali [Enter]')
            menu()


        def tampilkan():
            system('cls')
            judul()

            for i in range(len(s_nim)):
                print('%d. Nama         : %s' % (i + 0, s_nama[i]))
                print('    NIM          : %s' % s_nim[i])
                print('    Nilai Tugas  : %.2f' % s_tugas[i])
                print('    UTS          : %.2f' % s_uts[i])
                print('    UAS          : %.2f' % s_uas[i])
                print('    Nilai Akhir  : %.2f' % s_akhir[i])
                print('-----------------------------')
            kembali = input('Kembali Tekan [Enter]')
            menu()


        def ubah():
            rubah = input('Ubah Biodata Tekan [B]   : ')
            if rubah == 'B' or rubah == 'b':
                i = int(input('Masukkan Nomor Urut  : '))
                if (i > len(s_nim[i])):
                    print('Nomor Urut Salah')
                else:
                    namabaru = input('Nama      : ')
                    s_nama[i] = namabaru
            kembali = input('Kembali Tekan [Enter]')
            menu()


        def hapus():
            system('cls')
            judul()
            print('Hapus Data'.center(40))
            print('=================================')
            i = int(input('Masukkan Nomor Urut  : '))

            if (i > len(s_nim[i])):
                tidak = input('NIM Tidak Ada')
                hapus()

            else:
                s_nim.remove(s_nim[i])
                s_nama.remove(s_nama[i])
                s_tugas.remove(s_tugas[i])
                s_uts.remove(s_uts[i])
                s_uas.remove(s_uas[i])
                s_akhir.remove(s_akhir[i])

            print('Data Berhasil Di Hapus')
            kembali = input('Kembali Tekan [Enter]')
            menu()


        def selesai():
            system('cls')


        menu()
        
### Program :

![Screenshot (127)](https://user-images.githubusercontent.com/115678845/205915310-9bddcdaa-8393-42a8-9b80-5e671936f435.png)

### Hasil Run :

- Menambah Data

![Screenshot (123)1](https://user-images.githubusercontent.com/115678845/205915453-cdf806f7-a419-45da-be27-092fa6313ce7.png)

- Menampilkan Data

![Screenshot (124)2](https://user-images.githubusercontent.com/115678845/205915585-4595e975-c13f-4af5-9803-ed80f35214a2.png)

- Mengubah Data

![Screenshot (125)3](https://user-images.githubusercontent.com/115678845/205915669-cbae97d9-81ca-48f7-91d4-d8a8a80f8693.png)

![Screenshot (130)](https://user-images.githubusercontent.com/115678845/205916665-cb91beae-7c45-4a38-ac31-b682322368e4.png)

- Menghapus Data

![Screenshot (126)4](https://user-images.githubusercontent.com/115678845/205916771-06ab1a19-d046-4ead-ae3a-d5dba0903248.png)

- Selesai

![Screenshot (126)5](https://user-images.githubusercontent.com/115678845/205918640-12a84690-a757-461d-b11d-660cad3514a7.png)

### Penjelasan Program :
1. Definisikan dictionary terlebih dahulu data = {}.
2. Membuat fungsi
- Fungsi tampilkan(), untuk menambahkan data def tampilkan()
- Fungsi tambah(), untuk menampilkan data def tambah()
- Fungsi hapus(nama), untuk menghapus nama pada data def hapus(nama)
- Fungsi ubah(nama), untuk mengubah nama pada data def ubah(nama)
3. Menggunakan Perulangan while True: dapat diartikan perulangan akan terus mengulang jika inputan benar dan masuk kedalam proses jika tidak maka perulangan berhenti atau lanjut ke proses selanjutnya. Gunakan statement if untuk memproses perintah yang di inginkan sesuai inputan.
4. Untuk menambahkan data pilih "[1] Tambah" gunakan fungsi if gunakan perintah "1", lalu masukan nama, nim, tugas, uts, uas, nilaiakhir, nilai akhir didapat dari = ((tugas)*30/100 + (uts)*35/100 + (uas)*35/100.
5. Lalu jika ingin memilih "[2] Lihat" gunakan fungsi 'elif' dan gunakan fungsi 'for x in data.items():' untuk melihat data pada tabel data yang kita inputkan, dengan perintah "2". Jika data tidak terdaftar maka akan tampil "TIDAK ADA DATA" atau = 0.
6. Lalu untuk menampilan pilihan "[3] Ubah" gunakan fungsi 'elif' kemudian gunakan fungsi 'if nama in data.keys():' kemudian input nama, nim, nilai tugas, nilai uts, nilai uas untuk mengubah data nama kemudian gunakan fungsi 'else' untuk menampilkan data nama yang kita ingin ubah tidak ada.
7. Untuk menghapus data pilih "[4] Hapus" gunakan fungsi 'elif' kemudian gunakan fungsi 'if nama in data.keys():' kemudian fungsi 'del.data[nama] jika nama yang kita hapus tidak ada dalam tabel maka gunakan fungsi 'else' untuk menampilkan "TIDAK ADA DATA".
8. Untuk keluar maka gunakan fungsi else dan exit() atau gunakan perintah [5] Keluar.
9. Selesai.
### Flowchart Praktikum 6

![flowchart](https://user-images.githubusercontent.com/115678845/205917524-765f76c9-e2e8-4b0d-a4ed-31a221572096.jpeg)

# Sekian, Terima kasi
