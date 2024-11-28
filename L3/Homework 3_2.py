#Приклади:
#[12, 3, 4, 10] => [10, 12, 3, 4]
#[1] => [1]
#[] => []
#[12, 3, 4, 10, 8] => [8, 12, 3, 4, 10


lst = list([12, 3, 4, 10])
print (lst)

if len(lst) > 0 :
    lst.insert(0, lst.pop())
    print (lst)
else :
    print (lst)