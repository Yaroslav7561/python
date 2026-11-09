def flatten_list(lst):
    i = 0
    while i < len(lst):
        if type(lst[i]) == list:
            if len(lst[i]) == 0:
                lst.pop(i)
            else:
                lst[i:i+1] = lst[i]
        else:
            i = i + 1


list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
print("До:", list_a)
flatten_list(list_a)
print("После:", list_a)