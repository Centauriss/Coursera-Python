a, b, c = int(input()), int(input()), int(input()),
if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
elif c <= a <= b:
    print(c, a, b)
elif c <= b <= a:
    print(c, b, a)
else:
    print()
