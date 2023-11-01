print("Merhaba Tobeto")

#degiskenler 
#string
text = "Merhaba Tobeto" 
print(text)

StudentCount = "45" 

#int, integer => tam sayı 
StudentCount2 = 45 
#print(StudentCount + StudentCount2)
print(StudentCount2 + 5)

#double,decimal,float => ondalıklı sayıları
averagePoint = 25.5
print(averagePoint)

#boolean,bool => True- False 
isVerified = True 
print(isVerified)

print(type(text))
print(type(StudentCount2))
print(type(averagePoint))
print(type(isVerified))

#Matematiksel Operatörler 
# + - / * %

number = 10

print(10+10)
print(number + number)

print(number - 5)

print(number / 2)

print(number * 2)

#1 sol taraftaki değerin sağ taraftaki değere bölümünden kalan sonuç
print(number % 3)

#Mantıksal Operatörler 

print(number == 10) 
print(number == 11)

print(number != 10) #false
print(number != 11) #true

print(number > 10) #false
print(number >= 10) #true

print(number < 10) #false
print(number <= 10) #true

#string interpolation

hello = "Merhaba"
userName = "irem"
totalText = hello + " " + userName
print(totalText)

totalText = "{message} {name}".format(message =hello,name="elif")
print(totalText)

#f-string
totalText = f"Hoşgeldiniz {userName}"
print(totalText)
