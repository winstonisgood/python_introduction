def f (a, b, c = 3):
    print(f'this is c: {c}')
    return a * b

print(f(1, 2, 4))
print(f(1, 2))

#f(1, 2, 3, 4)

def b(a=1, b=2, c=3):
    return a*b*c
b()