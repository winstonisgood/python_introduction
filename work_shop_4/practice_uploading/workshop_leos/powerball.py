import random

def pick_numbers(pool_size, ball_num):
    pool = list(range(1, pool_size + 1))
    i = 1 
    picked_ball = []
    while i <= ball_num:
        random.shuffle(pool)
        print(pool)
        last_num = pool.pop()
        picked_ball.append(last_num)
        i += 1
    return(picked_ball)

print(pick_numbers(35, 7), pick_numbers(20, 1))



# while True:
#     poolsize_value=input('Please input the number of poolsize: ')
#     if poolsize_value.isdigit:
#        poolsize_num=int(poolsize_value)
#        break
#     else:
#        print('Please input a integer ')

# while True:
#     ball_value=input('Please input the number of balls: ')
#     if ball_value.isdigit and int(ball_value)<=int(poolsize_num):
#        ball_num=int(ball_value)
#        break
#     else:
#        print('Please input a integer less than poolsize')
       



