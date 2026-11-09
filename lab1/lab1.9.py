print("Доступные единицы: мм, см, м, км, сек, мин, час, мл, л, м3")

a = input("Из какой единицы: ")
b = input("В какую единицу:")
c = float(input("Значение:"))

if a == "мм": d = c * 0.001
elif a == "см": d = c * 0.01
elif a == "м": d = c * 1
elif a == "км": d = c * 1000
elif a == "сек": d = c * 1
elif a == "мин": d = c * 60
elif a == "час": d = c * 3600
elif a == "мл": d = c * 0.001
elif a == "л": d = c * 1
elif a == "м3": d = c * 1000

if b == "мм": d = d / 0.001
elif b == "см": d = d / 0.01
elif b == "м": d = d / 1
elif b == "км": d = d / 1000
elif b == "сек": d = d / 1
elif b == "мин": d = d / 60
elif b == "час": d = d / 3600
elif b == "мл": d = d / 0.001
elif b == "л": d = d / 1
elif b == "м3": d = d / 1000

print(c, a, "=", d, b)