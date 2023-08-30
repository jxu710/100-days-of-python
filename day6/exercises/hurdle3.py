# This is my solution for the Hurdle 3 challenge at Reeborg's World:  https://reeborg.ca/index_en.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
       jump()
    else:
        move()
    