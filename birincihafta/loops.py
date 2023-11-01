#FOR DÖNGÜSÜ
#start - Döngü kaçtan başlasın (0) (Alt limit)
#stop - Döngü kaça kadar devam etsin (Üst Limit)
#step - Döngü kaçar kaçar artsın (1)

# for i in range(10):
#     print(i) 


#Kullanıcının girdiği sayılar arasında en büyük olanı verir
""" biggestValue = 0

for i in range(5):
    sayi = int(input(f"{i+1}. sayıyı giriniz."))
    if sayi > biggestValue:
        biggestValue = sayi

print(f"Girdiğiniz sayılar arasında en büyük olanı: {biggestValue}") """


#Çift Sayıları yazdıran döngü 

""" forRangeMin = int(input("Döngünün alt limitini belirleyiniz: "))
forRangeMax = int(input("Döngünün üst limitini belirleyiniz: "))

for i in range(forRangeMin,forRangeMax+1):
    if i % 2 == 0 :
        print(i) """

#Diziye kullanıcıdan aldığımız sayıları ekleme
""" sayilar = []

for i in range(3):
    sayilar.append(int(input(f"{i+1}. sayiyi giriniz. ")))
#defaultu küçükten büyüğe
sayilar.sort(reverse=True) #büyükten küçüğe 
print(sayilar)

print(min(sayilar))
print(max(sayilar)) """

#Dizi elemanlarını listeleme
""" ogrenciler = ["Melike", "Halil", "Uğur","Seren","irem"] 
#length
print(len(ogrenciler))

for i in range(len(ogrenciler)):
    print(f"{i+1}. Ogrenci:  {ogrenciler[i]}")

for ogrenci in ogrenciler:
    print(f"Öğrenci: {ogrenci}") """

#break => ilgili döngünün o anda kırılmasını sağlıyor 
""" ogrenciler = ["Melike", "Halil", "Uğur","Seren","irem"] 
for i in range(len(ogrenciler)):
    if i>2 :
        break
    print(f"{i+1}. Ogrenci:  {ogrenciler[i]}") """

#continue => iterasyondaki current değeri atla , bir sonraki değer ile devam et
""" for i in ogrenciler:
    if i=="Halil":
        continue
    print(f"Öğrenci: {i}") """


#WHILE 
i= 0
while i <10:
    print("Merhaba")
    i += 1
