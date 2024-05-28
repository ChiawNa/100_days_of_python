#Reeborg has entered a hurdles race. Make him run the course, following the path shown.
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def all():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    all()


# Reeborg has entered a hurdle race, but he does not know in advance how long the race is. 
# Make him run the course, following a path similar to the one shown, but stopping at the only flag that will be shown after the race has started.
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json#

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def all():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:
    all()


# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position and number of hurdles changes each time this world is reloaded.
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def all():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:
    if wall_in_front():
        all()
    else:
        move()


# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position, the height and the number of hurdles changes each time this world is reloaded.
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def all():
    turn_left()
    
    while wall_on_right():
        move()
  
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()

    turn_left()

while at_goal() != True:
    if wall_in_front():
        all()
    else:
        move()


# Reeborg was exploring a dark maze and the battery in its flashlight ran out.
# Write a program using an if/elif/else statement so Reeborg can find the exit. 
# The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() != True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()