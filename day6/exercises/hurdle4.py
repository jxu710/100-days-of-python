# my solution for the Hurdle 4


def turn_right():
  turn_left()
  turn_left()
  turn_left()


def jump():
  turn_left()
  while wall_on_right() and is_facing_north():
    move()
  while right_is_clear():
    turn_right()
    move()


while not at_goal():
  if wall_in_front():
    jump()
  else:
    move()

# Another student's answer that is shorter


def turn_right():
  turn_left()
  turn_left()
  turn_left()


while not at_goal():  
  if front_is_clear():
    move()
    if right_is_clear():
      turn_right()
  elif wall_in_front():
    turn_left()
