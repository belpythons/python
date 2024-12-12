import os
os.system('cls')

#  MODE WRITE INI AKAN SELALU MENIMPA
with open("coba tulis.txt", "a", encoding = "utf-8") as file:
    file.write("halo\n")
    file.write("helo")
with open("coba tulis.txt", "r+", encoding = "utf-8") as file:
    file.write("helo my name is hanif\n")
    file.write("holaaaa")