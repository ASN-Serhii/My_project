#Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення
# - якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.

choice = "y"

while choice == "y" :
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
    choice = input("\nБажаєте продовжити (y/n)? - ")
