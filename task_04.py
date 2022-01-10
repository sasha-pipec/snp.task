def sort_list(list):
    if len(list) != 0:
        max1, min1 = max(list), min(list)
        for i in range(len(list)):
            if list[i] == max1:
                list[i] = min1
            elif list[i] == min1:
                list[i] = max1
        list.append(min1)
        return list
    else:
        return list


print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))
