def start_game():
    print("you find yourself in a dark forest. There are two paths ahead.")
    choose_path()

def choose_path():
    choice = input("do you go left or right? (left/right): ").lower()

    if choice == "left":
        go_left()
    elif choice == "right":
        go_right()
    else:
        print("invalid choice. Please enter 'left' or 'right'.")
        choose_path()

def go_left():
    print("you chose the left path and encounter a river.")
    choice = input("do you swim or try to find a bridge? (swim/bridge): ").lower()

    if choice == "swim":
        print("you swim across the river but lose your way. Game Over.")
    elif choice == "bridge":
        print("the bridge broke on you and to drowned to death.")
        
    else:
       print("invalid choice. Please enter 'swim' or 'bridge'.")
       go_left()


def go_right():
    print("you chose the right path and find a cave.")
    choice = input("do you enter the cave or go around it? (enter/around): ").lower()
    
    if choice == "enter":
        print("you enter the cave and find treasure! You win!")
    elif choice == "around":
        print("you go around the cave and encounter a monster. Game Over.")
    else:
        print("invalid choice. Please enter 'enter' or 'around'.")
        go_right()

start_game()