def isdigit(number):
    try:
        float(number)
        return True
    except:
        return False

def get_valid_number():
    input_value = ''
    isdecimal = False
    while not isdecimal:
        input_value = input("please enter a number:")
        isdecimal = isdigit(input_value)
        if isdecimal:
            return float(input_value)
        else:
            print('The text you entered is not a number!')

isdecimal = False
total_number = 0
while not isdecimal:
    input_value = input("Please enter how many numbers you are going to enter: ")
    isdecimal = input_value.isdecimal()
    if isdecimal:
        total_number = int(input_value)
    else:
        print('The text you entered is not a number!')

if (total_number > 0):
    numbers = []
    for i in range(total_number):
        numbers.append(get_valid_number())
    print(numbers)
    print(f'The max number is {max(numbers)} and position at {numbers.index(max(numbers))}')
    print(f'The min number is {min(numbers)} and position at {numbers.index(min(numbers))}')
    print(f'The total is {sum(numbers)}')
    print(f'The average number is {sum(numbers) / len(numbers)}')

    


