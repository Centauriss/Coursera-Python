a = int(input())
b = int(input())
c = int(input())
A = abs(a)
B = abs(b)
C = abs(c)
if A <= 10000 and B <= 1000 and C <= 1000:
    if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
        if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
