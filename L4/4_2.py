#Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд],
#             потім перемножити цю суму на останній елемент вхідного масиву.
#Не забудьте, що перший елемент масиву має індекс 0.
#Для порожнього масиву результат завжди 0.
#Робити запит на введення даних від користувача не потрібно.
#[0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
#[1, 3, 5] => 30
#[6] => 36
#[] => 0

lst = [0, 1, 7, 2, 4, 8]
print("0") if len(lst) == 0 else print(sum(lst[::2]) * lst[-1])

#if len(lst) == 0:
#    print("0")
#else:
#    result = sum(lst[::2]) * lst[-1]
#    print(result)
