# Напишіть функцію sumNum що задовільняє наступній умові:

# Дано ціле число num, 
# декілька кілька разів додайте всі його цифри, 
# доки в результаті не буде лише одна цифра, і поверніть її.

# Приклад 1
# sumNum(40) -> 4

# Для числа 40 потріботно повернути 4, чому?
# 1. 40 - розкладаємо на цифри -> 4, 0
# 2. Складаємо цифри 4 + 0 = 4
# 3. 4 - це одна цифра, повертаємо її

# Приклад 2
# sumNum(48) -> 3

# Для числа 48 потріботно повернути 3, чому?
# 1. 48 - розкладаємо на цифри -> 4, 8
# 2. Складаємо цифри 4 + 8 = 12
# 3. 12 - розкладаємо на цифри -> 1, 2
# 4. Складаємо цифри 1 + 2 = 3
# 5. 3 - це одна цифра, повертаємо її

# Приклад 3
# sumNum(2) -> 2

# Для числа 2 потріботно повернути 2, тому що число 2 складається з однієї цифри.

# num = 678
# num = set(x, y, z)
#
# def sum (num):
#     {sum = x + y + z
#     print(sum)
#     if len(sum) > 2
#     sum = (x + y)
#     else:
#     print(sum)
#     return sum }
# num = 6786
# def sum(num):
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     return sum
# print(sum(num))
# len(sum(num))
# def newsum(sum):
#     newsum = 0
#     print(newsum)
#     while newsum > 9:
#         newsum += sum % 10
#         sum //= 10
#     return newsum
# print(newsum(sum))



n=67459877
sum = list(map(int, str(n)))
print(sum(list(map(int, str(n))))

# n = 43564257346
# def sum_dig(m):
#     m = 0
#     while n > 9:
#         m = sum(map(int, str(n)))
#     return sum_dig
#     print(sum_dig)
# # num = 12345
# sum(map(int,str(12345)))
# sum
# def sumNum(num):
#     return num
#
# print(sumNum(38) == 2)
# print(sumNum(40) == 4)
# print(sumNum(48) == 3)
# print(sumNum(2) == 2)
