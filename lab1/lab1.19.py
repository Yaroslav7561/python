def cache(func):
    memory = {}
    
    def wrapper(*args):
        if args in memory:
            return memory[args]
        else:
            result = func(*args)
            memory[args] = result
            return result
            
    return wrapper


@cache
def slow_add(a, b):
    print("Выполняю сложение...")
    return a + b


print(slow_add(2, 3))
print(slow_add(2, 3))
print(slow_add(2, 3))