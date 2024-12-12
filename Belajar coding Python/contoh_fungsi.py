def coba_fungsi():
    print("="*35)
    print("="*10,"SELAMAT DATANG","="*10)
    print("="*35)


# def fungsi_len(judul):
#     hiasan = "="*len(judul)
#     print(hiasan)
#     print(f"{judul}")
#     print(hiasan)

def fungsi_len2(title):
    hiasan = "=" * (len(title) + 6)
    print (hiasan)
    print(f"***{title}***")
    print(hiasan)

def coba_semua():
    # fungsi_len()
    fungsi_len2()
    coba_fungsi()

coba_semua()
