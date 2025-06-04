mahasiswa = {}

def tambah_data():
    nim = input("Masukan NIM: ")
    if nim in mahasiswa:
        print("NIM sudah terdaftar. ")
        return
    nama = input("Masukan Nama: ")
    jurusan = input("Masukan Jurusan: ")
    try:
        ipk = float(input("Masukan IPK: "))
        if ipk < 0.0 or ipk  > 4.0:
            print("IPK harus antara 0.0 sampai 4.0")
            return
    except ValueError:
        print("IPK harus berupa angka. ")
        return

    mahasiswa[nim] = {"Nama": nama, "Jurusan": jurusan, "IPK" : ipk}
    print("Data mahasiswa berhasil ditambahkan. ")

def tampilkan_semua():
    if not mahasiswa:
        print("Tidak ada data mahasiswa. ")
    else:
        print("/nData mahasiswa:")
        for nim, data in mahasiswa.items():
            print(f"NIM: {nim}, Nama: {data['Nama']}. Jurusan: {data['Jurusan']}, IPK: {data['ipk']} ")

def cari_mahasiswa():
    nim = input("Masukan NIM yang ingin dicari: ")
    if nim in mahasiswa:
        data = mahasiswa[nim]
        print(f"NIM: {nim}, Nama: {data['Nama']}. Jurusan: {data['Jurusan']}, IPK: {data['ipk']} ")
    else:
        print("Data mahasiswa tidak ditemukan. ")
        
def hapus_mahasiswa():
    nim = input("Masukan NIM yang akan dihapus: ")
    if nim in mahasiswa:
        del mahasiswa[nim]
        print("Data mahasiswa berhasil dihapus. ")
    else:
        print("Data mahasiswa tidak ditemukan. ")

def menu():
    while True:
        print("n=== Menu Manajemen Data Mahasiswa ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Semua Data Mahasiswa")
        print("3. Cari Data Mahasiswa (berdasarkan NIM)")
        print("4. Hapus Data mahasiswa (berdasarkan NIM)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            tampilkan_semua()
        elif pilihan == '3':
            cari_mahasiswa()
        elif pilihan == '4':
            hapus_mahasiswa()
        elif pilihan == '5':
            print("Terimakasih!! Program selesai. ")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih antara 1 sampai 5. ")
            
menu()