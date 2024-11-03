import random

def pick_numbers(pool_size, ball_num):
    #Create a list of numbers from 1 to defined poolsize
    numbers = list(range(1, pool_size + 1))
    #Shuffle
    random.shuffle(numbers)
    # return numbers[-ball_num:]
    print(numbers)
    #Initialize winning list
    winning_numbers = []
    #set a condition to pop the number from shuffled number list and append to winning_numbers
    while len(winning_numbers) < ball_num:
        winning_numbers.append(numbers.pop())

    return winning_numbers

winning_seven = pick_numbers(35, 7)
p_ball = pick_numbers(20,1)

print(f'the winning seven numbers are: {winning_seven}')
print(f'the P ball is {p_ball}')
