from transformers import LEDForConditionalGeneration, LEDTokenizer

# Load pre-trained Longformer model and tokenizer
model_name = "allenai/led-large-16384"
tokenizer = LEDTokenizer.from_pretrained(model_name)
model = LEDForConditionalGeneration.from_pretrained(model_name)

def summarize_long_text(text):
    # Tokenize input text (maximum input length is 16,384 tokens)
    inputs = tokenizer(text, max_length=16384, return_tensors="pt", truncation=True)

    # Generate summary (we set a longer output length here)
    summary_ids = model.generate(
        inputs['input_ids'],
        max_length=1024,  # Maximum output length (summary length)
        min_length=200,   # Minimum output length
        length_penalty=2.0,
        num_beams=4,      # Beam search for better results
        early_stopping=True
    )

    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Example of a long input text
long_text = """Bahasa memegang peranan penting dalam kehidupan manusia karena 
bahasa merupakan alat komunikasi manusia dalam kehidupan sehari-hari. Hal 
ini sejalan dengan pendapat Noermanzah (2017:2) menjelaskan bahwa bahasa 
merupakan pesan yang disampaikan dalam bentuk ekspresi sebagai alat 
komunikasi pada situasi tertentu dalam berbagai aktivitas. Mempelajari bahasa 
asing, termasuk Bahasa Jerman, merupakan bekal penting untuk melangkah 
dalam kehidupan global. Namun, tidak dapat kita pungkiri terdapat beberapa 
hambatan yang menyebabkan seorang pemula kesulitan dalam belajar. Menurut 
Arianty dan Lusi (2019) pada penelitiannya mengatakan bahwa masih banyak 
anak muda yang tidak tertarik untuk belajar bahasa asing karena ketidaktahuan 
akan manfaat belajar bahasa asing dan prasarana yang tidak memadai. Hal ini 
juga dirasakan oleh para pemula yang sedang belajar bahasa Jerman.
Pembelajaran bahasa Jerman pada awal pertengahan tahun 70 hingga 80-an 
adalah penguasaan bahasa lisan dengan menggunakan metode audio-lingual. 
Kemudian, metode pengajaran bahasa beralih kepada pendekatan komunikatif 
pada tahun 1900-an. Media belajar yang digunakan kebanyakan berupa audio 
dan video yang mana pembelajaran hanya berjalan satu arah saja. Seiring 
berkembangnya zaman terdapat beberapa sarana belajar bahasa asing dalam 
bentuk platform dan aplikasi seperti Duolingo, Learn German, Busuu, dan lain 
sebagainya. Namun, terdapat beberapa kelemahan salah satunya harus 
bergantung pada jaringan internet, minimnya konten atau fitur tertentu, dan 
tidak semua aplikasi atau platform belajar bahasa asing menawarkan 
pembelajaran bahasa Jerman terutama pada keterampilan berbicara (sprechen).
Kelemahan itulah yang menjadi salah satu faktor penting adanya solusi inovatif 
yang dapat meningkatkan kemampuan pemahaman kosakata dan berbicara 
dalam Bahasa Jerman, sekaligus solusi yang dapat meningkatkan kemandirian 
dalam belajar di era global. 
Berdasarkan permasalahan di atas, penulis memberikan inovasi untuk 
membuat suatu media belajar dengan judul “Pemanfaatan Teknologi Robot 
Berbasis Artificial Intelligence dalam Meningkatkan Kemampuan Berbahasa 
Jerman Sebagai Media Belajar Mandiri di Era Global”. Robot ini akan 
membantu dan memudahkan para pemula yang sedang belajar bahasa Jerman 
secara mandiri terutama pada pemahaman kosakata dan keterampilan sprechen
(berbicara). Selain itu, robot ini juga memiliki dasar dan aspek linguistik yang 
dilengkapi sistem kamera untuk mendeteksi dan mengikuti pergerakan wajah 
serta memiliki sistem program berbasis Artificial Intelligence yang mampu 
membuat robot bisa berdialog dengan user
"""

# Summarize the long text
summary = summarize_long_text(long_text)
print("Summary:")
print(summary)
