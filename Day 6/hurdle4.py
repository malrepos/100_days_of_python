def turn_right():
    turn_left()
    turn_left()
    turn_left()


while at_goal() is False:
    if not wall_on_right():
        turn_right()
        move()
        turn_right()
        move()
        if front_is_clear():
            move()
        else:
            turn_left()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
    



