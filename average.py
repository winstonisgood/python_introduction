user_input = input('Please enter how many numbers you going to enter: ')

while not user_input.isdecimal():
    print('The text you entered is not legal! ')
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
average = sum(numbers) / len(numbers)
print(f'The average is: {average}')