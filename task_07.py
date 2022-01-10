def combine_anagrams(words_array):
    ress = []
    for i in range(len(words_array)):
        aa = True
        for j in range(len(ress)):
            if len(words_array[i].lower()) == len(ress[j][0].lower()) and all(
                    words_array[i].lower().count(x) == ress[j][0].lower().count(x) for x in words_array[i].lower()):
                ress[j].append(words_array[i].lower())
                aa = False
            else:
                continue
        if (aa):
            ress.append([words_array[i].lower()])
    return ress


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
                        "creams", "scream"]))
