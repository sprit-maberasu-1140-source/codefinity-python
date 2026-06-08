def pack_to_tuple(a, b, c):
    return (a, b, c)

values = [10, 20, 30]
result = pack_to_tuple(*values)
print(result)