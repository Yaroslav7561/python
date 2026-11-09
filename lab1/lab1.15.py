sales = []

count = int(input("Сколько видов товаров вы хотите ввести? "))

for i in range(count):
    print(f"\nТовар {i + 1}:")
    name = input("Название: ")
    price = float(input("Цена: "))
    qty = int(input("Количество: "))
    
    sales.append({"name": name, "price": price, "qty": qty})

revenue = {}
for item in sales:
    name = item["name"]
    total = item["price"] * item["qty"]
    if name in revenue:
        revenue[name] = revenue[name] + total
    else:
        revenue[name] = total

print("\nВыручка по товарам:")
for name in revenue:
    print(name, "-", revenue[name])

best = ""
best_sum = 0
for name in revenue:
    if revenue[name] > best_sum:
        best_sum = revenue[name]
        best = name

print("Самый прибыльный товар:", best, "-", best_sum)

unique = []
for item in sales:
    if item["name"] not in unique:
        unique.append(item["name"])

print("Уникальных наименований:", len(unique))