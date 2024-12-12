def hitung_grade(nilai):
    if nilai < 40:
        return 'E'
    elif 40 <= nilai < 55:
        return 'D'
    elif 55 <= nilai < 60:
        return 'C'
    elif 60 <= nilai < 65:
        return 'C+'
    elif 65 <= nilai < 70:
        return 'B-'
    elif 70 <= nilai < 75:
        return 'B'
    elif 75 <= nilai < 80:
        return 'B+'
    elif 80 <= nilai < 85:
        return 'A-'
    elif 85 <= nilai <= 100:
        return 'A'

def hitung_ipk(semester):
    total_nilai = 0
    jumlah_mata_kuliah = int(input(f'Masukkan jumlah mata kuliah di semester {semester}: '))
    
    for i in range(jumlah_mata_kuliah):
        mata_kuliah = input(f'Masukkan nama mata kuliah ke-{i + 1}: ')
        nilai = float(input(f'Masukkan nilai untuk {mata_kuliah}: '))
        total_nilai += nilai
    
    rata_rata = total_nilai / jumlah_mata_kuliah
    grade = hitung_grade(rata_rata)
    return rata_rata, grade

def main():
    semester_sekarang = int(input("Anda sedang berada di semester berapa?: "))
    ipk_total = 0
    
    for semester in range(1, semester_sekarang + 1):
        rata_rata, grade = hitung_ipk(semester)
        print(f'Semester {semester}: Rata-rata = {rata_rata:.2f}, Grade = {grade}')
        ipk_total += rata_rata
        
        # Menampilkan nilai IPK semester ini
        ipk_semester = rata_rata
        print(f'IPK untuk semester {semester}: {ipk_semester:.2f}\n')

    ipk_akhir = ipk_total / semester_sekarang
    print(f'IPK Akhir: {ipk_akhir:.2f}')

if __name__ == "__main__":
    main()
