# GETTING A NUMBER
number =  int(input("please enter a number: "))

# CHECKING WHAT WE WANT BY FOR LOOP
for i in range(0 , number):
    if i % 2 == 0 :
        print(i)
        i += 1
    else:
        i += 1