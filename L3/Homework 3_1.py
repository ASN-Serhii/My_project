x = int(input("Перше число: "))
todo = input("Яка дія: ")
y = int(input("Друге число: "))

if todo == "/":
    if y == 0 :
        print("Не можна ділити на нуль!")
    else :
        print ("x / y = ", x/y)
elif todo == "+" :
    print ("x + y = ", x+y)
elif todo == "-" :
    print ("x - y = ", x-y)
elif todo == "*" :
    print ("x * y = ", x*y)
else :
    print ("wrong data")