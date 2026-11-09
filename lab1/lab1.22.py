def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args):
            for i in range(len(expected_types)):
                if type(args[i]) != expected_types[i]:
                    raise TypeError(f"Аргумент {i + 1} должен быть {expected_types[i]}, а получен {type(args[i])}")
            return func(*args)
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    return a + b


print(add(2, 3))
print(add("2", 3))