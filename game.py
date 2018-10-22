import player, room, os
def GameControl():
        os.system("cls")
        player = CreatePlayer()
        current_room = roomStart()
        os.system("cls")
        menu(current_room)

def CreatePlayer():
        name = input("Please enter your name: ")
        gender = input("Please pick your Gender Male, Female or Other: ")
        if gender.upper() == ("MALE" or "BOY"):
                gender = 1
        elif gender.upper() == ("FEMALE" or "GIRL"):
                gender = 2
        else:
                gender = 3
        return player.player(name,gender)

def roomStart():
        return room.room("the royal kitchen","you are a lowly servant to the Royal Family of Orleasia.",0,0)

def menu(current_room):
        print(current_room.name.upper()+"\n\n"+current_room.description)

GameControl()
