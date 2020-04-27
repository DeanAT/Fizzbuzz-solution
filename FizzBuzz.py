#Fizzbuzz

fizzbuzz = range(1,101)

for i in fizzbuzz:
    if i % 3 == 0 and i % 5 == 0:
        i = "Fizzbuzz"
    elif i % 3 == 0:
        i = "Fizz"
    elif i % 5 == 0:
        i = "Buzz"
    print(i)
    