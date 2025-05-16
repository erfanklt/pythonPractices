# GETTING A NUMBER
number = int(input("please enter a number: "))

# CHECKING WHAT WE WANT
for j in range(0 , number):
    if j % 2 == 0 :
        print(j)
        j += 1
    else:
        j += 1