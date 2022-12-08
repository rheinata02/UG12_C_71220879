def balik_angkahuruf(angka):
    a=''
    for i in angka:
        a=i+a
    return a
masuk=input("Masukkan Kata atau angka :")
print (balik_angkahuruf(masuk))
