import array

angka = []

for i in range(5):
    isi = input('masukkan angka: ').format(i+1)
    if isi == 'stop':
        break
    angka.append(isi)

print('isi array: ',angka)

