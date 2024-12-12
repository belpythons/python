import cv2
import os
import numpy

os.system("cls")

image = cv2.imread("contoh gambar.jpg")         #imread untuk membaca gambar
image2 = cv2.imread("contoh gambar.jpg", 0)     #digunakan untuk mengganti warna menjadi abu-abu 
# image3 = cv2.imread("contoh gambar.jpg", 100)
# image4 = cv2.imread("contoh gambar.jpg", 300)
print(image.shape)

x = image.shape [0] * 0.5
y = image.shape [1] * 0.5
dimensi = (x, y)

resize = cv2.resize("contoh gambar.jpg", dimensi)



cv2.imshow("contoh gambar1", image)             #imshow digunakan untuk menampilkan gambar
cv2.imshow("contoh gambar2", image2)
# cv2.imshow("contoh gambar3", image3)
# cv2.imshow("contoh gambar4", image3)
cv2.waitKey(0)
cv2.destroyAllWindows()