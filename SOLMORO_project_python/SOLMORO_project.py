#Kriztian Mer J. Solmoro
#Section: G-6L
#Code Description: A Gardening Inventory and Logging System alike to Plants vs. Zombies' zen garden part complete with a plants section, fertilizer section, and a logging system.

import time
#import the other sections
import Solmoro_plantS
import Solmoro_fertilizer
import Solmoro_Logbook

#main Menu function
def mMenu():
    print(H, G, B) #for design langz
    print("||Welcome to the Hanging Gardens of Babylon!!! ||")
    print("||[1] Inspect the Gardens | Plant Section      ||")
    print("||[2] Check Nourishment   | Fertilizer Section ||")
    print("||[3] Entries & Changes   | Logbook Section    ||")
    print("||[0] Leave               | Exit               ||")
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    print(catArt)
    while True:
        try:
            choice = int(input("Welcome to the Hanging Gardens of Babylon! Please tell us how we may be of help! "))
            if choice in range(0, 4):
                break  #exit the loop if the input is valid
            else:
                print(sadCat)
                print("I'm sorry, that cannot be done in the garden...")
        except ValueError:
            print(sadCat)
            print("I'm sorry, that cannot be done in the garden...")
    return choice

H = r"""

| | | |  __ _  _ __    __ _ (_) _ __    __ _
| |_| | / _` || '_ \  / _` || || '_ \  / _` |
|  _  || (_| || | | || (_| || || | | || (_| |
|_| |_| \__,_||_| |_| \__, ||_||_| |_| \__, |
                      |___/            |___/
"""

G = r"""
  ____                   _
 / ___|  __ _  _ __   __| |  ___  _ __   ___
| |  _  / _` || '__| / _` | / _ \| '_ \ / __|
| |_| || (_| || |   | (_| ||  __/| | | |\__ \
 \____| \__,_||_|    \__,_| \___||_| |_||___/

"""
B = r"""
         __   ____          _             _
  ___   / _| | __ )   __ _ | |__   _   _ | |  ___   _ __
 / _ \ | |_  |  _ \  / _` || '_ \ | | | || | / _ \ | '_  \
| (_) ||  _| | |_) || (_| || |_) || |_| || || (_) || | | |
 \___/ |_|   |____/  \__,_||_.__/  \__, ||_| \___/ |_| |_|
                                   |___/
"""

catArt = r"""
 /\_/\                                                 
( o.o ) 
 > ^ < 
 +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+                                                 
 """

sadCat = r"""
 /\_/\  
( u.u )  -------------------------------------------------------------
 > ^ <
"""

lastCat = r"""

      .--.                      .--.
    .'_\/_'.                  .'_\/_'.
    '. /\ .'                  '. /\ .'
      "||"                      "||"
       || /\       /\_/\  (      || /\ 
    /\ ||//\)     ( ^.^ ) _)  /\ ||//\) 
   (/\\||/          \"/  (   (/\\||/ 
______\||/_______ ( | | ) ______\||/_______

"""

def menuChoices():
    while True:
        uChoice = mMenu() 

        if uChoice == 1:
            #enter plant section
            print(catArt)
            print("Let's go in the garden~ You'll find something waiting ~")
            time.sleep(1)
            print("~~~")
            time.sleep(1)
            print("~~~")
            time.sleep(1)
            Solmoro_plantS.plantMenu() 

        elif uChoice == 2:
            #enter fertilizer section
            print(catArt)
            print("What shall we have here?~")
            time.sleep(1)
            print("~~~")
            time.sleep(1)
            print("~~~")
            time.sleep(1)
            Solmoro_fertilizer.fertilizerMenu() 

        elif uChoice == 3:
            #logbook section
            print(catArt)
            print("Going to the loooogs~")
            time.sleep(1)
            print("~~~")
            time.sleep(1)
            print("~~~")
            time.sleep(1)
            Solmoro_Logbook.LogbookMenu()  

        elif uChoice == 0:
            print(lastCat)
            print("Thank you for visiting!")
            break  #exit the program

        time.sleep(1)

if __name__ == "__main__":
    menuChoices()



#References:
#OpenAI. (2024). ChatGPT (Version 4). Retrieved from https://chat.openai.com
#Stark, J. G.: (n.d.). ASCII flower. ASCII Art Copy. Retrieved November 11, 2024, from https://www.asciiartcopy.com/ascii-flower.html
#W3Schools. (n.d.). Python tutorial. W3Schools. Retrieved November 27, 2024, from https://www.w3schools.com/python/
#ASCII Art Hub. (n.d.). Cat ascii art. ASCII Art Hub. Retrieved December 1, 2024, from https://www.asciiarthub.com/cat.html


