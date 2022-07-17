# Ініцілізовано функцію, напишіть в тілі функції логіку яка
# перетворить вхідну строчку за певною логікою.

# Функція приймає на вхід будь яку строчку і виводить в консоль за допомогою функції print()
#  оновлену версію цієї строчки.
# Якщо довжина строчки більша ніж 5 символів -> Потрібно вивести лише перші 5 символів та в кінці додати три точки (...).
# Якщо перша літера строчки U або u (регістр не важливий) -> Вивести всю строчку в Upper Case (верхній регістр)
# Якщо перша літера строчки L або l (регістр не важливий) -> Вивести всю строчку в Lower Case (нижній регістр)
# Якщо жодна умова вище не підходить - вивести строку без змін.
# Декілька умов можуть пересікатись!
# Можна додавати свої тести за прикладом. Потрібно врахувати обробку можливих помилок.

# Наприклад:
#   transformStr('Testing string') - > 'Testi...' (довжина більше 5 символів)
#   transformStr('Lux') - > 'lux' (Починается на L)
#   transformStr('up') - > 'UP' (Починается на U)
#   transformStr('Luxery') - > 'luxer...' (Починается на L + довжина більше 5 символів)

x = "uelM"
if len(x) > 5:
        print(x[:5])
elif x[0]=="U" or x[0]=="u":
        print(x.upper())
elif x[0]=="l" or x[0]=="L":
        print(x.lower())
elif x[0]==["a-t","x-z", "L"] and len(x) > 5:
        print(x[:5], x.lower())
else:
        print(x)

# transformStr('Testing string') # 'Testi...' (довжина більше 5 символів)
# transformStr('Lux') # 'lux' (Починается на L)
# transformStr('up') # 'UP' (Починается на U)
# transformStr('Luxery') # 'luxer...' (Починается на L + довжина більше 5 символів)


# b = "Hello Amazing World!"
#
# # Get the characters from position
# # n 2 to position 5 (not included):
# print(b[2:5])
#
# # Get the characters from the start to position 5 (not included):
# print(b[:5])
#
# # Get the characters from position 2, and all the way to the end:
# print(b[2:])
#
# print(b[-5:-2])
#
# # upper lower
# print('upperCase', b.upper())
# print('lowerCase', b.lower())
