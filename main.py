import pyautogui
from Pet_Constants import *
from time import sleep
from screen_search import *

slot_location = {}
pet_menu = None
next_page = 50
collectibles = 49


# alternate plan
# instead of looking for each icon and storing the data, find the icon for bone
# and use that to guess where everything else is
# performance wise would probably be faster, should be easier to make since we only need
# the bone icon and gray dye icon

def find_available_pets(pet_group_img):
    """ When called will look through for all pet types and record the location"""

    pets_to_feed = {}
    # searching for the pet based on default icon images
    for pet in pet_group_img:

        if pet_group_img[pet] == "":
            print(f"Unknown image for pet: {pet}")

        else:
            icon_search = Search(pet_group_img[pet])
            pos = icon_search.imagesearch()

            if pos[0] != -1:
                print(f"Pet icon for pet '{pet}' was located")
                pets_to_feed[pet] = pos

            else:
                print(f"Could not find icon for pet '{pet}' | Reference image: location '{pet_group_img[pet]}")

    return pets_to_feed

def process_pet(pet, num_clicks):

    # feeding the pet
    pyautogui.moveTo(slot_location[food[pet.food]])
    for _ in range(num_clicks):
        pyautogui.click()

    # quenching pet's thirst
    pyautogui.moveTo(slot_location[food[pet.drink]])
    for _ in range(num_clicks):
        pyautogui.click()

    # exercising pet
    pyautogui.moveTo(slot_location[food[pet.exercise]])
    for _ in range(num_clicks):
        pyautogui.click()


    # returning to the collectibles menu
    pyautogui.moveTo(slot_location[collectibles])
    pyautogui.click()

    # returning to the pets menu
    pyautogui.moveTo(pet_menu)
    pyautogui.click()


if __name__ == '__main__':
    # locating pets menu icon position
    icon_search = Search("assets/bone.png")
    x, y = icon_search.imagesearch()

    pet_menu = (x, y)
    y -= 36
    index = 0

    # mapping each slot to a number
    for i in range(9):
        for j in range(6):
            slot_location[index] = (x + i * 36, y + j * 36)
            index += 1


    # opening pets menu
    pyautogui.moveTo(x, y)
    pyautogui.click()

    # get all pet groups
    available_pet_groups = find_available_pets(pet_homepage)

    # beginning the processing each pet
    for group in available_pet_groups:
        # grab all the pet types for a specific group
        pet_variants = pets[group]

        # click to be redirected to new menu with some random delay
        # would either go to feeding or into pet subgroup
        x, y = available_pet_groups[group]

        pyautogui.moveTo(x, y)
        pyautogui.click()

        for variant in pet_variants:
            s = pet_variants[variant]

            # check if we should click (if the pet exists), if not continue

            # else
            # going to the right page number
            for i in range(s.page - 1):
                pyautogui.moveTo(slot_location(next_page))
                pyautogui.click()
                # add random delay

            # opening the feeding page of the pet
            pyautogui.moveTo(slot_location(s.slot_num))
            pyautogui.click()

            # taking care of the pet
            process_pet(pet=variant, num_clicks=2)
