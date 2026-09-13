print("Assalomu Alaykum Steve !!!")

message = " HELLO WORLD !"
print(message)
# ***********************
a = 40
b = 30
c = a + b
print(c)

x = 9
y = 10
z = x+y
print(z)


# Dunder _builtins_, _init_
# Python da hamma narsa object bo'ladi.
message = "PYTHON: Everything is object!"
print(message)

result = type(message)
print("result:", result)

# Pythondagi ichki o'rnatigan tollari:

'''In Python, there are builtin tools:  
(1) TYPES > int float str list dict
(2) FUNCTION > print() len() input() type()
(3) CONSTANTS > True False None


'''
print(dir(__builtins__))  # builtin ni ichidagi dunderlarni korish ucn yozildi.
