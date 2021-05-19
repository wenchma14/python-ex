def char_frequency(str):
    dict = {}
    for i in str:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

print(char_frequency('www.google.com'))
