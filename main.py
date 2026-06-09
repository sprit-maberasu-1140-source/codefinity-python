def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
result1 = times3(10)
print(result1)

times5 = make_multiplier(5)
result2 = times5(4)
print(result2)