suhu_perkebunan = float(input('masukan suhu perkebunan sekarang: '))
if suhu_perkebunan <= 20 :
    kondisi =  ('sangat dingin')
    saran = "Hentikan penyiraman"
elif suhu_perkebunan <= 25 :
    kondisi =  ('dibawah normal')
    saran = "Hentikan penyiraman"
elif suhu_perkebunan <= 32 :
    kondisi =  ('normal')
    saran = "Alirkan air ke area tanaman"
elif suhu_perkebunan <= 45 :
    kondisi =  ('cukup panas')
    saran = "Alirkan air ke area tanaman dan Semprotkan air dengan mode hujan ringan"
elif suhu_perkebunan <= 50 :
    kondisi =  ('panas')
    saran = "Alirkan air ke area tanaman dan Semprotkan air dengan mode hujan sedang"
else :
    kondisi =  ('sangat panas')
    saran = "Alirkan air ke area tanaman dan Semprotkan air dengan mode hujan lebat"

print ('kondisi perkebunan saat ini: ', kondisi)
print ('Tindakan Operator: ', saran)