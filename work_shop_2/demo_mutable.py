# demo for the immutable function
def change_var(a, b):
    # non-global operation
    a = b
    print(f'a in the function: {a}')
    return a

# global
a = 1
b = 2
print(f'a in the first initial: {a}')
change_var(a, b)
print(f'a after function: {a}')

# demo for the mutable function
# global
a = [1,2,3]
b = 4

print(f'a in the first initial: {a}')
def add_var(a, b):
    # non-global operation
    a.append(b)
    print(f'a in the function: {a}')

add_var(a, b)
print(f'a after function: {a}')


# demo for the functional programming
# def equation(a , b , c):
#     return a * b + c

# 1 * 2 + 3
# 3 * 2 + 1

# equation(1, 2 ,3)
# equation(3, 2 ,1)


# a = (1,2,3)
# b = 4
