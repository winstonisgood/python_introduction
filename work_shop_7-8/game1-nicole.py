import pgzrun

# Game variables
game_paused = False
game_over = False
score = 0
obstacles = []
obstacle_timeout = 0
OBSTACLE_SPAWN_TIME = 100  # Adjusted constant for obstacle spawning

# Player character setup
p3 = Actor('p3_stand')
p3.images = ['p3_walk01', 'p3_walk02', 'p3_walk03', 'p3_walk04', 'p3_walk05', 'p3_walk06', 'p3_walk07', 'p3_walk08', 'p3_walk09', 'p3_walk10']
p3.imageindex = 0
p3.velocity_y = 0
p3.pos = (60, 400)
gravity = 0.7

# Sounds
jump_sound = sounds.jump
point_sound = sounds.point
die_sound = sounds.die

def draw():
    global game_over
    screen.draw.filled_rect(Rect(0, 0, 800, 400), (163, 232, 254))  # Sky
    screen.draw.filled_rect(Rect(0, 400, 800, 200), (88, 242, 152))  # Ground
    p3.draw()

    if game_over:
        # Display game over message and score
        screen.draw.text("Game Over!", center=(400, 270), color="white", fontsize=60)
        screen.draw.text(f"Score: {score}", center=(400, 330), color="white", fontsize=60)
    else:
        # Draw all active obstacles
        for actor in obstacles:
            actor.draw()

    # Draw score during gameplay
    screen.draw.text(f"Score: {score}", (20, 20), color="black", fontsize=36)

def update():
    global score, game_paused, game_over, obstacle_timeout

    # Don't update game if paused or over
    if game_paused or game_over:
        return

    # Update player animation
    p3.image = p3.images[p3.imageindex]
    p3.imageindex = (p3.imageindex + 1) % len(p3.images)

    # Check for jump input
    if keyboard.space and p3.y == 400:  # Allow jumping only when on the ground
        p3.velocity_y = -20
        jump_sound.play() 
        
    # Update player position and apply gravity
    p3.y += p3.velocity_y
    p3.velocity_y += gravity
    if p3.y > 400:
        p3.y = 400
        p3.velocity_y = 0

    # Increment obstacle timeout and spawn new obstacles
    obstacle_timeout += 1
    if obstacle_timeout > OBSTACLE_SPAWN_TIME:
        new_obstacle = Actor('cactus')
        new_obstacle.pos = (850, 400)
        obstacles.append(new_obstacle)
        obstacle_timeout = 0
        

    # Update and check collisions for obstacles
    for obstacle in obstacles:  # Use a copy to allow safe removal
        obstacle.x -= 4  # Move obstacle leftward
        if p3.colliderect(obstacle):
            game_over = True
            die_sound.play()
            return

        # Remove obstacles that are off the screen
        if obstacle.x < -50:
            obstacles.remove(obstacle)
            score += 1  
            point_sound.play() 
            
pgzrun.go()  
