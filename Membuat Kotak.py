print('Membuat Kotak')
n = int(input("masuukan Angka lebih dari 7 = "))

#Perulangan For dengan 2 n simbol
for _ in range (1, 2 * n+1):
    print('*', end = ' ')
print() # Pindah baris
#penampilan saru simbol dan sinmol tanpa sepasi lalu diikuti simbol di terakhir
for i in range (1, n-1):
    print('*', end = " ")
    for x in range (1, 2* n -1):
        print(' ', end = '')
    print('*')
for _ in range (1, 2* n +1):
    print('*', end='')
print() 