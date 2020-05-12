x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if y1 < y2:  # Движение вверх по полю
    if x1 == y1 and x2 == y2:  # Движение по диагоналям
        print('YES')
#   elif x1 == x2 and (y2 - y1 + 2) % 2 == 1:  # Движение по вертикальному краю
#       print('YES2')
#   elif (x2 - x1) % 2 == 0 and y1 == y2:
#      print('YES3')
    elif (x2 - x1) % 2 == 0 and (y2 - y1) % 2 == 0:
        print('YES')
    else:
        print('NO')
else:
    print("NO")
