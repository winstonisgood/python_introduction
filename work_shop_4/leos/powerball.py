import random

def picknumbers(poolsize, ballnum):
    pool=list(range(1,poolsize+1))
    i=1 
    pickedball=[]
    while i <= ballnum:
        random.shuffle(pool)
        last_num=pool.pop()
        pickedball.append(last_num)
        i+=1
    return(pickedball)

print(picknumbers(35,7),picknumbers(20,1))



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
       



