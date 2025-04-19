#Import the libraries
import pgzrun
from random import randint
from time import time

#Resize the screen
WIDTH= 500
HEIGHT= 500

#creating our elements and variables
Fox = Actor("fox")
Fox.pos = 250,250
Coin = Actor("coin")
Coin.x = randint(0, WIDTH)
Coin.y = randint(0, HEIGHT)
score=0
start_time = 0
total_time= 10
time_left = total_time


#drawing on the screen
def draw():
	screen.fill("lightblue")
	screen.draw.text("Score:" + str(score), color = "black", topleft=(10,10))
	screen.draw.text("Time left:" + str(round(time_left,1)), color = "black", topleft=(10,30))
	
	Fox.draw()
	Coin.draw()

	if time_left<=0:
		screen.fill("black")
		screen.draw.text("GAME OVER", color="white", centery=30, centerx=WIDTH//2)
		screen.draw.text("Score: " + str(score), color="white", centery=50, centerx=WIDTH//2)
		screen.draw.text("Press R to restart " , color="white", centery=70, centerx=WIDTH//2)


#Moving the fox using the keyboard
def update():
	global score,time_left,start_time

	time_passed = time()-start_time
	time_left = total_time - time_passed

	if keyboard.left:
		Fox.x = Fox.x -5
	elif keyboard.right:
		Fox.x = Fox.x+5
	elif keyboard.up:
		Fox.y = Fox.y -5
	elif keyboard.down:
		Fox.y = Fox.y +5

	# Keep fox on screen
	Fox.x = max(20,min(WIDTH-20,Fox.x))
	Fox.y = max(30,min(HEIGHT-30,Fox.y))
        
	#Checking for collision
	if Fox.colliderect(Coin):
		score = score+10
		Coin.x = randint(0, WIDTH)
		Coin.y = randint(0, HEIGHT)
		reset_time()

	
		

#reset time
def reset_time():
	global start_time, time_left
	start_time=time()
	time_left=total_time

def on_key_down(key):
	global Coin, score
	
	if key ==keys.R:
		score=0
		reset_time()
		Coin.x = randint(0, WIDTH)
		Coin.y = randint(0, HEIGHT)


#Run the game
reset_time()
pgzrun.go()