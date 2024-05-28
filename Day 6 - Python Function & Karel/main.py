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