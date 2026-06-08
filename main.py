def sum_of_squares_of_evens(numbers):
    evens = filter(lambda x: x % 2 == 0, numbers)
    squares = map(lambda x: x ** 2, evens)
    result = sum(squares)
    return result


result1 = sum_of_squares_of_evens([1, 2, 3, 4, 5, 6])
print(result1)
result2 = sum_of_squares_of_evens([7, 9, 11])
print(result2)
result3 = sum_of_squares_of_evens([0, -2, -4])
print(result3)
result4 = sum_of_squares_of_evens([])
print(result4)