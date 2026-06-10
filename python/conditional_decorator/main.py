def conditional_run(should_run):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if should_run:
                result = func(*args, **kwargs)
                return result
            else:
                return None
        return wrapper
    return decorator

@conditional_run(True)
def greet(name):
    return f"Hello, {name}!"

@conditional_run(False)
def farewell(name):
    return f"Goodbye, {name}!"

greeting = greet("Alice")
print(greeting)
farewell_message = farewell("Bob")
print(farewell_message)