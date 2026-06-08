def filter_long_strings(strings):
    return list(filter(lambda s: len(s) > 3, strings))

result1 = filter_long_strings(["cat", "house", "sun", "elephant"])
print(result1)
result2 = filter_long_strings(["dog", "tree", "sky", "river"])
print(result2)
result3 = filter_long_strings(["a", "be", "see", "deer"])
print(result3)