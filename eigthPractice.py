# GETTING NUMBERS
number1 = int(input("please enter first number: "))
number2 = int(input("please enter second number: "))
evenOrOdd = input("even or odd? ")

# CHECKING WHAT WE WANT
if number1 > number2 :
    if evenOrOdd == "even":
        for i in range(number2 + 1 , number1):
            if i % 2 == 0 :
                print(i)
                i += 1
            else:
                i += 1
    elif evenOrOdd == "odd" :
        for i in range(number2 + 1 , number1):
            if not i % 2 == 0:
                print(i)
                i += 1
            else:
                i += 1
    else:
        print("please enter even or odd!")
else:
    if evenOrOdd == "even":
        for i in range(number1 + 1 , number2):
            if i % 2 == 0 :
                print(i)
                i += 1
            else:
                i += 1
    elif evenOrOdd == "odd" :
        for i in range(number1 + 1 , number2):
            if not i % 2 == 0:
                print(i)
                i += 1
            else:
                i += 1
    else:
        print("please enter even or odd!")

