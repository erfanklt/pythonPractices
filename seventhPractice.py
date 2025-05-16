# GETTING NUMBERS
number1 = int(input("please enter first number: "))
number2 = int(input("please enter second number: "))

# CHECKING WHAT WE WANT
if number1 > number2 :
    for i in range(1 , number2 + 1):
        if number2 % i == 0 and number1 % i == 0:
            print(i)
            i += 1
        else:
            i += 1
else:
    for i in range(1 , number1 + 1):
        if number1 % i == 0 and number2 % i == 0:
            print(i)
            i += 1
        else:
            i += 1