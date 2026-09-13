'''FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
'''
print("===== DEFINE (parameter) vs CALL (argument) =====")
# build in function > print() type()
# Function - reusable block of code!
# Instead of block f} in JAVA, Python uses indentation!

# DEFINE - (build), parameter


def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - argument
result1 = greet('Martin')
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)

print("==== Keyword & default arguments ====")

# DEFINE


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL
result3 = give_greet(name="Justin", age=28)
print("result3:", result3)

result4 = give_greet("John")
print("result4:", result4)


print("===== Scope =====")
b = 100  # 3

# DEFINE


def calculate(a):  # 2
    c = a * b       # 1
    print(f"the c value: {c}")


# CALL
calculate(5)
