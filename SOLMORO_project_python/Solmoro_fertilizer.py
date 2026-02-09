#Kriztian Mer J. Solmoro
#G-6L
#Description: This will serve as the file for the plant section of the project

import time 

#ascii art stuff-------------------------------------------------------------------------------------

fertilizer_ascii = r"""

         _____              _    _  _  _
        |  ___|  ___  _ __ | |_ (_)| |(_) ____  ___  _ __  ___
        | |_    / _ \| '__|| __|| || || ||_  / / _ \| '__|/ __|
        |  _|  |  __/| |   | |_ | || || | / / |  __/| |   \__ \
        |_|     \___||_|    \__||_||_||_|/___| \___||_|   |___/

    
"""


FertilizerSelection = """
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
+------------------+  +------------------+  +------------------+  +------------------+  +------------------+
|       (1)        |  |       (2)        |  |       (3)        |  |        (4)       |  |        (5)       |
|   Purchase a     |  |  View Specific   |  |     View all     |  |   View Affected  |  |       Main       |
|   Fertilizer     |  |   Fertilizer     |  |    Fertilizers   |  |      Plants      |  |       Menu       |
+------------------+  +------------------+  +------------------+  +------------------+  +------------------+
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

"""
catArt = r"""
 /\_/\  
( o.o ) @~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@
 > ^ <
 """

cloverPatch = r"""
               {{{}}    ,,,             {{{}}    ,,,
            ,,, ~Y~    {{{}},,,      ,,, ~Y~    {{{}},,,
           {{}}} |/,,,  ~Y~{{}}}    {{}}} |/,,,  ~Y~{{}}}
            ~Y~ \|{{}}}/\|/ ~Y~  ,,, ~Y~ \|{{}}}/\|/ ~Y~  ,,,
            \|/ \|/~Y~  \|,,,|/ {{}}}\|/ \|/~Y~  \|,,,|/ {{}}}
            \|/ \|/\|/  \{{{}}/  ~Y~ \|/ \|/\|/  \{{{}}/  ~Y~
            \|/\\|/\|/ \\|~Y~//  \|/ \|/\\|/\|/ \\|~Y~//  \|/
            \|//\|/\|/,\\|/|/|// \|/ \|//\|/\|/,\\|/|/|// \|/
        jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""

viewFertImg = """
||    ⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀
||⠀⠀⠀⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠁⠀
||⠀⠀⠀⠀⠀⢠⣶⣶⣶⣶⣶⣶⣶⠖⢀⡀⠲⣶⣶⣶⣶⣶⣶⣶⡄⠀⠀⠀⠀
||⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠏⣀⣴⣿⣿⣦⡈⠻⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀
||⠀⠀⠀⠀⢀⣿⣿⣿⡿⠋⣡⣾⣿⣿⠛⣿⣿⣿⣶⣌⠻⣿⣿⣿⣿⠀⠀⠀⠀⠀
||⠀⠀⠀⠀⢸⣿⣿⣋⣀⣘⡛⢻⣿⠃⠀⠈⢿⣿⡟⢛⣃⣈⣛⣿⣿⠀⠀⠀⠀⠀
||⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠏⢸⣿⠀⠀⠀⠀⢙⡇⠸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
||⠀⠀⠀⠀⣾⣿⣿⣿⣿⠏⢠⣿⣿⣷⣄⠀⣴⣿⣿⡄⠹⣿⣿⣿⣿⠀⠀⠀⠀⠀
||⠀⠀⠀⠀⣿⣿⣿⣿⠏⣠⣿⣿⣿⣿⣿⠀⠛⠙⠛⢿⣄⠙⣿⣿⣿⠀⠀⠀⠀⠀
||⠀⠀⠀  ⣿⣿⡿⠃⣼⠟⠉⠀⠀⠀⠹⠃⣀⣀⠀⠀⠹⣧⠈⢿⣿⠀⠀⠀⠀⠀
||⠀⠀⠀⠀⢿⣿⠁⣼⣿⣦⣤⣀⣀⣀⡀⠀⣿⣿⣿⣿⣷⣿⣧⠈⣿⠀⠀⠀⠀⠀
||⠀⠀⠀⠀⢸⣿⡄⠹⣿⡿⠿⠿⠿⠟⠃⠘⠻⠿⠿⠿⢿⣿⠏⢠⣿⠀⠀⠀⠀⠀
||⠀⠀⠀⠀⠘⣿⣿⣦⣄⠀⠐⠶⠶⣶⣶⣶⣶⠶⠶⠂⠀⣠⣴⣿⡟⠀⠀⠀⠀⠀
||⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀
||⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠛⠛⠛⠛⠛⠛⠋⠉⠉⠉⠁
========================================
"""

viewAllImg = r"""
======================================================================
||  ___        _   _ _ _              ___ _                         ||
|| | __|__ _ _| |_(_) (_)______ _ _  / __| |_ ___ _ _ __ _ __ _ ___ ||
|| | _/ -_) '_|  _| | | |_ / -_) '_| \__ \  _/ _ \ '_/ _` / _` / -_)||
|| |_|\___|_|  \__|_|_|_/__\___|_|   |___/\__\___/_| \__,_\__, \___|||
||                                                        |___/     ||
======================================================================
"""
sadCat = r"""
 /\_/\  
