def connect_dicts(dict1, dict2):
    buf, buf1 = {}, {}
    res, ress = 0, 0
    ret = {}
    for key in dict1:
        res += int(dict1[key])
        if dict1[key] >= 10:
            buf[key] = dict1[key]
    for key in dict2:
        ress += int(dict2[key])
        if dict2[key] >= 10:
            buf1[key] = dict2[key]
    for i in buf:
        if i in buf1:
            if res > ress:
                ret[i] = buf[i]
            elif ress > res:
                ret[i] = buf1[i]
            else:
                ret[i] = buf1[i]
        else:
            ret[i] = buf[i]
    for i in buf1:
        if i not in ret:
            ret[i] = buf1[i]

    values = sorted(ret.values())
    resret = {}
    for i in values:
        for key in ret:
            if ret[key] == i:
                resret[key] = i

    return resret


print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))
