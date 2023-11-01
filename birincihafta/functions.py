#definition
def ortalamaHesapla() :
    final =75
    vize = 48
    ortalama = (vize*0.4) + (final * 0.6)
    print(ortalama)

def ortalamaHesaplaVeDöndür() : 
    final =75
    vize = 48
    ortalama = (vize*0.4) + (final * 0.6)
    return ortalama #fonk çağrıldığı yere değer götürür


ortalamaHesapla()
print(ortalamaHesaplaVeDöndür())

def ortalamaHesaplaVeYazdir(vize:float,final:float) -> float:
    return (vize*0.4) + (final*0.6)


print(ortalamaHesaplaVeYazdir(66,77))


vize=int(input("Vize notunuzu giriniz: "))
final=int(input("Final notunuzu giriniz: "))

def ortalamaHesapla2(vize=vize,final=final):
    return (vize*0.4) + (final*0.6)


print(ortalamaHesapla2())
