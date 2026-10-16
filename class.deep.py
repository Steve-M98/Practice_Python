''' CLASS deep diving
    (1) ENCAPSULATION
    (2) INHERITENCE
    (3) POLIMORPHISM
    (4) DECORETOR ==>  < GETTER > &  < SETTER >
    '''
print("===== ENCAPSULATION =====")
# ENCAPSULATION > public __private _protected

# Pythonda    => public,  __ => private,   _  => protected  shu holatda yasaladi.


class Account():
    # state
    description = "The class makes bank accounts"
# constructor

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount
# method

    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

       # Agar bu maxfiy ma'lumotni olmoqchi bo'lsak < getter > orqali olsak bo'ladi. < @property > --> getter deyiladi.
    @property
    def holder(self):
        return self.__owner


# bu yerda getterni sherigi setter orqali o'sha getter qilib yasalgan holder methodini ishlatdik. Uni ichida maxfiy bo'lgan ownerni ismini o'zgartirish kodi yozildi.
# setter har doim geter method nomi < holder > bn bir hil o'lishi kerak


    @holder.setter
    def holder(self, new_owner):
        print("holder-setter:", new_owner)
        self.__owner = new_owner


my_account = Account("Shawn", 1000)
my_account.get_balance()

# owner va amount ni __ private qilganimiz uchun endi o'zgartirish imkoni yo'q

print("---------------")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()


# bu yerda account egasini ismini va depositlarini bemalol o'zgartirish mumkin bo'lib qolganiligi uchun havfsiz qilish kerak. Ya'ni private( __ ) belgisi bilan himoyalash k.k
print("----------------------------")
my_account.amount = 10000000
my_account.owner = "Martin"
my_account.amount = 100000000
my_account.get_balance()


# Aslida < holder > method lekin GETTER orqali qilganimiz uchun uni < state > qilib yoziladi. Shunda biz yozgan < holder > methodi ichidagi kod ishga tushadi.
my_account.holder
print("getterni ishlashi:", my_account.holder)

# SETTER ni methodini call qilishda uni ham < state > holda yozib to'ridan to'gri qiymatini berib ketilsa bo'ldi. printga javob chiqadi.
my_account.holder = "Steve"
