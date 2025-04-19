# Import Libraries
import pgzrun
from random import randint
from time import time

# Screen size
WIDTH = 500
HEIGHT = 500

# Create variables and elements
score = 0
car = Actor("sport-car-2")
car.pos = 100, 100
person= Actor("passanger")
person.pos = 200, 200

game_over = False
timer_active = False
start_time = 0
total_time=3
time_left = total_time  

# Draw
def draw():
    screen.fill("#fbc4ab")
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
    
    # Display timer if active
    if timer_active:
        #screen.draw.text(f"Time: {time_left:.1f}", color="black", topright=(WIDTH-10, 10))
        screen.draw.text("Time: "+ str(round(time_left,1)), color = "black", topright=(WIDTH-10, 10))
    car.draw()
    person.draw()

    if game_over:
        screen.fill("black")
        screen.draw.text("GAME OVER", color="white", centery=30, centerx=WIDTH//2)
        screen.draw.text("Score: " + str(score), color="white", centery=50, centerx=WIDTH//2)
        screen.draw.text("Press R to restart", color="white", centery=80, centerx=WIDTH//2)

# Update function
def update():
    global score, game_over, time_left, timer_active
    
    if not game_over:
        # Movements
        if keyboard.left:
            car.x = car.x - 5
        if keyboard.right:
            car.x = car.x + 5
        if keyboard.up:
            car.y = car.y - 5
        if keyboard.down:
            car.y = car.y + 5
        


        # Keep fox on screen
        car.x = max(50, min(WIDTH-50, car.x))
        car.y = max(20, min(HEIGHT-20, car.y))
        
        # Collision detection
        if car.colliderect(person):
            score += 10
            place_person()
            reset_timer()  

        # Update timer if active
        if timer_active:
            elapsed = time() - start_time
            time_left = max(0, total_time - elapsed)
            
            if time_left <= 0:
                game_over = True
                timer_active = False

def place_person():
    person.x = randint(20, WIDTH-20)
    person.y = randint(20, HEIGHT-20)

def reset_timer():
    global timer_active, start_time, time_left
    timer_active = True
    start_time = time()
    time_left = total_time

def on_key_down(key):
    global game_over, score
    
    if key == keys.R and game_over:
        # Reset game
        game_over = False
        score = 0
        place_person()
        reset_timer()
    
# Initialize game
place_person()
reset_timer()  
pgzrun.go()