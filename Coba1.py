#jika itu adalah teks maka menggunaakn tanda petik 
#jika itu adalah angka maak tidak menggunakan tanda petik
nama = "Hanif NurKhalis"
umur = 30
print("Halo, nama saya", nama, "dan saya berusia", umur, "tahun.")

nama = "hanif nurkhalis"
panggilan = "hanif"
print("============PERCOBAAN 1============")
print("perkenalkan nama saya", nama, "biasa dipanggil", panggilan, "dan umur saya adalah", umur)

a = 10
b = 20
c = 30
jawab = 60
pertanyaan = "berapakah hasilnya?"
print("jika sebuah balok memiliki panjang", a, "memiliki tingggi", b, "dan memiliki lebar", c, pertanyaan, "=", jawab)
print("jika sebuah tempat memiliki cadangan sumber air sebesar", a, "liter, dan itu dapat digunakan selama", b, "hari untuk satu orang, dan jika itu digunakan untuk 3 orang maka membutuhkan lebih dari", c, "liter air")
print("===========PERCOBAAN 2===========")

#float merupakan penggunaan angka yang menggunakan tanda koma atau bilangan pecahan
#jika tidak menggunakan perintah float pada kalkulator maka hasil yang ditampilkan tidak akan menggunakan koma
a = 10
b = 20
c = float (a) * float (b)

print ("jika", a, "x", b, "=", float (c))
print("===========PERCOBAAN 3===========")

#foo merupakan perintah atau kata untuk list
#foo bukan menggunakan kurung tutup yang miring tetapi menggunakan kurung tutup yang lurus/tergak
#dapat dilihat seperti pada program tersebut 
foo = ["Hanif", "Nur", "Khalis", "Bantul", "Yogyakarta", "Kasihan", "True", "100"]
print(foo)
print(foo[0])
print(foo[4])
print("halo perkenalkan nama saya", foo[0], "saya tinggal di", foo[4])

print("========print foo 2=======")
foo[0] = "Hanif NurKhalis"
foo[7] = "tempat tinggalku di Kasihan Bantul Yogyakarta"
print(foo)
print(foo[1:4])
print(foo[2:])
print(foo[:3])  
print(foo[:])

print("======INPUT OUTPUT======")
a = float(input("masukan input a : "))
b = float(input("masukan input b : "))
print(a * b)

