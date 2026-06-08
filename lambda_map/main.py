cube = lambda x: x ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(cube, numbers))

result = cubed_numbers
print(result)