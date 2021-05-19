def string_both_ends(str):
    if len(str) < 2:
        return ''
    else:
        return str[0:2] + str[-2:-1:]  # 字符串切片

print(string_both_ends('google'))
print(string_both_ends('go'))
print(string_both_ends('g'))
