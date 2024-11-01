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

    # Find max and min value
    max_value = max(numbers)
    min_value = min(numbers)

    # Find max and min position
    max_positions = []
    min_positions = []
    for index in range(len(numbers)):
        if numbers[index] == max_value:
            max_positions.append(index)
        if numbers[index] == min_value:
            min_positions.append(index)

    max_position_result = ",".join(map(str, max_positions))
    min_position_result = ",".join(map(str, min_positions))


    print(numbers)
    print(f'The max number is {max(numbers)} and position at {max_position_result}')
    print(f'The min number is {min(numbers)} and position at {min_position_result}')
    print(f'The total is {sum(numbers)}')
    print(f'The average number is {sum(numbers) / len(numbers)}')






