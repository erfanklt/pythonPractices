# GETTING A NUMBER
number = int(input("please enter a number: "))

# CHECKING WHAT WE WANT BY FOR LOOP
for i in range(1 , number + 1):
    if number % i == 0:
        print(i)
        i += 1
    else:
        i += 1