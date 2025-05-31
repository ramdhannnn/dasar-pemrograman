def cek_angka(angka):
    if angka > 0:
        return "positif"
    elif angka < 0:
        return "negatif"
    else:
        return "nol"
angka = int(input("masukan angka: "))
print (cek_angka(angka))