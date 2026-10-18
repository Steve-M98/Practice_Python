''' CLASS deep diving
    (1) ENCAPSULATION
    (2) INHERITENCE <
    (3) POLIMORPHISM <
'''
print("===== INHERITENCE ======")

# PARENT > CHILD
# PARENT class ===> CHILD larga public va protected property (state va method) larini bera oladi.


class Animal:  # Parent
    description = "This a classs is parent for animals"

    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):   # Child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self. sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")


class Cat(Animal):   # Child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # Child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("************************")
dog.make_voice()
fish.make_voice()

print("************************")

# buyerda asosiy Parent classdagi state va methodlarni child larda ham ishlatdik
print(Animal.description)
print(Dog.description)

print(dog.voice, fish. voice)
print("dog status:", dog._status)
print("cat status:", cat._status)

print("===== POLIMORPHISM ======")
# bu bir hil nomdagi methodni har hil korinishda yozib ishlatish.
# Ya'ni Parentda yozilgan methodni nomi bilan bir hil nomdagi methodni child ni ichiga yozilsa hammasi o'z klasiidagi methodni ishga tushiradi.
# agar o'zida bo'lmasa keyin parentdagi methodni qabul qiladi.
dog.make_voice()
fish.make_voice()

print("************************")

#  buyerda fish ni Fish clasdan olinganini tekshiryapmiz
#  buyerda Fish ni Animal clasdan olinganini tekshiryapmiz
#  buyerda Animal ni object clasdan olinganini tekshiryapmiz
#  ya'ni hammsi oxiri OBJECT clasidan olingan chunki PYTHONDA hamma narsa OBJECT


# fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print(f"the result: {result}")


#  tepada yozib tekshiragn ishimizni endi < issubclass > functioni orqali ham yozib tekshirdik

# Fish > Animal > object
datal = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", datal, data2)
