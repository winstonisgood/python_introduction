import pgzrun

p3 = Actor('p3_stand')
p3.images = ['p3_walk01', 'p3_walk02', 'p3_walk03', 'p3_walk04', 'p3_walk05', 'p3_walk06', 'p3_walk07', 'p3_walk08', 'p3_walk09', 'p3_walk10']
p3.imageindex = 0
p3.velocity_y = 0
p3.pos = (60, 400)
gravity = 1

obstacle = Actor('cactus')

def draw():
    screen.draw.filled_rect((Rect(0, 0, 800, 400)), (163, 232, 254))
    screen.draw.filled_rect(Rect(0, 400, 800, 200), (88, 242, 152))
    p3.draw()
    print(2)

def update():
    p3.image = p3.images[p3.imageindex]
    p3.imageindex += 1
    if p3.imageindex >= len(p3.images):
        p3.imageindex = 0
    # p3.velocity_y = -20
    # print(1)

    if keyboard.space:
        p3.velocity_y = -20
    
    p3.y += p3.velocity_y
    p3.velocity_y += gravity
    if p3.y > 400:
        p3.y = 400
        p3.velocity_y = 0

pgzrun.go() # Must be last line

# set obstacles
# check collision
# score