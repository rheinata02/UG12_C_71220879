a = input("Masukkan angka :")
keluar = input("Masukkan angka yg ingin dihitung :")

angka = 0
for i in list (a):
    if i == keluar:
        angka = angka+1
print ("Angka", keluar, "muncul sebanyak", angka, "kali")
