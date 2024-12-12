while (True):
    angka = int(input("masukan angka: "))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        lanjut_enggak = input("apakah mau lanjut? (y/n)")
        if lanjut_enggak == "y":
            continue
        elif lanjut_enggak == "n":
            break
        else:
            print("MASUKAN Y ATAU N")
    except:
        print("pembagi nol silahkan ulangi lagi")
    finally:
        print("program selesai")
    
print("program selesai bro")
