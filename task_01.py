def is_palindrome(string):
    string = str(string)
    pal = True
    j = 1
    string = ''.join(filter(str.isalnum, string)).lower()
    for i in range(len(string) // 2):
        if string[i] != string[-j]:
            pal = False
            return pal
            break
        elif string[i] == string[-j]:
            pal = True
            j += 1
    return pal


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))
