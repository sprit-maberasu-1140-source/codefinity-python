def unpack_first_last(lst):
    first1, first2, *_, last2, last1 = lst
    result = (first1, first2, last2, last1)
    return result


res1 = unpack_first_last([1, 2, 3, 4, 5, 6])
print(res1)
res2 = unpack_first_last(['a', 'b', 'c', 'd'])
print(res2)
res3 = unpack_first_last([10, 20, 30, 40, 50])
print(res3)