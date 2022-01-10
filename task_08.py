def multiply_numbers(inputs=[]):
    inputs = str(inputs)
    buf = []
    res = 1
    for i in range(len(inputs)):
        if inputs[i].isdigit():
            buf.append(inputs[i])
        else:
            continue
    if len(buf) > 0:
        for i in range(len(buf)):
            res = res * int(buf[i])
        return res
    else:
        return None


print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))
