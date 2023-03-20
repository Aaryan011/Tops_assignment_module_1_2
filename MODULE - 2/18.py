# Write a Python program to add 'ing' at the end of a given string (length
# should be at least 3). If the given string already ends with 'ing' then add
# 'ly' instead if the string length of the given string is less than 3, leave it
# unchanged.

str1 = 'ending'

if str1.endswith('ing'):
    if len(str1) >=3:
        str1 = str1.replace('ing','ly')
        print('changed string', +str1)
    else:
        print('unchanged')
else:
    print('Doesnt contain ing in the end')