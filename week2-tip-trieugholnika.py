a = int(input())
b = int(input())
c = int(input())
A = a ** 2
B = b ** 2
C = c ** 2
if a > b and a > c and A == B + C:
    print('rectangular')
elif a > b and a > c and A < B + C:
    print('acute')
elif a > b and a > c and A > B + C:
    print('obtuse')
elif b > a and b > c and B == A + C:
    print('rectangular')
elif b > a and b > c and B < A + C:
    print('acute')
elif b > a and b > c and B > A + C:
    print('obtuse')
elif c > a and c > b and C == B + A:
    print('rectangular')
elif c > a and c > b and C < B + A:
    print('acute')
elif c > a and c > b and C > B + A:
    print('obtuse')
else:
    print('impossible')
