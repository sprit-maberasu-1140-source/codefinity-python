def process_numbers(numbers):
    def square_and_add_five(x):
        return x ** 2 + 5
    result = []
    for num in numbers:
        processed = square_and_add_five(num)
        result.append(processed)
    return result

output = process_numbers([1, 2, 3])
print(output)
