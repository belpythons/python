from transformers import BartForConditionalGeneration, BartTokenizer

# Load the pre-trained model and tokenizer
model_name = "facebook/bart-large-cnn"
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)

def summarize_text(text):
    # Tokenize the input text
    inputs = tokenizer(text, max_length=1024, return_tensors="pt", truncation=True)

    # Generate summary using the model
    summary_ids = model.generate(inputs['input_ids'], max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# print("\n")
# print("Masukan Teks yang akan di Ringkas")
# Example text
text = (""" Lulusan Perguruan Tinggi dituntut untuk memiliki academic knowledge, skill of thinking, management skill, dan communication skill. Kekurangan atas salah satu dari keempat keterampilan/kemahiran tersebut dapat menyebabkan berkurangnya mutu lulusan. Sinergisme akan tercermin melalui kemampuan lulusan dalam kecepatan menemukan solusi atas persoalan yang dihadapinya. Dengan demikian, pemikiran dan perilaku yang ditunjukkan mahasiswa akan bersifat kreatif (unik dan bermanfaat) dan konstruktif (dapat diwujudkan). Kemampuan berpikir kreatif dan bertindak inovatif mahasiswa dapat disalurkan melalui Program Kreativitas Mahasiswa (PKM). PKM berawal dari tahun 2001 dikembangkan untuk mengantarkan mahasiswa mencapai taraf pencerahan kreativitas dan inovasi berlandaskan penguasaan sains dan teknologi serta keimanan yang tinggi. Dalam rangka mempersiapkan diri menjadi pemimpin yang cendekiawan, wirausahawan mandiri dan arif, mahasiswa diberi peluang untuk mengimplementasikan kemampuan, keahlian, sikap, tanggung jawab, membangun kerjasama tim maupun mengembangkan kemandirian melalui kegiatan yang kreatif dalam bidang ilmu yang ditekuni. Program kreativitas yang dikhususkan bagi mahasiswa ini mengikuti perkembangan teknologi dalam era revolusi industri dalam mempersiapkan Sumber Daya Manusia yang mampu bersaing di era global. Di tingkat Perguruan Tinggi PKM menjadi program rutin dengan pembinaan yang terstruktur, yang berdampak meningkatnya kualitas proposal PKM dan atau karya tulisnya. Pada awalnya dikenal lima kegiatan yang ditawarkan dalam PKM, yaitu PKM-Penelitian (PKM-P), PKM-Kewirausahaan (PKM-K), PKM-Pengabdian kepada Masyarakat (PKM-M), PKM-Penerapan Teknologi (PKM-T) dan PKM-Penulisan Ilmiah (PKM-I). Namun sejak Januari 2009, Ditlitabmas mengelola 6 (enam) PKM. Kompetisi Karya Tulis Mahasiswa (KKTM) yang semula menjadi tugas Direktorat Akademik dalam pengelolaannya, dilimpahkan kepada Ditlitabmas. Karena sifatnya yang identik dengan PKM-I, KKTM selanjutnya dikelola bersama-sama PKM-I dalam PKM-Karya Tulis (PKM- KT). Dengan demikian, di dalam PKM-KT terkandung dua program penulisan, yaitu PKM-Artikel Ilmiah (PKM-AI) dan PKM-Gagasan Tertulis (PKM-GT). PKM-I atau selanjutnya disebut PKM-AI merupakan artikel hasil kegiatan yang ditampilkan pada laman simbelmawa. Sedangkan PKM GT yang berpeluang didiskusikan dalam forum terbuka, diposisikan sebagai pengganti PKM AI. Pada tahun 2011, jumlah bidang PKM bertambah menjadi 7 (tujuh) dengan diperkenalkannya bidang PKM-Karsa Cipta """)

# Summarize the text
summary = summarize_text(text)
print("Ringkasannya")
print("Summary:")
print(summary)
