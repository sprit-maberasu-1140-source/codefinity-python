def is_positive(n):
    return n > 0

def filter_positive(numbers):
    return list(filter(is_positive, numbers))

numbers = [-1, 3, 8, 0, -10]
print(filter_positive(numbers))