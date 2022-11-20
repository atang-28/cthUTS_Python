#menghitung dengan rumus pythagoras

cariApa = input("sisi yang akan dicari [alas/tinggi/miring] : ")

if cariApa == "alas":
    tinggi = int(input("Masukkan nilai tingginya : "))
    miring = int(input("Masukkan nilai sisi miringnya : "))

    #rumus pythagoras
    alas = (miring ** 2) - (tinggi ** 2)
    hasil = alas ** 0.5
    print("nilai alas yang dicari adalah", hasil)

elif cariApa == 'tinggi':
    alas = int(input("Masukkan nilai alasnya : "))
    miring = int(input("Masukkan nilai sisi miringnya : "))

    #rumus pythagoras
    tinggi = (miring ** 2) - (alas ** 2)
    hasil = tinggi ** 0.5
    print("nilai tinggi yang dicari adalah",hasil)

elif cariApa == "miring":
    tinggi = int(input("Masukkan nilai tingginya : "))
    alas = int(input("Masukkan nilai alasnya : "))

    #rumus pythagoras
    miring = (alas ** 2) + (tinggi ** 2)
    hasil = miring ** 0.5
    print("nilai sisi miring yang dicari adalah",hasil)

else:
    print("perhatikan format penulisan dan inputan angka yang diminta!!!")