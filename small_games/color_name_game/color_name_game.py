# import the modules
import tkinter
import random

# list of possible colour.
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']

score = 0

# the game time left, initially 30 seconds.
timeleft = 30
# function that will start the game.
def startGame(event):
    if timeleft == 30:
        # start the countdown timer.
        countdown()

        # run the function to
    # choose the next colour.
    nextColour()
# Function to choose and
# display the next colour.
def nextColour():
    # use the globally declared 'score'
    # and 'play' variables above.
    global score
    global timeleft
    # if a game is currently in play