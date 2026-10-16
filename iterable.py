print("===== Iterable objects & RANGE =====")
# Iterable objects > string, dict, tuple, list, range, map, filter;


range_obj = range(3)
print(" range_obj:", range_obj)

# ==> bu yerda for orqali. loop qilib har bir harfni consolga chiqaryapti
for letter in "MIT":
    print(f"the letter: {letter}")

for ele in range_obj:
    print(f"the element: {ele}")

    # ========================================

    print("===== DICTIONARY =====")
# Dictionary is JSON object!


# bu eski holatda object hosil qilish
person = {"name": "Justin", "age": 25, "single": True}

# bu esa < dict > methodi orqali object hosil qilindi. 2 lasi ham bir hil natija beradi.
person_obj = dict(name="Justin", age=25, single=True)

print(f"the person: {person}")
print(f"the person_obj: {person_obj}")


# method: get ()
# name = person_obj ["name"]
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"the name: {name}, hobby: {hobby} and balance: {balance}")

# agar del operatoriga person_obj ni qaysidir qiymatini bersak o'sha qiymatni o'chirib qolgan qiymatlarini qaytaradi.
del person_obj["single"]
for key in person_obj:
    print(f"the key: {key} > value {person_obj.get(key)}")

  # shunda bizga single qiymatini bermasdan name va age larni chiqaradi
  # bu yerda ham person_obj ni for orqali loop qilib key va uning valu sini iterate qilib oldik
