sayilar = [100,200,300,400,"Merhaba"] 
#Programcı saymaya 0'dan başlarız 
print(sayilar[0])
print(sayilar)
#listenin sonuna eleman ekler
sayilar.append(600)
print(sayilar)
#değere göre silme işlemi gerçekleştirir
sayilar.remove("Merhaba") 
print(sayilar)
#indexe göre siler
sayilar.pop(2)
print(sayilar)
#çoklu veri ekleme
sayilar.extend([10,20,30])
print(sayilar)
#dizinin içini temizliyor
sayilar.clear()
print(sayilar)
