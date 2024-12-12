def hitung_grade(nilai):
    if nilai < 40:
        return 'E', 0.00
    elif 40 <= nilai < 55:
        return 'D', 1.00
    elif 55 <= nilai < 60:
        return 'C', 2.00
    elif 60 <= nilai < 65:
        return 'C+', 2.33
    elif 65 <= nilai < 70:
        return 'B-', 2.67
    elif 70 <= nilai < 75:
        return 'B', 3.00
    elif 75 <= nilai < 80:
        return 'B+', 3.33
    elif 80 <= nilai < 85:
        return 'A-', 3.67
    elif 85 <= nilai <= 100:
        return 'A', 4.00

def hitung_ipk(semester):
    total_nilai = 0
    jumlah_mata_kuliah = int(input(f'Masukkan jumlah mata kuliah di semester {semester}: '))
    
    for i in range(jumlah_mata_kuliah):
        mata_kuliah = input(f'Masukkan nama mata kuliah ke-{i + 1}: ')
        nilai = float(input(f'Masukkan nilai untuk {mata_kuliah}: '))
        total_nilai += nilai
    
    rata_rata = total_nilai / jumlah_mata_kuliah
    grade, ipk = hitung_grade(rata_rata)
    return rata_rata, grade, ipk

def main():
    semester_sekarang = int(input("Anda sedang berada di semester berapa?: "))
    ipk_total = 0
    
    for semester in range(1, semester_sekarang + 1):
        rata_rata, grade, ipk = hitung_ipk(semester)
        print(f'Semester {semester}: Rata-rata = {rata_rata:.2f}, Grade = {grade}, IPK = {ipk:.2f}')
        ipk_total += ipk
        
        # Menampilkan nilai IPK semester ini
        print(f'IPK untuk semester {semester}: {ipk:.2f}\n')

    ipk_akhir = ipk_total / semester_sekarang
    print(f'IPK Akhir: {ipk_akhir:.2f}')

if __name__ == "__main__":
    main()
