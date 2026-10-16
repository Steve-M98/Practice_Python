'''FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
'''
print("===== DEFINE (parameter) vs CALL (argument) =====")
# build in function > print() type()
# Function - reusable block of code! ==> ma'lum bir joyda ma'lum bir kodni ishga tushiruvchi kod block
# JAVA larda function ni { qavs ichiga } yozib quriladi. PYTHON da : nuqta qoyib keyin yozib ketiladi  "Indentation" deyiladi

# DEFINE - (build), parameter


def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - argument
result1 = greeting('Martin')
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)

print("==== Keyword & default arguments ====")

# DEFINE


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL
# bu holatda yozishh keyword argument deyiladi.
result3 = give_greet(name="Justin", age=28)
print("result3:", result3)

# shu holatda yozsak ham javob bir hil chiqadi.
# result3 = give_greet("Justin", 28)


# bu yerda 2 chi argumentni bermadik age ga qiymat bermadik bu holatda parametrga default qiymatni berib qoyish kerak.
result4 = give_greet("John")
print("result4:", result4)


print("===== Scope =====")
b = 100  # 3

# DEFINE
# bu yerda izlanayotgan qiymat scopka ni ichida bo'lsa birinchi ichidan keyin parametrdan unda ham yo'q bolsa tashqaridan izlaydi


def calculate(a):  # 2
    c = a * b       # 1
    print(f"the c value: {c}")


# CALL
calculate(5)
