h = int(input())
a = int(input())
b = int(input())

# h = 10
# a = 3
# b = 2
# x1 = 8


# h1 = (x * a + (-b * x)) * (a-b) + b
# h = xa^2 + xb^2 + b
# -xa^2 -xb^2 = -h +b
# -x(a^2 +b^2) = -h +b
# x = ((-h + b) / ((a-b) * (a+b)))*(-1)
# h1 = x*(a-b) + b
# x2 = int((h/(a-b)) - b)

# x = int(((h - a) % (a - b) + a - b - 1) % (a - b))

print(int((h - a - 1) // (a - b) + 2))
