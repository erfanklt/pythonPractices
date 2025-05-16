# CREATE MAX AND SUM
sum = 0
max = None

for i in range(10000):
    num = float(input("please enter a number(if you want to stop enter 0): "))
    if num == 0 :
        break
    else :
        sum += num
        if max == None:
            max = num
        elif max > num :
            max = max
        elif max < num :
            max = num
        else:
            max = max
        i += 1
print("sum is: ")
print(sum)
print("max is: ")
print(max)