( u.u )  -------------------------------------------------------------
 > ^ <
"""

#ascii art stuff--------------------------------------------------------------------------------------

fertDict = {}
id_counter = 1 #counter for the unique fertilizer id

#for the id counter-----------------------------------------------------------------------
def saveCounter(x):
  global id_counter

  try: 
    with open("Fertilizer_Dictionary.dat", "r") as sFertD: #brings an error if the counter loads with the dat file empty, so check if it has content first
      if sFertD.readline(): #check if the first line in the .dat file exists

        fertIds = [x for x in x.keys()]
        lastID = int(fertIds[-1][-1])
        print(lastID)
        id_counter = lastID + 1

      else:
        id_counter = 1

  except FileNotFoundError:
    id_counter = 1
#for the id counter-----------------------------------------------------------------------


#fertilizer menu-------------------------------------------------------------------------
def displayFertilizerMenu():
    print(cloverPatch)
    print(fertilizer_ascii)
    print(FertilizerSelection)
    print(catArt)

def fertilizerMenu():
  while True:
        displayFertilizerMenu()  # Display fertilizer menu
        try:
            fertChoice = int(input("How may we assist you with fertilizers? "))
            if fertChoice in range(1, 6):
                if not handleFertilizerChoice(fertChoice, fertDict):
                    break  #exit if the user chooses "Return" (option 7)
            else:
                print("Please select from one of the options (>n<)!")
                time.sleep(1)
        except ValueError:
            print("Please enter a valid number from the choices (>n<)!")
            time.sleep(1)
#fertilizer menu-------------------------------------------------------------------------------------------

#saveFertilizer-------------------------------------------------------------------------------------------
def saveFertDict(x):
    with open("Fertilizer_Dictionary.dat", "w") as sFertD: #opens the separate file
        for fertIds, fertDetails in x.items(): 
            fName = fertDetails["Fertilizer Name"]
            fAmount = fertDetails["Amount"]
            fSupplier = fertDetails["Last Supplier"]
            sFertD.write(f"{fertIds}, {fName}, {fAmount}, {fSupplier}\n") #save fertilizer data
#saveFertilizer-------------------------------------------------------------------------------------------

#load the fertilizer file-------------------------------------------------------------------------------------------
def loadFertDict(x):
    try:
        with open("Fertilizer_Dictionary.dat", "r") as sFertD:
            for line in sFertD:
                fertDetails = line.strip().split(", ")
                fertId = fertDetails[0]
                fName = fertDetails[1]
                fAmount = float(fertDetails[2])
                fSupplier = fertDetails[3]
                x[fertId] = {
                "Fertilizer Name": fName,
                "Amount": fAmount,
                "Last Supplier": fSupplier
                }

    except FileNotFoundError :
        print(catArt)
        print("The fertilizer storage is empty ! (0w0) Time to start buying!")

#load the fertilizer file-------------------------------------------------------------------------------------------

loadFertDict(fertDict) #load file into the dictionary
saveCounter(fertDict) #ids follow suit

#buyFertilizer----------------------------------------------------------------------------------------
def purchFert(x):  # Adding the fertilizer
    print(catArt)
    global id_counter  # To access the counter, had no choice but to resort to global 

    while True:  # Loop in case the user wants to buy multiple fertilizers without going back to the menu
        fName = str(input("What fertilizer would you like to buy? ")).lower().capitalize()

        # Ask for amount
        while True:
            try:
                fAmount = float(input("How much should we buy? "))
                if fAmount < 1:
                    print("Please enter a valid amount, at least 1! (>n<)")
                else:
                    break
            except ValueError:
                print("Please enter a valid amount! (>n<)")

        # Ask for supplier
        fSupplier = str(input("From which supplier or partner should we buy them? "))

        # Check if the fertilizer is already in the dictionary
        alreadyHave = False
        for fertId, fertDetails in x.items():  # Loop through fertilizer ids
            if fName == fertDetails["Fertilizer Name"]:  # Check if the fertilizer is already in the dictionary
                fertDetails["Amount"] += fAmount
                fertDetails["Last Supplier"] = fSupplier
                alreadyHave = True
                print(f"Updated {fName} in inventory. New amount: {fertDetails['Amount']} from {fSupplier}.")
                time.sleep(2)
                break  # End the loop once it matches

        #If the fertilizer was not already in the dictionary, create a new entry
        if not alreadyHave:
            fertId = f"F{id_counter}"  #Generate fertilizer ID
            id_counter += 1
            #Adding the entry into the dictionary
            x[fertId] = {
                "Fertilizer Name": fName,
                "Amount": fAmount,
                "Last Supplier": fSupplier
            }
            print(f"Added {fAmount} of {fName} from {fSupplier} as a new fertilizer.")
            time.sleep(2)

        #save it to a separate file
        saveFertDict(fertDict)

        #---------------log-------------------------
        from Solmoro_Logbook import addLogEntry
        from Solmoro_Logbook import logDict
        from Solmoro_Logbook import saveLogbook

        action = "purchase"
        plantId = "NA"

        addLogEntry(logDict, plantId, fertId, action)
        saveLogbook(logDict)
        print("~Successfully logged!~")

        #---------------log-------------------------

        # Ask if the user wants to buy another fertilizer
        print(catArt)
        newFert = input("Would you like to buy another fertilizer (OwO)? [y/n]: ").strip().lower()
        while newFert not in ["y", "n"]:  # In case the user chooses something else
            newFert = input("Please answer me properly! (UnU) [y/n]: ").strip().lower()

        if newFert == "n":
            print("Ok!")
            time.sleep(2)
            break  # Exit the loop and go back to the main menu
   
#buyFertilizer--------------------------------------------------------------------------------------

#view fertilizer-------------------------------------------------------------------------------------------
def viewFertilizer(x): 
    print(catArt)
    toView = input("What is the name of the fertilizer that you would like to view?").strip().lower()
    print("==============================================================================")

    #checker if the fertilizer is found in the dictionary
    fertFound = False

    for fertIds, fertInfo in x.items(): #iterates through the dictionaries within the dictionary
        if fertInfo["Fertilizer Name"].lower() == toView: #checks if the fertilizer name is in the dictionary
            fertFound = True #updates the value if true
            #the actual display
            print(catArt)
            print("We found the fertilizer! UwU")
            print(viewFertImg)
            print(f"||Fertilizer ID: {fertIds}")
            print(f"||Fertilizer Name: {fertInfo['Fertilizer Name']}")
            print(f"||Amount: {fertInfo['Amount']}")
            print(f"||Last Supplier: {fertInfo['Last Supplier']}")
            time.sleep(3)
            return

    if not fertFound:
        print(sadCat)
        print(f"My apologies, we did not find any fertilizer named {toView} in the storage...")
        time.sleep(3)
#view fertilizer-------------------------------------------------------------------------------------------

#view all--------------------------------------------------------------------------------------------------

def viewAll(x):
    print(catArt)
    print("~ As you wish ~")
    print(catArt)
    print("Servants! Bring in the fertilizers!")
    time.sleep(1)
    print("hai~")
    time.sleep(1)
    print("hai~")
    time.sleep(1)
    print(viewAllImg)
    columns = r"""
    || ID ||   Fertilizer Name   ||   Amount   ||   Last Supplier   ||
    ==================================================================
    """
    print(columns)

    for fertIds, fertInfo in x.items(): #loops through the ids in the dicitionary then loops in the details in them
        print(f"    || {fertIds} ||    {fertInfo['Fertilizer Name']}    ||   {fertInfo['Amount']}   ||   {fertInfo['Last Supplier']}   ||")

    if not x:
        print(sadCat)
        print("!!-Oh no! There doesn't seem to be anything in the storage!-!!")
        print("--------------------------------------------------------------------")

    time.sleep(3)

#viewall---------------------------------------------------------------------------------------------------

#viewAffectedPlants----------------------------------------------------------------------------------------

def viewAffectedPlants(x):
    #import plant dictionary and save function
    from Solmoro_plantS import plantDict

    print(catArt)
    toView = input("('o') Which fertilizer would you like to account for? Please enter its ID! ('o') ").strip().upper()

    #checker if fertilizer is found
    fertFound = False

    for fertIds, fertInfo in x.items(): #find the fertilizer ID in the fertilizer dictionary
        if fertIds == toView:
            fertFound = False

            #get the information from the dictionary
            print(catArt)
            print("Getting the list of all plants who needs this fertilizer...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)

            plantFound = False #for the plant

            for plantIds, plantInfo in plantDict.items(): #loop through the plant dictionary
                for reqFert in plantInfo["Plant Nourishment"]:
                    if reqFert.lower() == fertInfo["Fertilizer Name"].lower(): #check if the fertilizer matches the one in plant nourishment
                        plantList = []
                        plantList.append(plantInfo["Plant Name"])

                        print("We're doooone! Here are the list of plants associated with this fertilizer!: ")
                        print(viewFertImg)
                        print(f"||Fertilizer ID: {fertIds}")
                        print(f"||Fertilizer Name: {fertInfo['Fertilizer Name']}")
                        print(f"||Amount: {fertInfo['Amount']}")
                        print(f"||Last Supplier: {fertInfo['Last Supplier']}")
                        print("||Affected Plants:")
                        for plants in plantList:
                            print(f"||      (^w^) {plants}")
                            time.sleep(1)

                        plantFound = True
                        fertFound = True
                        time.sleep(5)
                        
                        return

                    else: 
                        print(sadCat)
                        print(f"Oh shucks, there are no plants that need {fertInfo['Fertilizer Name']}!")
                        time.sleep(3)

        if not fertFound:
            print(sadCat)
            print(f"We could not find any fertilizer with the ID: {toView} in the fertilizer storage!")
            time.sleep(2)

#viewAffectedPlants----------------------------------------------------------------------------------------


#menu stuff

#the main menu stuff
def handleFertilizerChoice(choice, fertDict):
    if choice == 1:
        purchFert(fertDict)
    elif choice == 2:
        viewFertilizer(fertDict)
    elif choice == 3:
        viewAll(fertDict)
    elif choice == 4:
        viewAffectedPlants(fertDict)
    elif choice == 5:
        print(catArt)
        print("Returning...")
        time.sleep(1)
        print("~~~")
        time.sleep(1)
        return False  #exit the fertilizer menu to return to the main menu
    return True

#References:
#OpenAI. (2024). ChatGPT (Version 4). Retrieved from https://chat.openai.com
#Stark, J. G.: (n.d.). ASCII flower. ASCII Art Copy. Retrieved November 11, 2024, from https://www.asciiartcopy.com/ascii-flower.html
#Emoji Combos. (n.d.). Fertilizer bag text art. Emoji Combos. https://emojicombos.com/fertilizer-bag-text-art
#W3Schools. (n.d.). Python tutorial. W3Schools. Retrieved November 27, 2024, from https://www.w3schools.com/python/
