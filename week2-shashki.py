x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if y1 < y2:  # Движение вверх по полю
#  проверка диагонали
    if (x1 == y1 and x2 == y2) or (abs(x2-x1) == abs(y2-y1)):
        print('YES')
    elif (x2 - x1) % 2 == 0 and (y2 - y1) % 2 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
