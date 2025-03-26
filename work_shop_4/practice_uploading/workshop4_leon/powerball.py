import random as random



# def pick_numbers(poolsize:int,ballnum:int):
#     # create regular balls
#     regular_balls = set()
#     while len(regular_balls) < ballnum:
#         regular_ball = random.randint(1,poolsize)
#         regular_balls.add(regular_ball)
#
#     # create power ball
#     pball = random.randint(1,pball_number)
#
#     result = list(regular_balls)
#     random.shuffle(result)
#     # merge regular balls and power ball
#     result.append(pball)
#     return tuple(result)
#
# print(pick_numbers(20,7))



def pick_numbers2(pool_size: int,ball_num: int,powerball_number: int):
    # create pool for regular ball
    regular_pool = list(range(1, pool_size + 1))

    # select regular balls from pool
    selected_balls = []
    while len(selected_balls) < ball_num:
        index = random.randint(0, len(regular_pool) - 1)
        selected_ball = regular_pool.pop(index)
        selected_balls.append(selected_ball)

    # create power ball
    powerball = random.randint(1, powerball_number)

    # merge regular balls and power ball
    selected_balls.append(powerball)

    return tuple(selected_balls)

print(pick_numbers2(20,7,  20))


