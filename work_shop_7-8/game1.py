import pgzrun
import random

# player setup
p3 = Actor('p3_stand')
p3.images = ['p3_walk01', 'p3_walk02', 'p3_walk03', 'p3_walk04', 'p3_walk05', 'p3_walk06', 'p3_walk07', 'p3_walk08', 'p3_walk09', 'p3_walk10']
p3.imageindex = 0
p3.velocity_y = 0
p3.pos = (60, 400)
gravity = 1

# obstacles setup
obstacles = []
obstacles_timeout = 50

# score setup
score = 0

# game over setup
game_over = False

def draw():

    if game_over:
        screen.draw.text("Game Over", center=(400, 200), color="red", fontname="bauhs93", fontsize=30)
        screen.draw.text(f"Score: {score}", center=(400, 240), color="white", fontname="bauhs93", fontsize=25)
    else:
        screen.draw.filled_rect((Rect(0, 0, 800, 400)), (163, 232, 254))
        screen.draw.filled_rect(Rect(0, 400, 800, 200), (88, 242, 152))
        p3.draw()
        for obstacle in obstacles:
            obstacle.draw()


def update():
    # any global variable need to be updated need specify global
    global obstacles_timeout, score, game_over

    if game_over:
        return

    p3.image = p3.images[p3.imageindex]
    p3.imageindex += 1
    if p3.imageindex >= len(p3.images):
        p3.imageindex = 0
    if keyboard.space:
        sounds.jump.play()
        p3.velocity_y = -20
    
    p3.y += p3.velocity_y
    p3.velocity_y += gravity
    if p3.y > 400:
        p3.y = 400
        p3.velocity_y = 0

    obstacles_timeout -= 1
    if obstacles_timeout < 0:
        obstacle = Actor('cactus')
        # obstacle.pos = (850, 400)
        # x position >= width of screen + width of obstacle
        obstacle.x = 850
        obstacle.y = 400
        obstacles.append(obstacle)
        # reset timeout in random
        obstacles_timeout = random.randint(25, 75)
    
    # obstacles move to the left
    for obstacle in obstacles:
        obstacle.x -= 5
        if obstacle.x < -50 and not game_over:
            sounds.point.play()
            obstacles.remove(obstacle)
            score += 1
            print(f'Score: {score}')
    
    # check collision
    # check the collision between player and obstacles, if collide, collision index will be returned
    # if not collide, -1 will be returned
    if p3.collidelist(obstacles) != -1:
        game_over = True
        sounds.die.play()
        print('Game Over')

pgzrun.go() # Must be last line


# set obstacles
# check collision
# score