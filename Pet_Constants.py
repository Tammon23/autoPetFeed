from Pet import Pet

pets = {
    "Silverfish": [Pet("stick", "water", "cake", "Silverfish")],
    "Cat": [Pet("stick", "water", "cake", "Cat")],                                                #
    "Chicken": [Pet("frisbee", "water", "flower", "Adult_Chicken"),
                Pet("stick", "milk", "cookie", "Baby_Chicken")],
    "Wolf": [Pet("leash", "water", "bone", "Adult_Wolf"),
             Pet("ball", "milk", "cookie", "Adult_Wolf")],
    "Bat": [Pet("stick", "water", "melon")],
    "Rabbit": [Pet("stick", "water", "carrot", "Black_Rabbit"),
               Pet("stick", "water", "carrot", "Brown_Rabbit"),
               Pet("stick", "water", "carrot", "White_Rabbit"),
               Pet("ball", "water", "carrot", "Black_&_White_Rabbit"),
               Pet("ball", "water", "carrot", "Gold_Rabbit"),
               Pet("ball", "water", "carrot", "Salt_&_Pepper_Rabbit"),
               Pet("sword", None, "unknown", "Killer_Rabbit")],
    "Villager": [Pet("stick", "water", "cake", "Cat")],                                           #
    "Zombie": [Pet("stick", "water", "cake", "Cat")],                                             #
    "Little_Helper": [Pet("frisbee", "milk", "cookie", "Red_Helper"),
                      Pet("ball", "milk", "cake", "Green_Helper")],
    "Golem": [Pet("ball", "lava", "flower", "Golem")],
    "Enderman": [Pet("ball", "milk", "potato", "Enderman")],
    "Blaze": [Pet("stick", "lava", "magma_cream", "Blaze")],
    "Snowman": [Pet("stick", "water", "carrot", "Snowman")],
    "Herobrine": [Pet("sword", "milk", "cookie", "Herobrine")],
    "Endermite": [Pet("sword", "lava", None, "Endermite")],
    "Mini_Wither": [Pet(None, "lava", "rotten_flesh", "Mini_Wither")],
    "Clone": [Pet("unknown", "unknown", "unknown", "Clone")],
    "Minecart": [Pet("unknown", "unknown", "unknown", "Clone")],                                 #
    "Grinch": [Pet("frisbee", "water", "cookie", "Grinch")],
    "Spider": [Pet("leash", "water", "unknown", "Spider"),
               Pet("sword", "water", "steak", "Cave_Spider"),
               Pet("unknown", "unknown", "steak", "Bouncy_Spider")],
    "Cow": [Pet("feather", "milk", "wheat", "Adult_Cow"),
            Pet("ball", "milk", "pumpkin_pie", "Baby_Cow"),
            Pet("feather", "milk", "mushroom_soup", "Adult_Mooshroom"),
            Pet("feather", "milk", "cookie", "Baby_Mooshroom")],
    "Creeper": [Pet("leash", "lava", "cake", "CREEPER"),
                Pet("sword", "lava", "cake", "CREEPER")],
    "Horse": [Pet("unknown", "unknown", "unknown", "Clone")],                                  #
    "Pig": [Pet("frisbee", "water", "apple", "Adult_Pig"),
            Pet("leash", "milk", "apple", "Baby_Pig"),
            Pet("frisbee", "lava", "melon", "Adult_Pigman"),
            Pet("sword", "milk", "cookie", "Baby_Pigman")],
    "Sheep": [Pet("leash", "water", "wheat", "Black_Sheep"),
              Pet("leash", "water", "wheat", "Blue_Sheep"),
              Pet("leash", "water", "wheat", "Brown_Sheep"),
              Pet("leash", "water", "wheat", "Cyan_Sheep"),
              Pet("leash", "water", "wheat", "Gray_Sheep"),
              Pet("leash", "water", "wheat", "Green_Sheep"),
              Pet("leash", "water", "wheat", "Light_Blue_Sheep"),
              Pet("leash", "water", "wheat", "Lime_Sheep"),
              Pet("leash", "water", "wheat", "Magenta_Sheep"),
              Pet("leash", "water", "wheat", "Orange_Sheep"),
              Pet("leash", "water", "wheat", "Pink_Sheep"),
              Pet("leash", "water", "wheat", "Purple_Sheep"),
              Pet("leash", "water", "wheat", "Red_Sheep"),
              Pet("leash", "water", "wheat", "Silver_Sheep"),
              Pet("leash", "water", "wheat", "White_Sheep"),
              Pet("leash", "water", "wheat", "Yellow_Sheep"),
              Pet("leash", "water", "wheat", "Rainbow_Sheep"),
              Pet("leash", "water", "wheat", "Bouncy_Sheep"),
              Pet("leash", "water", "wheat", "Merry_Sheep"),
              Pet("frisbee", "milk", "melon", "Black_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "Blue_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "Brown_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "Cyan_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "Gray_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "Green_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "Light_Blue_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "Lime_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "Magenta_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "Orange_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "Pink_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "Purple_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "Red_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "Silver_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "White_Baby_Sheep"),
              Pet("frisbee", "milk", "melon", "Yellow_Baby_Sheep")],
    "Slime": [Pet("ball", "milk", "bone", "Big_Slime"),
              Pet("unknown", "milk", "raw_fish", "Small_Slime"),  # document says Frisbee, Milk, Raw Fish
              Pet("frisbee", "milk", "raw_fish", "Tiny_Slime"),
              Pet("feather", "lava", "magma_cream", "Big_Magma_cube"),
              Pet("ball", "lava", "magma_cream", "Small_Magma_cube"),
              Pet("frisbee", "milk", "magma_cream", "Tiny_Magma_cube")],
    "Skeleton": [Pet("frisbee", "lava", "rotten_flesh", "Skeleton"),
                 Pet("sword", "lava", "none", "Wither_Skeleton"),
                 Pet("ball", "water", "bone", "Frozen_Skeleton")],
    "Guardian": [Pet(None, "water", "flower", "Guardian"),
                 Pet("unknown", "water", "flower", "Elder_Guardian")],
    "Squid": [Pet("frisbee", "water", "raw_fish")]
}

