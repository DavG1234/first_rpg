def adventure():
    print("Welcome to the RPG Adventure!")
    print("You find yourself in a dark forest.")
    print("What would you like to do?")
    print("1. explore a cave")
    print("2. burn a castle")
    print("3. go to a village")
    player = 0
    while player != "3":
        player = input("enter number your choice ")
        if player == "3":
            print("you see a vendor.")
        elif player == "2":
            print("the castle colapsed on you and you died try again.")
        else:
            print("the cave colapsed on you and you died try again")
    print("You find yourself at the village gate and see a vendor.")
    print("What would you like to do?")
    print("1. smack him ")
    print("2. ask him for food ")
    print("3. steal his food ")
    player = 0
    while player != "2":
        player = input(" enter your number choice ")
        if player == "1":
            print("he smacks you into outer space and you die try again")
        elif player == "2":
            print(" he kindly gives you food thinking you are a pesant")
        elif player == "3":
            print("you steal his food and while running away you get run over by a police car and die try again")
        else:
            print("BAD")
    
    


 



adventure()
    