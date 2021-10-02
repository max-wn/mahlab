a = int(input())

if 99 < (a // 100) * (a % 100 // 10) * (a % 10) < 1000:
    print('YES')
else:
    print('NO')
