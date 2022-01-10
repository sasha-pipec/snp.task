def coincidence(list=[], range=(0, 0)):
    spisok = []
    for i in list:
        if isinstance(i, (int, float)):
            if i in range or i // 1 <= range[-1] and i // 1 >= range[0]:
                spisok.append(i)
    return spisok


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
