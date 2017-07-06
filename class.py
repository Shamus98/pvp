class dog:
    def __init__(self, name, age, gender,breed):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
    def love(self, name):
        print(self.name, "любит", name)

bul = dog ("Буль",2, "мужчина","овчарка")
print(bul.age)
bul.age += 80
print(bul.age)
bul.love("Булька")

barbi = dog ("барби",1 , "ж","хаски")
print(barbi.gender)
barbi.love("папка")