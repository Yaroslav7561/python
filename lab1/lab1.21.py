import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        
        milliseconds = (end - start) * 1000
        print("Время выполнения:", milliseconds, "мс")
        
        return result
    return wrapper


@timing
def slow_function():
    total = 0
    for i in range(1000000):
        total = total + i
    return total


slow_function()