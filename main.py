import pyautogui
from Pet_Constants import *
from time import sleep
from screen_search import *
from ItemSlot import ItemSlot

# flow of events
# scan the pet page and locate all the pieces to play
# record where each tile is
# everytime you click a pet with submenu i.e., Chicken; Adult, Babe
    # record the placement of each item



pet_homepage = {
    "Silverfish": "assets/clay_ball.png",
    "Cat": "assets/fish_cod_raw.png",
    "Chicken": "assets/egg.png",
    "Wolf": "assets/bone.png",
    "Bat": "assets/coal.png",
    "Rabbit": "assets/carrot.png",
    "Villager": "assets/emerald.png",
    "Zombie": "assets/rotten_flesh.png",
    "Little_Helper": "assets/little_helper.png",
    "Golem": "",
    "Enderman": "assets/ender_pearl.png",
    "Blaze": "",
    "Snowman": "assets/snowball.png",
    "Herobrine": "",
    "Endermite": "assets/ender_eye.png",
    "Mini_Wither": "",
    "Clone": "",
    "Minecart": "",
    "Grinch": "",
    "Spider": "assets/string.png",
    "Cow": "assets/beef_raw.png",
    "Creeper": "assets/gunpowder.png",
    "Horse": "assets/saddle.png",
    "Pig": "assets/porkchop_raw.png",
    "Sheep": "assets/mutton_raw.png",
    "Slime": "assets/slimeball.png",
    "Skeleton": "assets/bow_standby.png",
    "Squid": ""
}


def find_available_pets():
    pets_to_feed = {}
    # searching for the pet based on default icon images
    for pet in pet_homepage:

        if pet_homepage[pet] == "":
            print(f"Unknown imagine for pet: {pet}")

        else:
            search = Search(pet_homepage[pet])
            pos = search.imagesearch()

            if pos[0] != -1:
                print(f"Pet icon for pet '{pet}' was located")
                pets_to_feed[pet] = pos

            else:
                print(f"Could not find icon for pet '{pet}' | Reference image: location '{pet_homepage[pet]}")

    return pets_to_feed


def find_image():
    pass

def feed_pet():
    pass

def thirst_pet_quench():
    pass

def exercising_pet():
    pass


if __name__ == '__main__':

    #
    # search = Search("assets/bone.png")
    # x, y = search.imagesearch()
    #
    #
    # if x != -1:
    #     print(f"Found pet's menu at {x} {y}, initiating opening...")
    #     pyautogui.moveTo(x, y)
    #     pyautogui.click()
    #
    # else:
    #     print("image not found")

    print(len(find_available_pets()))


