from model import daftar_nilai
from view import view_nilai
from view import input_nilai

nilai_mhs = []

while True:
      print("Menu:")
      print("1. Tambah data")
      print("2. Ubah data")
      print("3. Hapus data")
      print("4. Cari data")
      print("5. Cetak daftar nilai")
      print("6. Cetak hasil pencarian")
      pilihan = input("Masukkan pilihan Anda (1-6): ")
      
      if pilihan == '1':
        data = input_nilai.masukan_data()
        daftar_nilai.tambah_data(nilai_mhs, data)
        
      elif pilihan == '2':
        data = input_nilai.masukan_data()
        data_baru = input_nilai.masukan_data()
        daftar_nilai.ubah_data(nilai_mhs,data, data_baru)
      elif pilihan == '3':
        data = input_nilai.masukan_data()
        daftar_nilai.hapus_data(nilai_mhs,data)
      elif pilihan == '4':
        data = input_nilai.masukan_data()
        hasil = daftar_nilai.cari_data(nilai_mhs, data)
        if hasil:
          print("Data ditemukan.")
        else:
          print("Data tidak ditemukan.")
      elif pilihan == '5':
        view_nilai.cetak_daftar_nilai(nilai_mhs)
      elif pilihan == '6':
        data = input_nilai.masukan_data()
        view_nilai.cetak_hasil_pencarian(nilai_mhs,data)
      else:
        print("masukan data yang valid")
