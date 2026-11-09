import datetime

def log_calls(file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = datetime.datetime.now()
            with open(file, "a", encoding="utf-8") as f:
                f.write(f"{now} | {func.__name__} | аргументы: {args}, {kwargs}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_calls("log.txt")
def summa(a, b):
    return a + b


@log_calls("log.txt")
def greet(name):
    return f"Привет, {name}!"


print("Сумма:", summa(5, 10))
print(greet("Аня"))
print(summa(1, 2))