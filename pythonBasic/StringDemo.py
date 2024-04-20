# password = "abcdABA$"
# print(password.isalpha())
# strings are immutable
s = "ABCDE$%"
# print('s.isalpha', s.isalpha())
# print('s.isdigit', s.isdigit())
# print('s.islower', s.islower())
# print('s.isupper', s.isupper())


# print('s.lower', s.lower())
# print('s.upper', s.upper())

x = '    abc     '
print(x.lstrip()) #to remove left side space from string

# a = "abc"

# for my_char in a:
# 	print(my_char*2)

# b = 'def'

# # c = a+b

# c = a*3

# print(c)

# fruit = "Apple"

# # print(fruit[4])

# print(fruit[-2])

# my_char = fruit[2];
# print(my_char)


# name = """Srija
# Kumar
# Sharma"""
# paragraph = ''' This is a
# multiline
# String
# paragraph. This is for testing'''

# print(name)

#slicing
s = "abcde"
s[1:4] #bcd

s[1:5] #bcde

s[:4]#abcd it will start from index 0

s[1:]#bcde it will end at last letter by default

s[0:5:2] #ace

s[::-1] #edcba

s[0:5:-1]# ' ' gives blank result

s[-1:0:-1] #edcb

s[-1:0:-1]# '' gives blank result