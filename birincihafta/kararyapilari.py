ortalamaNot = input("Lütfen Ortalamanızı giriniz.")
print(type(ortalamaNot))
ortalamaNotAsInteger = int(ortalamaNot)
print(type(ortalamaNotAsInteger))

if ortalamaNotAsInteger >80 :
    print("Geçtiniz")
    if ortalamaNotAsInteger >90:
        print("bravo")
elif ortalamaNotAsInteger > 50:
    print("Başarılı")
else:
    print("Maalesef kaldınız")
