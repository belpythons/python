import os

os.system("cls")
amount = input ("Enter the number of student : ")
while amount == "" or amount.isnumeric() == False:  #isnumeric() untuk agar bilangan tersebut harus angka kalau untuk hutug pakai isalhpa()
    print("please enter the valid number! \n")
    amount = input("Enter the number of Student: ")
amount = int(amount)
# man = "He"
# woman = "She"
arrayName =  []
arrayGender = ["He", "She"]
arrayAddress = []
arrayMajor = []
arrayExpertise = []
for x in range(amount):
    print("\n", "="*20)
    print("student" + str (x+1) + ":")
    nameRemanem = input("Name : ")
    genderRemanem = input("Gender List \n 1.Male \n 2.Female\n : ")
    if genderRemanem == 1:
        arrayGender.append[0]
    elif genderRemanem == 2:
        arrayGender.append[1]
    addresRemanem = input("Addres : ")
    majorRemanem = input ("Major : ")
    expertiseRemanem = input("Expertise : ")
    arrayName.append(nameRemanem)
    arrayGender.append(genderRemanem)
    arrayAddress.append(addresRemanem)
    arrayMajor.append(majorRemanem)
    arrayExpertise.append(expertiseRemanem)

    if os.name == "nt":
        os.system ("cls")
    else:
        os.system("clear")

print("Result of Students Recap Data")
for i in range (len(arrayName)):
    print(str(i+1) + "," + arrayName[i] + "live in" + arrayAddress[i] + "," + genderRemanem(arrayGender[i]) + " majored in" + arrayMajor[i] + "With" + arrayExpertise[i] +"expertise")