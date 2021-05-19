filename = input('input a filename:')
f_exten = filename.split('.')
print('The extension of the file is:' + repr(f_exten[-1]))  # repr()将对象转化为string格式，输出的字符带有引号.
