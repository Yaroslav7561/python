sum = int(input("Введите сумму в рублях:"))
p100 = sum // 100
sum %= 100
p50 = sum // 50
sum %= 50
p10 = sum // 10
sum %= 10
p5 = sum // 5
sum %= 5
p2 = sum // 2
sum %= 2
p1 = sum
print("Купюр по 100:", p100)
print("Купюр по 50:", p50)
print("Купюр по 10:", p10)
print("Купюр по 5:", p5)
print("Монет по 2:", p2)
print("Монет по 1:", p1)