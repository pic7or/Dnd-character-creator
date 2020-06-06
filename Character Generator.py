# Boss creator
# Dnd boss creator v1.0 by pic7or
# to do list:

# 1. # lv generator
# 2. Button for generator
# Dice 6 face
# HP creator
# Race and Class Choice
# apply stats from class and race
# name generator


from tkinter import *
import random

root = Tk()
root.title("Character Generator by Pic7oR")


name_male = [" Lydan ", " Syrin ", " Ptorik ", " Joz Varog ", " Gethrod Hezra ", " Feron Ophni ", " Colborn Fintis ", " Gatlin Jinto ", " Hagalbar Krinn", "Lenox Revvyn", "Hodus Dimian", "Paskel", "Kontas", "Weston", "Azamarr Jather", "Kent", "Moki", "Rankar", "Lothe", "Ryven", "Clawsen", "Pakker", "Embre", " Cassian ", " Verssek ", " Dagfinn ", " Ebraheim ", " Nesso ", " Eldermar ", " Rivik ", " Rourke ", " Barton ", " Hemm ", " Kagran ", " Lassrin " , " Vadim ", " Arlo ", " Quintis ", " Vale ", " Caelan ", " Yorjan ", " Khron ", " Ishmael ", " Jakrin ", " Fangar ", " Roux ", " Baxar ", " Hawke ", " Gatlen ", " Barak ", " Nazim ", " Kadric ", " Paquin "]
name_female = ["Syrana", "Resha", "Varin", "Wren", "Yuni", "Talis", "Kessa", "Magaltie", "Aeris", "Desmina", "Krynna", "Herra", "Pret", "Kory", "Afia", "Tessel", "Rhiannon", "Zara", "Jesi", "Belen", "Rei", "Ciscra", "Temy", "Renalee", "Estyn", "Maarika", "Lynorr", "Tiv", "Annihya", " Semet", " Tamrin ", " Antia ", " Reslyn ", " Basak ", " Vixra ", " Pekka ", " Xavia ", " Beatha ", " Yarri ", " Liris ", " Sonali "," Razra ", " Soko ", " Maeve ", " Everen ", " Yelina ", " Morwena ", " Hagar ", " Palra ", " Elysa ", " Sage ", " Ketra ", " Lynx ", " Agama ", " Thesra ", " Tezani ", " Ralia ", " Esmee ", " Heron "]

male_or_female = ["| Male |", "| Female |"]


def command():
    display.delete("1.0", END)
    gender_and_name()
    lv_generator()
    class_generator()


def stats_generator(stat):
    six_dice_1 = random.randint(2, 6)
    six_dice_2 = random.randint(2, 6)
    six_dice_3 = random.randint(2, 6)
    stat += ((six_dice_3 + six_dice_2 + six_dice_1) -11) // 2
    display.insert(END, stat)

def gender_and_name():
    gender = random.choice(male_or_female)
    display.insert(END, gender)
    if gender == "| Male |":
        name = random.choice(name_male)
    else:
        name = random.choice(name_female)
    display.insert(END, "| Name: " + name)

def class_generator():
    strength = 0
    intellect = 0
    charisma = 0
    constitution = 0
    wisdom = 0
    dexterity = 0
    dnd_classes = [" Ranger ", " Barbarian ", " Paladin ", " Warrior ", " Rogue ", " Wizard ", " Mystic ", " Monk "]
    character_class = random.choice(dnd_classes)
    display.insert(END, '| Class: ' + character_class)
    if character_class == " Ranger ":
        dexterity += 1
    if character_class == " Barbarian ":
        strength += 2
        intellect -= 1
    if character_class == " Paladin ":
        strength += 1
        intellect += 1
        dexterity -= 1
    if character_class == " Warrior ":
        strength += 2
        intellect -= 1
    if character_class == " Rogue ":
        dexterity += 2
        strength -=1
    if character_class == " Wizard ":
        intellect += 3
        strength -= 2
    if character_class == " Mystic ":
        intellect += 1
        wisdom += 2
        strength -=2
    if character_class == " Monk ":
        intellect -= 1
        wisdom += 2
        dexterity += 1

    dnd_races = [" Human ", " Demi-God ", " Orc ", " Elf ", " Druid ", " Goblin ", " Viking "]
    character_races = random.choice(dnd_races)
    display.insert(END, '| Race: |' + str(character_races))
    if character_races == " Human ":
        constitution += 1
        wisdom += 1
        charisma += 2
    if character_races == " Demi-God ":
        intellect += 1
        wisdom += 2
    if character_races == " Orc ":
        strength += 3
        constitution += 1
        intellect -= 2
        charisma -= 2
    if character_races == " Elf ":
        dexterity += 3
        charisma += 1
        strength -= 2
    if character_races == " Druid ":
        dexterity += 2
        intellect += 1
        wisdom += 1
        strength -= 2
        charisma -= 2
    if character_races == " Goblin ":
        dexterity += 2
        intellect += 2
        constitution += 1
        strength -= 2
        charisma -= 3
    if character_races == " Viking ":
        strength += 2
        wisdom += 2
        intellect -= 1
    display.insert(END,"| Strength: ")
    stats_generator(strength)
    display.insert(END, "| Intellect: ")
    stats_generator(intellect)
    display.insert(END, "| Dexterity: ")
    stats_generator(dexterity)
    display.insert(END, "| Wisdom: ")
    stats_generator(wisdom)
    display.insert(END, "| Charisma: ")
    stats_generator(charisma)
    display.insert(END, "| Constitution: ")
    stats_generator(constitution)

def lv_generator():
    six_dice_1 = random.randint(1, 6)
    six_dice_2 = random.randint(1, 6)
    six_dice_3 = random.randint(1, 6)
    six_dice_4 = random.randint(1, 6)
    hp = six_dice_1 + six_dice_2 + six_dice_3 + six_dice_4

    level = random.randint(5, 15)
    point_to_add = ((level * 2) -2) // 2
    hp += level * 2

    ac = random.randint(4, 16)

    display.insert(END, "| Level: ")
    display.insert(END, level)
    display.insert(END, "| HP: ")
    display.insert(END, hp)
    display.insert(END, "| AC: ")
    display.insert(END, ac)
    display.insert(END, "| Points that need to be added: ")
    display.insert(END, point_to_add)



# Button
generator = Button(root, text="New Boss", command=command)
generator.pack()

# Display
display = Text(root)
display.pack()



# Main Loop

root.mainloop()




