# Напишіть функцію commonStr що задовільняє наступній умові:



# Дано дві строчки, поверніть нову строчку 
# яка буде складатись виключно зі спільних символів перерадних строк.
# Якщо немає спільних символів - поверніть пусту строчку. 
# Ви можете повернути відповідь у будь-якому порядку.
# Символи не повині дублюватись у відповіді.

# Приклад 1
# commonStr('loli', 'luck') -> 'l'

# Приклад 1
# commonStr('good day', 'good morning') -> 'god'

# def commonStr(str1, str2):
#     str1 = 'loli'
#     str2 = 'luck'
#     str1.find(str1, ["Aa"],["Zz"])
#     return ''

str.index("loli", "lo", 0, 3)
print()



# print(commonStr('loli', 'luck') == 'l')
# print(commonStr('good day', 'good morning') == 'god')



# from collections import Counter
# a = "aabbcc"
# print(Counter(a))