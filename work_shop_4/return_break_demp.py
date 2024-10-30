def return_value():
    for i in range(5):
        if i == 3:
            return 3
    return 5

def break_value():
    for i in range(5):
        if i == 3:
            break
    return 5

print(return_value())
print(break_value())