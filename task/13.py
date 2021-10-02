def printError():
    print("Error. Division by zero!")


n = int(input())
if n == 0:
    printError()
else:
    print(5//n)
