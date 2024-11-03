import random

def pick_numbers(pool_size, ball_num):
    return random.sample(range(1, pool_size + 1), ball_num)

winning_numbers = pick_numbers(35, 7)
power_ball = pick_numbers(20, 1) 

print(f'the winning numbers are: {winning_numbers}')
print(f'the power ball is {power_ball}')