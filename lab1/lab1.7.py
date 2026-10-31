min = int(input("Минут:"))
sms = int(input("СМС:"))
mb = int(input("Мб:"))
sum = 24.99
if min > 60:
    sum += (min - 60) * 0.89
    print("Лишние минуты:", round((min - 60) * 0.89, 2), "руб.")
if sms > 30:
    sum += (sms - 30) * 0.59
    print("Лишние СМС:", round((sms - 30) * 0.59, 2), "руб.")
if mb > 1000:
    sum += (mb - 1000) * 0.79
    print("Лишний интернет:", round((mb - 1000) * 0.79, 2), "руб.")
print("Налог:", round(sum * 0.02, 2), "руб.")
print("Итого:", round(sum * 1.02, 2), "руб.")

