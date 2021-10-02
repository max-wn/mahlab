inp1 = int(input())
inp2 = int(input())
inp3 = int(input())

if inp1 == inp2 or inp1 == inp3 or inp2 == inp3:
    if inp1 == inp2 == inp3:
        print(3)
    else:
        print(2)
else:
    print(0)
