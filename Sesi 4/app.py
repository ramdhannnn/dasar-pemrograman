angka = 4
jenis = "ganjil"

if angka %2 ==0:
    jenis = "genap"
    
print("%s adalah bilangan %s" % (angka,jenis))
#multi
nilai =int(input("masukan nilai: "))
grade = "E"

if nilai >=90:
    grade = "A"
elif nilai >=80:
    grade = "B"
elif nilai >=70:
    grade = "C"
elif nilai >=60:
    grade = "D"

print("Grade:",grade)