def merge_dicts(dict1, dict2):
    merged = {**dict1, **dict2}
    return merged


result1 = merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
print(result1)
result2 = merge_dicts({}, {'x': 10})
print(result2)
result3 = merge_dicts({'foo': 9}, {})
print(result3)