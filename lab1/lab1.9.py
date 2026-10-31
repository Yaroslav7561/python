choice = input("Выберите категорию (длина, масса, время, температура): ")

if choice == 1:
    a1 = input("Из какой единицы (мм, см, м, км): ")
    a2 = input("В какую единицу (мм, см, м, км): ")
    value = float(input("Значение: "))
    
    if a1 == 1:
        a3 = value
    elif a1 == 2:
        a3 = value * 10
    elif a1 == 3:
        a3 = value * 1000
    elif a1 == 4:
        a3 = value * 1000000
    
    if a2 == 1:
        result = a3
    elif a2 == 2:
        result = a3 / 10
    elif a2 == 3:
        result = a3 / 1000
    elif a2 == 4:
        result = a3 / 1000000
    
    print("Результат:", result)

elif choice == 2:
    a1 = input("Из какой единицы (г, кг, т): ")
    a2 = input("В какую единицу (г, кг, т): ")
    value = float(input("Значение: "))
    
    if a1 == 1:
        a3 = value
    elif a1 == 2:
        a3 = value * 1000
    elif a1 == 3:
        a3 = value * 1000000
    
    if a2 == 1:
        result = a3
    elif a2 == 2:
        result = a3 / 1000
    elif a2 == 3:
        result = a3 / 1000000
    
    print("Результат:", result)

elif choice == 3:
    a1 = input("Из какой единицы (сек, мин, час): ")
    a2 = input("В какую единицу (сек, мин, час): ")
    value = float(input("Значение: "))
    
    if a1 == "сек":
        a3 = value
    elif a1 == "мин":
        a3 = value * 60
    elif a1 == "час":
        a3 = value * 3600
    
    if a2 == "сек":
        result = a3
    elif a2 == "мин":
        result = a3 / 60
    elif a2 == "час":
        result = a3 / 3600
    
    print("Результат:", result)

elif choice == 4:
    a1 = input("Из какой единицы (C, F, K): ")
    a2 = input("В какую единицу (C, F, K): ")
    value = float(input("Значение: "))
    
    if a1 == "C":
        a3 = value
    elif a1 == "F":
        a3 = (value - 32) * 5 / 9
    elif a1 == "K":
        a3 = value - 273.15
    
    if a2 == "C":
        result = a3
    elif a2 == "F":
        result = a3 * 9 / 5 + 32
    elif a2 == "K":
        result = a3 + 273.15
    
    print("Результат:", result)

else:
    print("Неизвестная категория")