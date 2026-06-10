def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_args
def add(a, b):
    return a + b

@log_args
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Decorate the functions (デコレーター構文を使っているので手動再代入は不要)
result1 = add(2, 3)
result2 = greet("Alice")
result3 = greet("Bob", greeting="Hi")