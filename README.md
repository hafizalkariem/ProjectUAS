# ProjectUAS
###data = []
nilai_mhs = []


def tambah_data(nilai_mhs, data):
  nilai_mhs.append(data)
  

def ubah_data(nilai_mhs, data, data_baru):
  # Mencari dan mengubah data di dalam list/database
  index = nilai_mhs.index(data)
  nilai_mhs[index] = data_baru

def hapus_data(nilai_mhs, data):
  # Menghapus data dari list/database
  nilai_mhs.remove(data)

def cari_data(nilai_mhs, data):
  # Mencari data di dalam list/database
  if data in nilai_mhs:
    return True
  else:
    return False ###

