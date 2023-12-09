'''
Jumlah 4 buah bilangan kuadrat pertama adalah 30 (30=1+4+9+16),
Buat program untuk menghitung berapakah jumlah 1000 bilangan kuadrat pertama, menggunakan while loop
'''

b = 1
total = 0

# Perulangan while
while b <= 1000:
    # Menambahkan kuadrat bilangan ke jumlah
    total = total + b ** 2
    hitung = b + 1

print(total)
