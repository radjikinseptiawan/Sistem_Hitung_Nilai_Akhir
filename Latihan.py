# Nama : Radjikin Septiawan
# Kelas : TIF 24 A1
# NIM : 312410071

init = ["Universitas","Pelita","Bangsa",2024,2025]

# Tampilkan element ke 3
print(init[2])

# Ambil nilai elemen ke 2 sampai elemen ke 4
print(init[1:3])

#Ambil elemen terakhir
print(init[4])

# Ubah Element List
init[3] = "Septiawan"
print(init[3])
print(init)

# Ubah Element ke 2 sampai ke 4
init[1:3] = "index","inter","append"
print(init)

# Tambah element list

# Membagi elemen list menjadi dua
initA = ["Universitas","Pelita","Bangsa"]
initB = [2024,2025]


# menambah 3 element ke list initB
initB.insert(2,2026)
initB.insert(3,2027)
initB.insert(4,2028)

print(initB)

# Menggabungkan initA dan initB
initA.extend(initB)

print(initA)