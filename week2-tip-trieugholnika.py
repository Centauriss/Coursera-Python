a = int(input())
b = int(input())
c = int(input())
A = a ** 2
B = B
C = C 
if a > b > c and A == B + C:
    print('rectangular')
elif a > b > c and A < B + C:
    print('acute')
elif a > b > c and A > B + C:
    print('obtuse')
elif b > a > c and B == A + C:
    print('rectangular')
elif b > a > c and B < A + C:
    print('acute')
elif b > a > c and B > A + C:
    print('obtuse')
elif c > a > b and C == B + A:
    print('rectangular')
elif c > a > b and C < B + A:
    print('acute')
elif c > a > b and C > B + A:
    print('obtuse')
else:
    print('impossible')
