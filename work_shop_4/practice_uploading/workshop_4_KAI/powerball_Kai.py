import random

def picknumbers(poolsize, ballnum):
    return random.sample(range(1, poolsize + 1), ballnum)

winning_numbers = picknumbers(35, 7)
power_ball = picknumbers(20, 1) 

print(f'the winning numbers are: {winning_numbers}')
print(f'the power ball is {power_ball}')