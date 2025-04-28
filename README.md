# CrackleFest-Egg-Collector

# What is it?
CrackleFest is a Discord bot that creates a egg hunt themed text based game in a discord channel.
This script was created to automate the game to compete in a server contest to hunt the most eggs. This allows the user to continue collecting eggs while away from their computer.


# How it works
The script works by using a series of function calls, designed so that the order could be rearranged to fit a desired pattern.

## Modules
This script uses Time and PyAutoGUI. Time allows for spacing out commands to account for Discord lag. Time also helps with troubleshooting   errors that occurred while the user is AFK, as it enables us to log the time of each event to the console. PyAutoGUI is essential to the script, as it allows it to manipulate your mouse, search for images on screen, and type commands.

## Functions
#### quest_checker()
CrackleFest has a list of NPCs that request the player hunt specific eggs. This function contains an array called npcs with each NPC's name. The array is fed into a for loop, and each NPC is interacted with. The complete and accept button is in the same place, simplifying things, as only one location needs to be clicked. After a quest is completed, the player must wait 12 hours before accepting another quest from that NPC, meaning there is no need to talk to an NPC again immediately after completing their quest.

#### pet_recall_sale()
CrackleFest includes a series of pets that can be unlocked by reaching different areas. each pet can hunt for eggs and has their own inventory. Similar to quest_checker(), this function contains an array that declares all pet names 

#### four_hour_loop()
This function is actually a nested function containing two additional functions, egg_hunt() and five_min_cluster(). This four_hour_loop() as the name implies, simply times these two out so that they run for a set length of approximately four hours. five_min_cluster() in turn is a nested version of cluster_hunt() that runs every 30 seconds for 5 minutes (this is because an egg hunt can be done every 5 minutes by default). The functions were nested in this way to allow times to be more easily adjusted during troubleshooting. They could reasonably be combined if desired.

##### egg_hunt()
The core gameplay look of CrackleFest involves hunting for eggs, which, by default, can be done every 5 minutes. This function automates this process by hunting for an egg, then clicking on the Discord reaction based minigame that pops up. The app simply clicks on the middle choice, as the correct egg is randomized.

##### cluster_hunt()
CrackleFest also semi-randomly generates egg clusters. Clicking on the right Discord reaction nets the player a cluster that can be broken open for a decent number of eggs. Fortunately, unlike in egg_hunt() all these reactions are different, and there is always a right answer. This function searches for "Egg_Cluster_Egg.png", which is a picture of the correct reaction. After it is found, PyAutoGUI clicks on the egg, netting the user an egg cluster.



# Notes for any users
Your pets may have different names. Check and change the code accordingly.

The x and y coordinates used are assuming Discord is full screen on a 1920 x 1080 monitor. If this is not the case they will need to be adjusted accordingly.

time.sleep commands may need to be adjusted up or down depending on how snappy your Discord is.

CrackleFest is highly configurable on the server-side. If you are an admin, review the configurations, if not, troubleshoot them and make changes as necessary to meet the configured settings.

CrackleFest also introduced bosses after this code was written. They are not addressed by this script.

The game will still require some interaction, even discounting bosses, such as opening egg clusters, however, this automation allows the player to automate all restrictive parts of the game (there is no limit to how many egg clusters you can collect, and you can open multiple at once).

If you use Discord in light mode you may need a new Egg_Cluster_Egg.png
