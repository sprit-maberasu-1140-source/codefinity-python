import time
import functools

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        log_message = f"Calling function '{func.__name__}' with args={args}, kwargs={kwargs}"
        print(log_message)
        result = func(*args, **kwargs)
        return result
    return wrapper

def time_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        timing_message = f"Function '{func.__name__}' executed in {duration:.6f} seconds"
        print(timing_message)
        return result
    return wrapper

@time_execution
@log_calls
def multiply(a, b):
    product = a * b
    return product

result1 = multiply(5, 7)
print(result1)

result2 = multiply(2, 10)
print(result2)

