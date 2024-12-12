ulang = 20
for i in range(ulang):
    print ('sekarang perulangan ke: ', str (i))

item = ('apel', 'jeruk', 'semangka', 'nanas')
for list in item:
    print (list)

jawab = ('ya')
hitung = 0
while (jawab == 'ya'):
    hitung += 1
    jawab = input('ulang tidak bre?')
    if jawab == ('tidak'):
        break
print ('kamu sudah mengulang sebanyak: '+ str(hitung))



