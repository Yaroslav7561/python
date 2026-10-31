import random
a = random.randint(1, 100)
b = 0
print("Угадай число от 1 до 100!")
while b != a:
    b = int(input("Твоя догадка:"))
    if b < a:
        print("Больше")
    elif b > a:
        print("Меньше")
    else:
        print("Ты угадал число", a)