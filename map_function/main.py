def apply_function_to_list(func, items):
    return [func(item) for item in items]

def double(x):
    return x * 2

def uppercase(s):
    return s.upper()

doubled = apply_function_to_list(double, [1, 2, 3, 4])
print(doubled)

uppercased = apply_function_to_list(uppercase, ["hello", "world"])
print(uppercased)
