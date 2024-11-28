#[1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
#[1, 2, 3] => [[1, 2], [3]]
#[1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
#[1] => [[1], []]
#[] => [[], []]

lst = []
if not len(lst) % 2 :
    lst1 = [lst[:int(len(lst) / 2)], lst[int(len(lst) / 2):]]
    print (lst1)
elif len(lst) % 2 :
    lst1 = [lst[:int(len(lst) / 2 + 1)], lst[int(len(lst) / 2 + 1):]]
    print(lst1)
