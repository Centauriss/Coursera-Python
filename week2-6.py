x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (abs(x1 - x2) % 2 == 0) and (abs(y1 - y2) % 2 == 0) or ((x1 == y1) and (x2 == y2)):
    print('YES')
else:
    print('NO')
