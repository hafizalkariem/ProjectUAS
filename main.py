from model import daftar_nilai
from view import input_nilai
from view import view_nilai

nilai_mhs = []

while True:
    print("Menu")
    print("1. tambah data")
    print("2. ubah data")
    print("3. hapus data")
    print("4. cari data")
    print("5. cetak daftar nilai")
    print("6. cetak hasil pencarian")

    pilihan = input("Masukan Pilihan Anda (1-6) : ")

    if pilihan == '1':
        data = input_nilai.input_nilai()
        daftar_nilai.tambah_data(nilai_mhs,data)
    elif pilihan == '2':
        data = input_nilai.input_nilai()
        data_baru = input_nilai.input_data()
        daftar_nilai.ubah_data(nilai_mhs,data)
    elif pilihan == '3':
        data = input_nilai.input_nilai()
        daftar_nilai.hapus_data(nilai_mhs,data)
    elif pilihan == '4':
        data = input_nilai.input_nilai()
        hasil = daftar_nilai.cari_data(nilai_mhs,data)
        if hasil :
            print("Data Ditemukan")
        else:
            print("Data Tidak Ditemukan")
    elif pilihan == '5':
        view_nilai.cetak_daftar_nilai(nilai_mhs,data)
    elif pilihan == '6':
        data = input_nilai.input_nilai()
        view_nilai.cetak_hasil_pencarian(nilai_mhs,data)
    else:
        print("Masukan Data yang valid")

