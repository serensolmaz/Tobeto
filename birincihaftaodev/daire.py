#Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

import math

yaricap = float(input("Dairenin yarıçapını giriniz: "))

cevre = 2*math.pi*yaricap
alan = math.pi*yaricap**2

print("Çevre = ", cevre)
print("Alan = ", alan)
