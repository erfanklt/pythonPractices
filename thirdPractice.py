# GETTUNG A NUMBER
number = int(input("please enter a number: "))

# CREATE A FLAG
flag = True

# CHECKING WHAT WE WANT BY FOR LOOP
for i in range(2 , number):
    if number % i == 0:
        flag = False
        i += 1
    else:
        i += 1 

# CHECKING THE FLAG
if flag :
    print("The number is prime!")
else:
    print("The number is composite!")