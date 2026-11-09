text = input("введите текст: ")
words = text.split()

print("общее количество слов:", len(words))

print("частота слов:")
shown = []
for w in words:
    if w not in shown:
        print(w, ":", words.count(w))
        shown.append(w)

top = ""
top_n = 0
for w in words:
    n = words.count(w)
    if n > top_n:
        top_n = n
        top = w
print("самое частое слово:", top)

short = words[0]
long = words[0]
for w in words:
    if len(w) < len(short):
        short = w
    if len(w) > len(long):
        long = w
print("самое короткое слово:", short)
print("самое длинное слово:", long)

# оставляем слова длиной 3 и больше
new_words = []
for w in words:
    if len(w) >= 3:
        new_words.append(w)

print(" анализ после фильтрации ")
print("осталось слов:", len(new_words))

top2 = ""
top_n2 = 0
for w in new_words:
    n = new_words.count(w)
    if n > top_n2:
        top_n2 = n
        top2 = w
print("самое частое слово:", top2)

short2 = new_words[0]
long2 = new_words[0]
for w in new_words:
    if len(w) < len(short2):
        short2 = w
    if len(w) > len(long2):
        long2 = w
print("самое короткое слово:", short2)
print("самое длинное слово:", long2)