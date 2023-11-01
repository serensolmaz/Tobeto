#Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

sayi = input("Bir sayı giriniz: ")

sayininTersi = sayi[::-1]

if sayi == sayininTersi:
    print("Palindrom sayıdır.")
else:
    print("Palindrom sayı değildir.")
