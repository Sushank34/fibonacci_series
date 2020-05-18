def fibonacci_sequence(num1):
    list1 = []
    if num1 == 0:
        list1 = list1
    elif num1 == 1:
        list1.append(0)
    elif num1 == 2:
        list1.extend([0, 1])
    else:
        list1.extend([0, 1])
        for i in range(2, num1):
            list1.append(list1[i - 2] + list1[i - 1])
    print(list1)

t=int(input())
while t>0:
    n=int(input())
    fibonacci_sequence(n)
    t=t-1
