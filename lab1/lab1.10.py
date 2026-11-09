sum = float(input("Сумма покупки: "))
age = int(input("Возраст: "))
birthday = input("Сегодня день рождения? (да/нет): ")
vip = input("Вы VIP-клиент? (да/нет): ")
s = 0
if sum > 1000:
    s = 10
if age >= 63:
    s = s + 5
if birthday == "да":
    s = s + 5
if (vip == "да") and (s < 15):
    s = 15
if s > 25:
    s = 25
print("Скидка:", s, "%")
print("Сумма:", sum - (sum * s / 100), "руб.")