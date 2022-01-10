def max_odd(array):
    max = 0
    for i in range(len(array)):
        if isinstance(array[i], str):
            continue
        elif isinstance(array[i], (int, float)):
            if array[i] % 2 != 0 and array[i] > max:
                max = array[i]
    if max == 0:
        return None
    else:
        return int(max)


print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))
