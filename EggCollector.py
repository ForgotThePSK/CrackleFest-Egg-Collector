import time
import pyautogui


def egg_hunt():
    # Function call takes ~6 seconds
    print("Hunting at " + str(time.ctime()))
    # Prints a notice with the hunt time
    pyautogui.click(x=1400, y=1000)
    # Clicks the text box
    pyautogui.typewrite('/hunt zone:The Arcane Void')
    time.sleep(2)
    # Enters the requested command, waits a moment, then enters 2x to parse the command
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=485, y=925)
    pyautogui.moveTo(500, 1000)
    # Clicks on the center egg
    pyautogui.moveTo(1, 1)
    # moves the mouse to avoid getting in the way of detect commands


def sell_eggs():
    # function call takes ~3 seconds
    pyautogui.click(x=1400, y=1000)
    pyautogui.typewrite('/sell_eggs exclude_quest:True')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')


def cluster_hunt():
    try:
        egg_button_loc = pyautogui.locateOnScreen("Egg_Cluster_Egg.png")
        pyautogui.click(egg_button_loc)
        pyautogui.moveTo(1, 1)
        # Searches for egg image and attempts to click the center. Moves mouse to avoid getting in the way of detects
    except pyautogui.ImageNotFoundException:
        print("There is no egg cluster detected at " + str(time.ctime()))
        # if the image is not found, prints that there is no egg cluster detected
    else:
        print("Egg cluster detected at " + str(time.ctime()))
        # If an egg cluster was detected, notes the time it was found


def five_min_cluster():
    # Function call takes ~30 seconds
    for inc in range(1, 11):
        cluster_hunt()
        print("Cluster Hunt loop number " + str(inc) + " completed at " + str(time.ctime()))
        time.sleep(30)
        # Loops the cluster_hunt command 10 times to make a 5-min loop. Prints a message to track the interval


def four_hour_loop():
    # Range 1, 49 = 48 rotations, 4 hr 4.8 min
    for inc in range(1, 47):
        print("Four hour loop cycle progress " + str(inc) + "/46")
        # Loops for just under 4 hours (Other delays roughly make up remaining time)
        egg_hunt()
        # Hunts for an egg
        five_min_cluster()
        # Searches for clusters for five minutes


def pet_recall_sale():
    print('Recalling pets and selling non-essential eggs.')
    print(" ")
    print(" ")
    print(" ")
    # Declaring Pets as an array
    pets = ['Sierra', 'Sasha', "Ella",
            'Bruno', 'Toby', 'Bear']
    sell_eggs()
    time.sleep(1)
    # Recalls and feeds all pets
    rotation_num = 0
    for pet in pets:
        # Recall Pet
        pyautogui.click(x=1400, y=1000)
        pyautogui.typewrite('/pets come_back')
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.typewrite(pet)
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        # Feed Pet
        pyautogui.click(x=1400, y=1000)
        pyautogui.typewrite('/pets feed')
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.typewrite(pet)
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        # Increment the counter for the number of consecutive pets fed
        rotation_num = rotation_num + 1
        # If this is the third pet to be recalled consecutively, sell non-essential eggs
        if rotation_num > 2:
            sell_eggs()
            rotation_num = 0
    # return all pets to hunting.
    for pet in pets:
        pyautogui.click(x=1400, y=1000)
        pyautogui.typewrite('/pets go_hunt')
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.typewrite(pet)
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)


def quest_checker():
    npcs = ["Allunaxis", "Ampaia", "Anarzee", "Bastules", "Berlya", "Bhuc", "Broti", "Chasre", "Cyndrad", "Drarv",
            "Erioxis", "Faelyn", "Futrixi", "Gnerk", "Guards", "Gwyn", "Khlorica", "Levia", "Mawu", "Neia", "Omylia",
            "Raddar", "Rhunyll", "Ryul", "Salthor", "Thesine", "Twilight", "Vetos", "Xethas", "Yennaria"]
    for npc in npcs:
        pass
        # Contact NPC
        pyautogui.click(x=1400, y=1000)
        pyautogui.typewrite('/interact')
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.typewrite(npc)
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)
        # Select the interact button
        pyautogui.click(x=425, y=925)
        pyautogui.moveTo(1400, 1000)
        time.sleep(1)
        # Complete/Accept Quest Area
        pyautogui.click(x=450, y=880)
        pyautogui.moveTo(1400, 1000)
        time.sleep(1)
    time.sleep(3)


time.sleep(3)

while True:
    quest_checker()
    pet_recall_sale()
    quest_checker()
    four_hour_loop()
