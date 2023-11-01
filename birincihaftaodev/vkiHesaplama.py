#Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

agirlik = float(input("Kilonuzu giriniz: "))
boy = float(input("Boyunuzu giriniz: "))

vki= agirlik / (boy*boy)

print("Vücut kitle indeksiniz = " , vki)
