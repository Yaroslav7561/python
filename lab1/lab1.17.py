def merge_dicts(dict_a, dict_b):
    for key in dict_b:
        if key in dict_a:
            val_a = dict_a[key]
            val_b = dict_b[key]

            if type(val_a) == dict and type(val_b) == dict:
                merge_dicts(val_a, val_b)
            
            elif type(val_a) == list and type(val_b) == list:
                for item in val_b:
                    if item not in val_a:
                        val_a.append(item)
            
            elif type(val_a) == tuple and type(val_b) == tuple:
                for item in val_b:
                    if item not in val_a:
                        val_a = val_a + (item,)
                dict_a[key] = val_a
            
            elif type(val_a) == set and type(val_b) == set:
                for item in val_b:
                    val_a.add(item)
            
            else:
                dict_a[key] = val_b
        else:
            dict_a[key] = dict_b[key]


dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}} 

print("До:", dict_a)
merge_dicts(dict_a, dict_b)
print("После:", dict_a)