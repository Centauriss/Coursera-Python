N = 36
x = int(input())
y = int(input())
if (x < y) and (x == 1 or x % N == 1) and (y == N or y % N == 0):
    print('YES')
else:
    print('NO')
