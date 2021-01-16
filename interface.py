import time
import random
import tkinter
import pyautogui
from Pet_Constants import *
from screen_search import Search
from tkinter import font, messagebox


def isFloat(string):
    """ A replacement for .isnumeric() that works with floats and ints """
    try:
        float(string)
        return True
    except ValueError:
        return False


class Application(tkinter.Frame):
    def __init__(self, master=None, pet_group_img=None, food_maps=None):
        super().__init__(master)
        self.window_width = 305
        self.window_height = 450
        self.master = master
        self.master.iconbitmap('application_icon.ico')
        self.master.resizable(width=False, height=False)
        self.master.geometry(f'{self.window_width}x{self.window_height}')
        self.master.title("Hypixel AutoPetFeeder")

        self.tile_size = 36
        self.pet_group_img = pet_group_img
        self.food_maps = food_maps
        self.pets_to_feed = None
        self.slot_location = {}
        self.num_clicks = 2
        self.lower_interval = None
        self.upper_interval = None
        self.missing_pet_icon = Search("assets/gray_dye_selected.png", precision=0.95)
        self.book = Search("assets/book.png", precision=0.95)
        self.gold_pants = Search("assets/golden_leggings.png")
        self.boat = Search("assets/boat.png")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        myFont = font.Font(size=15)
        button_width = 25
        self.label_welcome = tkinter.Label(self, text="Status: IDLE", font=myFont)  # fg, bg, width, height
        self.label_welcome.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.btn_get_slot_pos = tkinter.Button(self,
                                               text="Generate Slot Position",
                                               command=self.gen_slot_positions,
                                               width=button_width,
                                               font=myFont, borderwidth=4)
        self.btn_get_slot_pos.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.btn_pet_icons = tkinter.Button(self,
                                            text="Scan For Pets",
                                            command=self.find_pets,
                                            width=button_width,
                                            font=myFont, borderwidth=4)
        self.btn_pet_icons.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.label_upper_interval = tkinter.Label(self, text="Upper Interval:", font=myFont)  # fg, bg, width, height
        self.label_upper_interval.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.entry_upper_interval = tkinter.Entry(self, bd=5)
        self.entry_upper_interval.grid(row=3, column=1)

        self.label_lower_interval = tkinter.Label(self, text="Lower Interval:", font=myFont)  # fg, bg, width, height
        self.label_lower_interval.grid(row=4, column=0, columnspan=1, padx=5, pady=5, sticky="w")

        self.entry_lower_interval = tkinter.Entry(self, bd=5)
        self.entry_lower_interval.grid(row=4, column=1)

        self.label_num_clicks = tkinter.Label(self, text="Number of Clicks:", font=myFont)  # fg, bg, width, height
        self.label_num_clicks.grid(row=5, column=0, columnspan=1, padx=5, pady=5, sticky="w")

        self.entry_num_clicks = tkinter.Entry(self, bd=5)
        self.entry_num_clicks.grid(row=5, column=1)

        self.btn_feed = tkinter.Button(self,
                                       text="Feed Pets",
                                       command=self.feed_pets,
                                       width=button_width,
                                       font=myFont,
                                       borderwidth=4)
        self.btn_feed.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.btn_help = tkinter.Button(self,
                                       text="HELP",
                                       command=self.help,
                                       width=button_width,
                                       font=myFont,
                                       borderwidth=4)
        self.btn_help.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.quit = tkinter.Button(self,
                                   text="QUIT",
                                   fg="red",
                                   command=self.master.destroy,
                                   width=button_width,
                                   font=myFont,
                                   borderwidth=4)
        self.quit.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        self.label_version = tkinter.Label(self, text="Tammon23 - v1.1.0")
        self.label_version.grid(row=9, column=1, sticky="e")

    def find_pets(self):
        """ When called will look through for all pet types and record the location"""
        self.label_welcome["text"] = "Status: SCANNING..."
        pets_to_feed = {}
        # searching for the pet based on default icon images
        for pet in self.pet_group_img:

            if self.pet_group_img[pet][0] == "":
                print(f"Unknown image for pet: {pet}")

            else:
                icon_search = Search(self.pet_group_img[pet][0])
                pos = icon_search.imagesearch()

                if pos[0] != -1:
                    print(f"Pet icon for pet '{pet}' was located")
                    pets_to_feed[pet] = self.pet_group_img[pet][1]

                else:
                    print(
                        f"Could not find icon for pet '{pet}' | Reference image: location '{self.pet_group_img[pet][0]}")

        self.pets_to_feed = pets_to_feed

        self.label_welcome["text"] = "Status: Found Pets"

    def feed_pets(self):
        """ When called will iterate through every pet and feed it """
        if self.pets_to_feed is None:
            error_message = 'Please preform a scan first!'
            messagebox.showerror(title="ERROR", message=error_message)
            return

        if len(self.pets_to_feed) == 0:
            error_message = 'No pets were found!'
            messagebox.showerror(title="ERROR", message=error_message)
            return

        num_clicks = self.entry_num_clicks.get()
        if len(num_clicks) != 0 and not num_clicks.isnumeric():
            error_message = 'Invalid number of clicks!'
            messagebox.showerror(title="ERROR", message=error_message)
            return

        upper_interval = self.entry_upper_interval.get()
        if len(upper_interval) != 0 and not isFloat(upper_interval):
            error_message = 'Invalid upper interval!'
            messagebox.showerror(title="ERROR", message=error_message)
            return

        lower_interval = self.entry_lower_interval.get()
        if len(lower_interval) != 0 and not isFloat(lower_interval):
            error_message = 'Invalid lower interval!'
            messagebox.showerror(title="ERROR", message=error_message)
            return

        # Applying the settings and defaults where requried
        if len(num_clicks) == 0:
            self.num_clicks = 2
        else:
            self.num_clicks = int(num_clicks)

        if len(upper_interval) == 0:
            self.upper_interval = 1.75
        else:
            self.upper_interval = float(upper_interval)

        if len(lower_interval) == 0:
            self.lower_interval = 0.75
        else:
            self.lower_interval = float(lower_interval)

        self.label_welcome["text"] = "Status: FEEDING..."

        # beginning the processing each pet
        for group in self.pets_to_feed:
            # grab all the pet types for a specific group
            pet_variants = pets[group]

            # adding random delay
            sleep_time = random.uniform(self.lower_interval, self.upper_interval)
            time.sleep(sleep_time)

            # a set of pets we don't own
            missing_pets = None

            # a set of pages we've already scanned for missing pets
            processed_pages = set()

            # used to track if the last pet in a variant was skipped
            before_skipped = False

            print("Pet variants: ")
            for v in pet_variants:
                print(str(v))

            # used to track if we are currently on the menu
            current_pet_page = 1

            last_pet_to_feed_slot = pet_variants[-1].slot_num
            for variant in pet_variants:

                if not before_skipped:
                    # click to be redirected to new menu with some random delay
                    # would either go to feeding or into pet subgroup
                    x, y = self.slot_location[self.pets_to_feed[group]]

                    pyautogui.moveTo(x, y)
                    pyautogui.click(button="right")

                    # adding random delay
                    sleep_time = random.uniform(self.lower_interval, self.upper_interval)
                    time.sleep(sleep_time)

                # stalling program until we switch from the Pets page to a different page
                print("Waiting for page change indicated by missing boat")
                self.boat.imagegone_loop(0.05)

                print(f"Working on pet {variant}")
                s = variant

                print("pages", current_pet_page, s.page)
                if current_pet_page != s.page:
                    # if we do have the pet go to the right page
                    for i in range(s.page - 1):
                        print(f"Going to next page")
                        pyautogui.moveTo(self.slot_location[50])  # 50 is the slot location of the next arrow
                        pyautogui.click(button='right')

                        # adding random delay
                        sleep_time = random.uniform(self.lower_interval, self.upper_interval)
                        time.sleep(sleep_time)

                        current_pet_page += 1

                # if we have more than 1 pet look for messing
                if s.page not in processed_pages:

                    processed_pages.add(s.page)

                    # moving mouse off item so we can scan window without any obstructions
                    if len(pet_variants) > 1:
                        x_mouse, y_mouse = self.slot_location[0]
                        x_mouse -= self.tile_size
                        # finding missing pets in slot
                        pyautogui.moveTo(x=x_mouse, y=y_mouse,
                                         duration=0.4)  # mouse should just go somewhere off screen
                        time.sleep(1)
                        missing_pets = self.get_missing_pets()
                    else:
                        missing_pets = []
                    print(f"Missing pet(s): {missing_pets}")

                # if we don't have the pet don't attempt to feed it
                # TODO Alternatively instead of checking if a pet exists allow the user to input it
                if s.slot_num in missing_pets:
                    print(f"skipping pet because missing")
                    # if the last pet to check is
                    if last_pet_to_feed_slot == s.slot_num:
                        for _ in range(s.page):
                            pyautogui.moveTo(self.slot_location[48])
                            pyautogui.click(button='right')

                            # adding delay in between page flips
                            time.sleep(1.5)

                    # set to true indicates that we are skipping
                    # and that we should not reenter a pet variant submenu
                    before_skipped = True
                    continue

                else:
                    before_skipped = False

                # if the icon itself goes to the page and there are no subvariants
                # then we should already be on the food page
                if s.slot_num != -1:
                    # opening the feeding page of the pet
                    pyautogui.moveTo(self.slot_location[s.slot_num])
                    pyautogui.click(button='right')

                    # adding random delay
                    sleep_time = random.uniform(self.lower_interval, self.upper_interval)
                    time.sleep(sleep_time)

                # waiting until the menu changes to the pet window
                # done by searching for the book icon continuously
                self.book.imagesearch_loop(0.05)  # minecraft runs at 1/20s

                # resetting the page number
                current_pet_page = 1

                # taking care of the pet
                self.process_pet(pet=variant)

                # exiting the feeding menu
                pyautogui.moveTo(self.slot_location[49])
                pyautogui.click(button='right')

                # adding random delay
                sleep_time = random.uniform(self.lower_interval, self.upper_interval)
                time.sleep(sleep_time)
                print("exited pet feeding area")
                # waiting for the menu switch
                self.gold_pants.imagesearch_loop(0.05)  # minecraft runs at 1/20s

                # enter pets menu by clicking bone
                print("Entering pet menu")
                pyautogui.moveTo(self.slot_location[9])
                pyautogui.click(button='right')

                # waiting until we are on the pet menu
                self.boat.imagesearch_loop(0.05)

        self.label_welcome["text"] = "Status: IDLE"

    def help(self):
        help_message = 'To use, first DESPAWN CURRENT PET if spawned. Next,\n' \
                       'select the collectables icon (chest in hotbar)\n' \
                       'with only the custom texture pack on. Next enter\n' \
                       'the pet menu by clicking the bone. Hit "Generate slot\n"' \
                       'Position" this will tell the program where to move\n' \
                       'the mouse to click each slot. Press "Scan For Pets". \n' \
                       'Once the scan is complete, enter a random click interval, default is\n' \
                       '0.4s to 0.8s. Fill in the number of clicks minimum should\n' \
                       'be 1 default is 2. This is the number of times the pet will\n' \
                       'be fed. Lastly, select "Feed Pets" to beginning feeding'
        messagebox.showinfo(title="HELP", message=help_message)

    def process_pet(self, pet):
        """ When called will feed the pet its favourite food, give the pet its favourite drink
            and take the pet on its favourite exercise
            :param pet the pet object """
        # feeding the pet
        if pet.food is None or pet.food == "unknown":
            print("Pet's favourite is unknown or none so choosing random (if wrong contact Tammon)")
            pyautogui.moveTo(self.slot_location[random.randint(0, 17)])
        else:
            pyautogui.moveTo(self.slot_location[self.food_maps[pet.food]])
        for _ in range(self.num_clicks):
            pyautogui.click(button='right')
            # adding random delay
            sleep_time = random.uniform(self.lower_interval, self.upper_interval)
            time.sleep(sleep_time)

        # quenching pet's thirst
        if pet.drink is None or pet.drink == "unknown":
            print("Pet's favourite drink is unknown or none so choosing random (if wrong contact Tammon)")
            pyautogui.moveTo(self.slot_location[random.randint(27, 29)])
        else:
            pyautogui.moveTo(self.slot_location[self.food_maps[pet.drink]])

        for _ in range(self.num_clicks):
            pyautogui.click(button='right')

            # adding random delay
            sleep_time = random.uniform(self.lower_interval, self.upper_interval)
            time.sleep(sleep_time)

        # exercising pet
        # quenching pet's thirst
        if pet.exercise is None or pet.exercise == "unknown":
            print("Pet's favourite exercise routine is unknown or none so choosing random (if wrong contact Tammon)")
            fun = [33, 34, 35, 42, 43, 44]
            pyautogui.moveTo(self.slot_location[random.choice(fun)])
        else:
            pyautogui.moveTo(self.slot_location[self.food_maps[pet.exercise]])

        for _ in range(self.num_clicks):
            pyautogui.click(button='right')

            # adding random delay
            sleep_time = random.uniform(self.lower_interval, self.upper_interval)
            time.sleep(sleep_time)

    def gen_slot_positions(self):
        self.label_welcome["text"] = "Status: Getting Slot Coordinates"

        # locating pets menu icon position
        icon_search = Search("assets/empty_slot.png")
        x, y = icon_search.imagesearch()

        if x == -1:
            self.label_welcome["text"] = "Status: Failed Finding Positions"
            return

        # mapping each slot to a number
        index = 0
        for j in range(6):
            for i in range(9):
                self.slot_location[index] = ((x + i * self.tile_size) + self.tile_size / 2, (y + j * self.tile_size) +
                                             self.tile_size / 2)
                print(f"{index}: {self.slot_location[index]}")
                index += 1

        self.label_welcome["text"] = "Status: Found Slot Positions"

    def get_missing_pets(self):
        """ Retrieves the slots of all pets that are missing """

        # grabbing all center coordinates of all existing matches
        locations, picture_dimension = self.missing_pet_icon.imagesearch_multiple(pic_size=True)
        w, h = picture_dimension

        # iterating over each slot to locate missing pet
        missing_pets_slot = []
        for slot in self.slot_location:
            for loc in locations:
                x, y = loc
                if self.slot_location[slot][0] - 31 <= x <= self.slot_location[slot][0] - 31 + w and \
                        self.slot_location[slot][1] - 31 <= y <= self.slot_location[slot][1] - 31 + h:
                    missing_pets_slot.append(slot)

        return set(missing_pets_slot)


if __name__ == "__main__":
    root = tkinter.Tk()
    app = Application(master=root, pet_group_img=pet_homepage, food_maps=food)
    app.mainloop()
