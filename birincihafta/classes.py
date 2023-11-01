class Human:
    #property, attribute => özellik nitelik
    # name=" "
    # age = 25

    #instance üretilen noktada ilk çalışan yapıcı bloktur
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        print("yapıcı blok çalıştı")

    #methods, davranışlar 
    def talk(self,message):
        print(message)

    def walk(self):
        print(f"{self.name} is Walking")


human1 = Human("Elif", 24) #instance üretmek => örnek ürettik
# human1.name = "Elif"
# human1.age = 24
human1.talk("Merhaba")
human1.walk()
