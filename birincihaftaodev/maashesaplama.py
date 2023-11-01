#Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

maas = int(input("Maaşınızı giriniz: "))
zam = int(input("Zam oranını giriniz: "))

zamliMaas = maas + (maas*zam)/100

print(zamliMaas)
