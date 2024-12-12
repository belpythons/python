def step_1():
    print("Step 1: Perintah berhasil dilakukan.")

def step_2():
    print("Step 2: Perintah berhasil dilakukan.")

def step_3():
    print("Step 3: Perintah berhasil dilakukan.")

def step_4():
    print("Step 4: Perintah berhasil dilakukan.")

def step_5():
    print("Step 5: Perintah gagal dilakukan.")
    raise Exception("Error: Gagal di Step 5")  # Simulasi kegagalan pada step 5

def run_program():
    try:
        step_1()  # Melakukan perintah pertama
        step_2()  # Melakukan perintah kedua
        step_3()  # Melakukan perintah ketiga
        step_4()  # Melakukan perintah keempat
        step_5()  # Melakukan perintah kelima (yang akan gagal)
    except Exception as e:
        print(e)
        print("Mengulangi dari step ke-3 karena kegagalan di step akhir...")
        # Ulang dari tengah (step ke-3)
        try:
            step_3()
            step_4()
            step_5()  # Bisa gagal lagi jika error masih ada
        except Exception as e:
            print(e)
            print("Masih gagal, program berhenti.")
            return
    
    print("Program berhasil selesai.")

# Menjalankan program
run_program()
