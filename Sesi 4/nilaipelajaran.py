def hitung_cek_nilai (matematika, saint, inggris):
    rata_rata = (matematika + saint + inggris) / 3
    di_bawah_70 = sum (1 for nilai  in [matematika, saint, inggris] if nilai < 70)
    
    if rata_rata > 75 and di_bawah_70 <= 1:
        return "lulus"
    else:
        return "tidak lulus"

matematika = float(input("masukan nilai matematika: "))
saint = float(input("masukan nilai saint:" ))
inggris = float(input("masukan nilai inggris: "))

hasil = hitung_cek_nilai(matematika, saint, inggris)
print(f"hasil:{hasil}")
        
    