# Cats:
# Adult cats: Black, Red, Siamese, Wild ocelot
# Ball, Milk, Raw Fish
# Baby cats: Black, Red, Siamese, wild ocelot
# Leash, Milk, Cake


#
# Villagers:
# Adult Blacksmith and Adult Butcher:
# Steak, Lava, Sword
# Baby Blacksmith:
# Stick, Milk, Pumpkin Pie
# Baby Butcher:
# Ball, Milk, Cookie
# Adult Farmer:
# Feather, Milk, Potato
# Baby Farmer:
# Stick, Milk, Cake
# Adult Librarian:
# Frisbee, Water, Apple
# Baby Librarian:
# Feather, Milk, Cookie
# Adult Priest:
# Frisbee, Water, Bread
# Baby Priest:
# Feather, Milk, Cake
# Zombie Villager:
# Stick, Lava, Rotten Flesh
# Witch:
# Feather, Milk, Pumpkin Pie
#
# Zombies:
# Adult Zombie:
# Sword, Lava, Rotten Flesh
# Baby Zombie:
# Sword, Milk, Cake
# Frozen Zombie:
# unknown
# Growing Zombie:
# unknown
#

# Horses:
# Adult Horses: Black, Brown, white, Chestnut, Creamy, Dark browm, Gray
# Leash, Water, Apple
# Mule and Donkey:
# Leash, Water, Hay
# Baby Brown Horse:
# Stick, Milk, Apple
# Other Baby Horses: Chestnut, Creamy, Dark browm, Gray
# Leash, Milk, Cake
# Skeleton and Undead Horses:
# Stick, Lava, Rotten Flesh


