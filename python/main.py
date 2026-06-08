def sum_first_last(numbers):
    if len(numbers) == 1:
        return numbers[0] * 2
    else:
        first, *_, last = numbers
        return first + last


output1 = sum_first_last((1, 2, 3, 4, 5))
print(output1)
output2 = sum_first_last((10, 20))
print(output2)
output3 = sum_first_last((7,))
print(output3)