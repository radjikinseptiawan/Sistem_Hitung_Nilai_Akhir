mahasiswa = []

no = 0

while no < 10 :
    nama = input("Nama mahasiswa : ")
    nomorIndukMahasiswa = input("NIM : ")
    nilaiTugas = float(input("Nilai Tugas : "))
    nilaiUTS = float(input("nilai UTS : "))
    nilaiUAS = float(input("nilai UAS : "))
    no +=1
    nilaiAkhir = nilaiTugas * 0.3 + nilaiUAS * 0.35 + nilaiUTS * 0.35

    choose = input("Tambahkan Data ? (yes/no) : ")

    if choose.lower() == "yes" :
        print("="*64)
        print("| no |   Nama   |   NIM   |  Nilai Tugas  |   UTS   |   UAS    |   Nilai Akhir |")
        mahasiswa.append({
        "no": no ,
        "nama" : nama,
        "NIM" : nomorIndukMahasiswa,
        "nilaiTugas" : nilaiTugas,
        "nilaiUTS" : nilaiUTS,
        "nilaiUAS" : nilaiUAS,
        "nilaiAkhir" : nilaiAkhir
         })
        for mhs in mahasiswa:
            print(f"| {mhs["no"]} | {mhs["nama"]} |{ mhs["NIM"]:<10} | {mhs["nilaiTugas"]:<4} | {mhs["nilaiUTS"]:<4} | {mhs["nilaiUAS"]:<4} |{mhs["nilaiAkhir"]:<4} |")
        print("="*64)
    else:
        print("| no |   Nama   |   NIM   |  Nilai Tugas  |   UTS   |   UAS    |   Nilai Akhir |")
        for mhs in mahasiswa:
            print(f"| {mhs["no"]:2} | {mhs["nama"]:<15} |{ mhs["NIM"]:<10} | {mhs["nilaiTugas"]:<11} | {mhs["nilaiUTS"]:<7} | {mhs["nilaiUAS"]:<7} |{mhs["nilaiAkhir"]:<12} |")
        print("="*64)
                  

print("Tabel Sudah Penuh")

