#Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
#Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.
import random

#[1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
#[1, 1, 2, 1] == [1, 2, 2]
#[6, 3, 7] == [6, 7, 3]

lst = [random.randint(0, 100) for i in range(random.randint(3, 10))]
print(lst)
lst_new = lst[0], lst[2], lst[-2]
print(lst_new)