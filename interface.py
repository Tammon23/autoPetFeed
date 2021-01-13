import tkinter as tk
from tkinter import font, messagebox
import pyautogui
from Pet_Constants import *
from time import sleep
from screen_search import Search


class Application(tk.Frame):
    def __init__(self, master=None, pet_group_img=None, food_maps=None):
        super().__init__(master)

        self.window_width = 300
        self.window_height = 410
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry(f'{self.window_width}x{self.window_height}')
        self.master.title("Hypixel AutoPetFeeder")

        self.pet_group_img = pet_group_img
        self.food_maps = food_maps
        self.pets_to_feed = None
        self.slot_location = None
        self.pet_menu = None

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        myFont = font.Font(size=15)
        button_width = 25
        self.label_welcome = tk.Label(self, text="Status: IDLE", font=myFont)  # fg, bg, width, height
        self.label_welcome.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.btn_get_slot_pos = tk.Button(self,
                                          text="Generate Slot Position",
                                          command=self.gen_slot_positions,
                                          width=button_width,
                                          font=myFont, borderwidth=4)
        self.btn_get_slot_pos.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.btn_pet_icons = tk.Button(self,
                                       text="Scan For Pets",
                                       command=self.find_pets,
                                       width=button_width,
                                       font=myFont, borderwidth=4)
        self.btn_pet_icons.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.label_upper_interval = tk.Label(self, text="Upper Interval:", font=myFont)  # fg, bg, width, height
        self.label_upper_interval.grid(row=3, column=0, padx=5, pady=5)

        self.entry_upper_interval = tk.Entry(self, bd=5)
        self.entry_upper_interval.grid(row=3, column=1)

        self.label_lower_interval = tk.Label(self, text="Lower Interval:", font=myFont)  # fg, bg, width, height
        self.label_lower_interval.grid(row=4, column=0, columnspan=1, padx=5, pady=5)

        self.entry_lower_interval = tk.Entry(self, bd=5)
        self.entry_lower_interval.grid(row=4, column=1)

        self.btn_feed = tk.Button(self,
                                  text="Feed Pets",
                                  command=self.feed_pets,
                                  width=button_width,
                                  font=myFont,
                                  borderwidth=4)
        self.btn_feed.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.btn_help = tk.Button(self,
                                  text="HELP",
                                  command=self.help,
                                  width=button_width,
                                  font=myFont,
                                  borderwidth=4)
        self.btn_help.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.quit = tk.Button(self,
                              text="QUIT",
                              fg="red",
                              command=self.master.destroy,
                              width=button_width,
                              font=myFont,
                              borderwidth=4)
        self.quit.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.label_version = tk.Label(self, text="Tammon - v1.0.0")
        self.label_version.grid(row=8, column=1, sticky="e")

    def find_pets(self):
        """ When called will look through for all pet types and record the location"""
        self.label_welcome["text"] = "Status: SCANNING..."
        pets_to_feed = {}
        # searching for the pet based on default icon images
        for pet in self.pet_group_img:

            if self.pet_group_img[pet] == "":
                print(f"Unknown image for pet: {pet}")

            else:
                icon_search = Search(self.pet_group_img[pet])
                pos = icon_search.imagesearch()

                if pos[0] != -1:
                    print(f"Pet icon for pet '{pet}' was located")
                    pets_to_feed[pet] = pos

                else:
                    print(f"Could not find icon for pet '{pet}' | Reference image: location '{self.pet_group_img[pet]}")

        self.pets_to_feed = pets_to_feed

        self.label_welcome["text"] = "Status: IDLE"

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

        if self.pet_menu is None:
            error_message = 'Please generate slot positions first!'
            messagebox.showerror(title="ERROR", message=error_message)
            return

        self.label_welcome["text"] = "Status: FEEDING..."
        print("Feeding pets")
        self.label_welcome["text"] = "Status: IDLE"

    def help(self):
        help_message = 'To use select the collectables icon (chest in hot bar)\n' \
                       'with the default 1.8 texture pack on. Select "Generate\n' \
                       'Slot Position" this will tell the program where to move\n' \
                       'the mouse to click each slot. Next enter the pet menu by\n' \
                       'clicking the bone. Press "Scan For Pets". Once the scan\n' \
                       'is complete, enter a random click interval, default is\n' \
                       '0.4s to 0.8s. Lastly, select "Feed Pets" to beginning feeding'
        messagebox.showinfo(title="HELP", message=help_message)

    def process_pet(self, pet, num_clicks=2):
        """ When called will feed the pet its favourite food, give the pet its favourite drink
            and take the pet on its favourite exercise
            :param pet the pet object
            :param num_clicks the number of times the item should be clicked (max should be 2 min should be 1) """

        # feeding the pet
        pyautogui.moveTo(self.slot_location[self.food_maps[pet.food]])
        for _ in range(num_clicks):
            pyautogui.click()

        # quenching pet's thirst
        pyautogui.moveTo(self.slot_location[self.food_maps[pet.drink]])
        for _ in range(num_clicks):
            pyautogui.click()

        # exercising pet
        pyautogui.moveTo(self.slot_location[self.food_maps[pet.exercise]])
        for _ in range(num_clicks):
            pyautogui.click()

        # returning to the collectibles menu
        pyautogui.moveTo(self.slot_location[49])  # 49 is the slot of the collectibles chest
        pyautogui.click()

        # returning to the pets menu
        pyautogui.moveTo(self.pet_menu)
        pyautogui.click()

    def gen_slot_positions(self):
        self.label_welcome["text"] = "Status: Getting Slot Coordinates"

        # locating pets menu icon position
        icon_search = Search("assets/bone.png")
        x, y = icon_search.imagesearch()

        if x == -1:
            self.label_welcome["text"] = "ERROR: NOT ON PET PAGE"
            return

        self.pet_menu = (x, y)
        y -= 36
        index = 0

        # mapping each slot to a number
        for i in range(9):
            for j in range(6):
                self.slot_location[index] = (x + i * 36, y + j * 36)
                index += 1

        self.label_welcome["text"] = "Status: IDLE"


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root, pet_group_img=pet_homepage, food_maps=food)
    app.mainloop()
