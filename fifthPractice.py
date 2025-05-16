# GETTING A NUMBER
number =  int(input("please enter a number: "))

# CHECKING WHAT WE WANT BY FOR LOOP
for i in range(2 , number):

    # CREATE A FLAG
    flag = False
    
    # PRIME OR NOT
    for j in range(2 , i):
        if i % j == 0 :
            flag = True
            break
    if not flag:
        print(i)