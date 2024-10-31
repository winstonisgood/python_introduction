import random

def picknumbers(poolsize, ballnum):
    #Create a list of numbers from 1 to defined poolsize
    numbers = list(range(1, poolsize + 1))
    #Shuffle
    random.shuffle(numbers)
    #Initialize winning list
    winning_numbers = []
    #set a condition to pop the number from shuffled number list and append to winning_numbers
    while len(winning_numbers) < ballnum:
        winning_numbers.append(numbers.pop())

    return winning_numbers

winning_seven = picknumbers(35, 7)
p_ball = picknumbers(20,1)

print(f'the winning seven numbers are: {winning_seven}')
print(f'the P ball is {p_ball}')
