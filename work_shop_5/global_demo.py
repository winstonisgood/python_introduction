def foo():
    global x
    x = 20
    print(f'x inside function: {x}')

foo()
print(f'x outside function: {x}')