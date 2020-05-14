a = int(input())
b = int(input())
c = int(input())
if a > b > c and a ** 2 == b ** 2 + c ** 2:
    print('rectangular')
elif a > b > c and a ** 2 < b ** 2 + c ** 2:
    print('acute')
elif a > b > c and a ** 2 > b ** 2 + c ** 2:
    print('obtuse')
elif b > a > c and b ** 2 == a ** 2 + c ** 2:
    print('rectangular')
elif b > a > c and b ** 2 < a ** 2 + c ** 2:
    print('acute')
elif b > a > c and b ** 2 > a ** 2 + c ** 2:
    print('obtuse')
elif c > a > b and c ** 2 == b ** 2 + a ** 2:
    print('rectangular')
elif c > a > b and c ** 2 < b ** 2 + a ** 2:
    print('acute')
elif c > a > b and c ** 2 > b ** 2 + a ** 2:
    print('obtuse')
else:
    print('impossible')
