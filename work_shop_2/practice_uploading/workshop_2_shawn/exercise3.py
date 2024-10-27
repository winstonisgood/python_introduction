user_input = input('Please enter how many numbers you going to enter: ')

while not user_input.isdecimal():
    print('The text you entered is not a number! ')
    user_input = input('Please enter how many numbers you going to enter:')

numbers_count = int(user_input)
numbers = []
for i in range(numbers_count):
    while True:
        try:
            number = float(input('Please enter a number: '))
            numbers.append(number)
            break
        except ValueError:
            print('The text you entered is illegal!')

max_number = numbers[0]
min_number = numbers[0]
max_index = [0]
min_index = [0]
for i in range(1, len(numbers)):
    if numbers[i] > max_number:
        max_number = numbers[i]
        max_index = [i]
    elif numbers[i] == max_number:
        max_index.append(i)
    if numbers[i] < min_number:
        min_number = numbers[i]
        min_index = [i]
    elif numbers[i] == min_number:
        min_index.append(i)

average = sum(numbers) / len(numbers)
total_value = sum(numbers)
print(f'The max number is {max_number} and position at {max_index}')
print(f'The min number is {min_number} and position at {min_index}')
print(f'The total is {total_value}')
print(f'The average is {average}')




# max_number = max(numbers)
# min_number= min(numbers)
# print(f'The max number is {max_number}')
# print(f'The min number is {min_number}')