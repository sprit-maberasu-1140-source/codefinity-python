pairs = [(1, 3), (2, 2), (4, 1)]

def get_second_element(pair):
    return pair[1]

sorted_pairs = sorted(pairs, key=get_second_element)
print(sorted_pairs)