# input_nilai.py

def masukan_data():
  nama = input("Masukkan nama: ")
  nim = input("Masukkan NIM: ")
  uts = int(input("Masukkan nilai UTS: "))
  uas = int(input("Masukkan nilai UAS: "))
  tugas = int(input("Masukkan nilai tugas: "))
  data = {'nama': nama, 'nim': nim, 'uts': uts, 'uas': uas, 'tugas': tugas}
  return data
