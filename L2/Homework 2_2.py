y = int(input("Please input 5-digit number: "))

print(y)

x = y % 10
x = x*10 + y//10 % 10
x = x*10 + y//100 % 10
x = x*10 + y//1000 % 10
x = x*10 + y//10000 % 10

print(x)