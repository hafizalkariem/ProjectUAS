data = []

def cetak_daftar_nilai(nilai_mhs):
  # Mencetak daftar nilai
  print()
  for data in nilai_mhs:
    print(f"Nama: {data['nama']}, NIM: {data['nim']}, Nilai UTS: {data['uts']}, Nilai UAS: {data['uas']}, Nilai Tugas: {data['tugas']}")

def cetak_hasil_pencarian(nilai_mhs, data):
  # Mencetak hasil pencarian
  if data in nilai_mhs:
    print(f"Data ditemukan: Nama: {data['nama']}, NIM: {data['nim']}, Nilai UTS: {data['uts']}, Nilai UAS: {data['uas']}, Nilai Tugas: {data['tugas']}")
  else:
    print("Data tidak ditemukan.")
