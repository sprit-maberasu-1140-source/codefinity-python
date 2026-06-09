x = 10

def modify_variable():
    global x
    x = 20
    y = 5
    result = f"x is {x}, y is {y}"
    return result

output = modify_variable()
print(output)
print(x)
