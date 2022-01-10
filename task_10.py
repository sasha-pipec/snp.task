def count_words(string):
    string = string.lower()
    buf = []
    buff = ""
    res = {}
    for i in range(len(string)):
        if string[i].isalpha():
            buff += string[i]
        elif string[i] == " ":
            buf.append(buff)
            buff = ''
        else:
            continue
    buf.append(buff)
    for i in range(len(buf)):
        if buf[i] not in res and buf[i] != "":
            res[buf[i]] = buf.count(buf[i])
        else:
            continue
    return res


print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))
