input_str="python is best programming language"
for i in range(len(input_str)):
    end_value = '-'

    if input_str[i] == ' ' or i == len(input_str)-1 or input_str[i+1] == ' ':
        end_value = ''

    if i%2 == 0:
        print(input_str[i].upper(), end=end_value)
    else:
        print(input_str[i].lower(), end=end_value)
print()


'''st = 'python programming hello world'
for i in range(len(st)):
    end_value = '-'

    if st[i] == ' ' or i == len(st)-1 or st[i+1] == ' ':
        end_value = ''

    if i%2 == 0:
        print(st[i].upper(), end=end_value)
    else:
        print(st[i].lower(), end=end_value)
print()'''
