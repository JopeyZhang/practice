# -*- coding:utf-8 -*-


str1 = 'hello,everyone.my name is xz,i am learning Python now.the weather is good today.'

# find()
print(str1.find("xz"))

# replace()
str1 = str1.replace('xz', 'xzz')
print(str1)


str2 = "2021-3-7 15:25:44"

# split()
str2 = str2.split(' ')
print(str2)

str3 = str2[0].split('-')  # ignore line17; str3 = str2.split(' ')[0].split('-')
print(str3)

str4 = str2[1].split(':')
print(str4)

# strip()
str5 = '   xz is good   '
str5 = str5.strip()
print(str5)

# lower()
str5 = str5.upper()
print(str5)

# upper()
str6 = str5.lower()
print(str6)

# startswith()
print(str6.startswith('x'))

# endswith()
print(str6.endswith('od'))




