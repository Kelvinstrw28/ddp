#mobil
kendaraan=["mobil","toyota","15000","hitam","4"]
print (kendaraan)
kendaraan.append("hitam")
print(kendaraan)
kendaraan.append("empat ban")
print(kendaraan)
kendaraan.append("300juta")
kendaraan.insert(2,"toyota")
print(kendaraan)

#2
pilih = int(input ("mau hitung apa? 3 untuk persegi, 5 untuk lingkaran, 2 segitiga"))

match pilih:
 case 3:
  print(int(input ("berapa sisinya?")) ** 2)
 case 5:
  print(3.14 * int(input ("berapa jari jari nya?")) **2)
 case 2:
  print(1/2 * int(input("berapa alasnya? ")) * int(input("berapa tingginya?")))
 case _:
  print("salah angka")
  
  #menhitung angka
  angka = int(input("Tulis sebuah angka:"))
  bilangan = int(input("Masukkan bilangan: "))

