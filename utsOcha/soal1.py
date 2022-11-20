#mengurutkan 5 bilangan inputan user

myList = []

for i in range(1,6):
    try:
        myList.append(int(input(f"masukkan angka ke {i}: ")))
    except ValueError:
        print("inputan salah!! mohon masukkan angka yang benar")

print(15*'-')
print(f"\ndaftar angka {myList}")

myList.sort()

print(15*'=')
print(f"urutan dari yang terkecil adalah {myList}")