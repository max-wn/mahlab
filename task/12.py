r = int(input())
n = 1
a = ''
b = ''
c = ''
d = ''

for i in range(n, r+1):
    if i == r+1:
        a += '+___ '
        b += '|{} / '.format(i)
        c += '|__\\ '
        d += '| '
    else:
        a += '+___ '
        b += '|{} / '.format(i)
        c += '|__\\ '
        d += '|    '
print(a)
print(b)
print(c)
print(d)

