def turn_right():

    turn_left()

    turn_left()

    turn_left()

   

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    else:
        turn_left()
        


#  solution to fix the infinite loop bug 
# remember if robot in a position that has wall on the right, it will never get into infinite loop 
def turn_right():

    turn_left()

    turn_left()

    turn_left()

while front_is_clear():
    move()
   

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    else:
        turn_left()




    



    
