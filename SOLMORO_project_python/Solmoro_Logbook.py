#Kriztian Mer J. Solmoro
#G-6L
#Description: This will serve as the file for the logbook section of the project

import time

                                                                                        
                                                                                        
#ascii art--------------------------------------------------------------------------------------------------------------------------------  
book_ascii = r"""                                                                                        
                                                                                        
                              ██████████          ██████████                            
░░      ░░            ░░    ██          ██  ░░  ██          ██    ░░      ░░            
                          ██              ██  ██              ██                        
                        ██      ██  ██      ██      ██  ██      ██                      
                      ████  ██          ██  ██  ██          ██  ████                    
        ░░      ░░  ██░░██                  ██                  ██░░██    ░░      ░░    
                    ██░░██      ██  ██      ██      ██  ██      ██░░██                  
                    ██░░██  ██          ██  ██  ██          ██  ██░░██                  
                    ██░░██                  ██                  ██░░██                  
                    ██░░██                  ██                  ██░░██                  
                     _                    _                    _
                    | |      ___    __ _ | |__    ___    ___  | | __
                    | |     / _ \  / _` || '_ \  / _ \  / _ \ | |/ /
                    | |___ | (_) || (_| || |_) || (_) || (_) ||   <
                    |_____| \___/  \__, ||_.__/  \___/  \___/ |_|\_\
                                   |___/
                    ██░░░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░░░██                  
                    ██░░░░░░░░██████████░░░░░░░░░░██████████░░░░░░░░██                  
                    ██░░░░████          ██████████          ████░░░░██                  
                      ████                                      ████                    
                                                                                        
"""

logSelection = """

  /-/|       ||  /-/|         ||  /-/|              ||   /-/|       ||   /-/|
 /_/ |1|Add  || /_/ |2|View   || /_/ |3|View        ||  /_/ |4|Data ||  /_/ |5|Back to
 | |/|  Log  || | |/|  All    || | |/|  Transactions||  | |/|  Reset||  | |/|  Main Menu
 |^| |  Entry|| |^| |  Entries|| |^| |  per         ||  |^| |       ||  |^| |
 |_|/        || |_|/          || |_|/   Section     ||  |_|/        ||  |_|/
 =========================================================================================

"""

catArt = r"""
 /\_/\  
( o.o ) @~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@
 > ^ <
 """

sadCat = r"""
 /\_/\  
( u.u )  -------------------------------------------------------------
 > ^ <
"""

viewAllLog = r"""

=========================================
||  _              _              _    ||
|| | |   ___  __ _| |__  ___  ___| |__ ||
|| | |__/ _ \/ _` | '_ \/ _ \/ _ \ / / ||
|| |____\___/\__, |_.__/\___/\___/_\_\ ||
||           |___/                     ||
||                                     || 
=========================================
"""

asciiAdd = r"""

||          _    _         _          _   
||  __ _ __| |__| |   _ __| |__ _ _ _| |_ 
|| / _` / _` / _` |  | '_ \ / _` | ' \  _|
|| \__,_\__,_\__,_|__| .__/_\__,_|_||_\__|
||               |___|_|                  

"""

asciiDel = r"""

 ||    _     _     _               _          _   
 || __| |___| |___| |_ ___    _ __| |__ _ _ _| |_ 
 ||/ _` / -_) / -_)  _/ -_)  | '_ \ / _` | ' \  _|
 ||\__,_\___|_\___|\__\___|__| .__/_\__,_|_||_\__|
 ||                      |___|_|                  

"""

asciiPurch = r"""
                   _                 
||  _ __ _  _ _ _ __| |_  __ _ ___ ___ 
|| | '_ \ || | '_/ _| ' \/ _` (_-</ -_)
|| | .__/\_,_|_| \__|_||_\__,_/__/\___|
|| |_|                                 

"""

asciiNourish = r"""

||                    _    _    
||  _ _  ___ _  _ _ _(_)__| |_  
|| | ' \/ _ \ || | '_| (_-< ' \ 
|| |_||_\___/\_,_|_| |_/__/_||_|                              

"""

#ascii art--------------------------------------------------------------------------------------------------------------------------------  
#import stuff-----------------------------------------------------------------------------------------------------------------------------
import Solmoro_plantS
import Solmoro_fertilizer
import SOLMORO_project

#global stuff
logDict = {}
id_counter = 1


#for the id counter-----------------------------------------------------------------------
def saveCounter(x):
  global id_counter

  try: 
    with open("Logbook_Dictionary.dat", "r") as sLogD: #brings an error if the counter loads with the dat file empty, so check if it has content first
      if sLogD.readline(): #check if the first line in the .dat file exists

        logIds = [x for x in x.keys()]
        lastID = int(logIds[-1][-1])
        print(lastID)
        id_counter = lastID + 1

      else:
        id_counter = 1

  except FileNotFoundError:
    id_counter = 1
#for the id counter-----------------------------------------------------------------------

#logbook menu-----------------------------------------------------------------------------------------------------------------------------

def displayLogMenu():
    print(book_ascii)
    print(logSelection)
    print(catArt)


def LogbookMenu():
  while True:
        displayLogMenu()  # Display logbook menu
        try:
            logChoice = int(input("~Hello! What would you like to view???~ "))
            if logChoice in range(1, 6):
                if not handleLogChoice(logChoice, logDict):
                    break  #exit if the user chooses "Return" (option 6)
            else:
                print("Please select from one of the options (>n<)!")
                time.sleep(1)
        except ValueError:
            print("Please enter a valid number from the choices (>n<)!")
            time.sleep(1)
#logbook menu-----------------------------------------------------------------------------------------------------------------------------

#load logbook----------------------------------------------------------------------------------------------------------------------------
def loadLogbook(x):
    try:
        with open("Logbook_Dictionary.dat", "r") as sLogD: #iterate through lines in the logbook dat file
            for line in sLogD:
                logInfo = line.strip().split(", ") #split them up and reassign
                logId = logInfo[0]
                plantId = logInfo[1]
                fertId = logInfo[2]
                date = logInfo[3]
                action = logInfo[4]

                x[logId] = { #enter into the dictionary
                    "Plant ID": plantId,
                    "Fertilizer ID": fertId,
                    "Date": date,
                    "Action": action
                }
    except FileNotFoundError:
        print(catArt)
        print("There are currently no logged activities! Perhaps it's titme to change that!")
    return x
#load logbook------------------------------------------------------------------------------------------------------------------------------

#initiate
loadLogbook(logDict)
saveCounter(logDict)

#save log entry---------------------------------------------------------------------------------------------------------------------------
def saveLogbook(x):
    with open("Logbook_Dictionary.dat", "w") as sLogD:
        for logId, logInfo in x.items():
            plantId = logInfo["Plant ID"]
            fertId = logInfo["Fertilizer ID"]
            date = logInfo["Date"]
            action = logInfo["Action"]
            sLogD.write(f"{logId}, {plantId}, {fertId}, {date}, {action}\n")
#add log entry----------------------------------------------------------------------------------------------------------------------------
def dateCheck():
    month = input("What month is it? [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec] (+o+) ").strip().lower().capitalize()
    while month not in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
        print(sadCat)
        month = input("Do you need a lesson on the Gregorian Calendar? Please enter a valid month in the given format... (UnU) ")


    #Month conditioning
    if month in ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]: 
        #31 days
        day = int(input("What day of the month is it? [1-31]: "))
        while day not in range(1, 32):  #Day must be between 1 and 31
            print(sadCat)
            day = int(input("Hey! We're on earth... please enter a valid day (1-31): "))
    elif month in ["Apr", "Jun", "Sep", "Nov"]:
        #30 days
        day = int(input("What day of the month is it? [1-30]: "))
        while day not in range(1, 31):  #Day must be between 1 and 30
            print(sadCat)
            day = int(input("Hey! We're on earth... please enter a valid day (1-30): "))
    elif month == "Feb":
        #Only 28 days (no leap year)
        day = int(input("What day of the month is it? [1-28]: "))
        while day not in range(1, 29):  #Day must be between 1 and 28
            print(sadCat)
            day = int(input("Hey! We're on earth... please enter a valid day (1-28): "))

    year = input("~Now, what year is it?~")

    date = f"{str(day)} {month} {year}"
    return date

def addLogEntry(a, plantId, fertId, action):
    global id_counter #access the id counter

    print(catArt)
    print("Logging~~~")
    logDate = dateCheck()

    #generating logbook Ids
    logId = f"L{id_counter}"
    id_counter += 1
    #---------------------------------------------
    #Adding the entry into the dictionary
    a[logId] = {
      "Plant ID": plantId,
      "Fertilizer ID": fertId,
      "Date": logDate,
      "Action": action
    }

#add log entry----------------------------------------------------------------------------------------------------------------------------

#view all--------------------------------------------------------------------------------------------------

def viewAll(x):
    print(catArt)
    print("~ As you wish ~")
    print(catArt)
    print("Servants! Bring in the logbook!")
    time.sleep(1)
    print("hai~")
    time.sleep(1)
    print("hai~")
    time.sleep(1)
    print(viewAllLog)
    columns = r"""
    || ID ||   Plant ID   ||   Fertilizer ID   ||    Date    ||   Action   ||
    =========================================================================
    """
    print(columns)

    for logIds, logInfo in x.items(): #loops through the ids in the dicitionary then loops in the details in them
        print(f"    || {logIds} ||      {logInfo['Plant ID']}      ||       {logInfo['Fertilizer ID']}       || {logInfo['Date']} ||   {logInfo['Action']}   ||")
 
    if not x:
        print(sadCat)
        print("!!-Oh no! There doesn't seem to be anything logged yet!-!!")
        print("--------------------------------------------------------------------")

    time.sleep(3)

#viewall---------------------------------------------------------------------------------------------------


#view transactions per action-----------------------------------------------------------------------------------

def viewTransac(x):
    print(catArt)
    print("|| add_plant || delete_plant || purchase || nourish ||")
    action = input("|| Oh sure sure! Which action transaction would you like to view?").strip().lower()
    while action not in ["add_plant", "delete_plant", "purchase", "nourish"]: #in case the user inputs something else
        action = input("Please please please! Choose something from the options! (>n<)").strip().lower()

    print(f"Looking up the transaction history for {action}...")
    print("~~~")
    time.sleep(1)
    print("~~~")
    time.sleep(1)
    print("~~~")
    time.sleep(1)
    if action == "add_plant": #check the action value and print the specified art for that action
        print(asciiAdd)
    elif action == "delete_plant":
        print(asciiDel)
    elif action == "purchase":
        print(asciiPurch)
    elif action == "nourish":
        print(asciiNourish)
    for logIds, logInfo in x.items(): #iterate through the log dictionary and check if it is the same as the input
        if logInfo["Action"] == action:
            print(f"|| {logIds} || {logInfo['Plant ID']} || {logInfo['Fertilizer ID']} || {logInfo['Date']} ||")

    time.sleep(3)
            
    

#view transactions per action-----------------------------------------------------------------------------------

#resetting data-------------------------------------------------------------------------------------------------
def dataReset(x):
    import Solmoro_plantS
    import Solmoro_fertilizer
    from Solmoro_plantS import plantDict
    from Solmoro_fertilizer import fertDict

    decision = input("Are you sure you would like to do this??? There's no going back... [y/n] ").strip().lower() #confirmation
    while decision not in ["y", "n"]: #in case the user chooses something else
      decision = input("Please answer me properly! This is a serious decision! (UnU) [y/n]")

    if decision == "n":

      print("Whew, going back...")
      time.sleep(1)
      return #go back to the menu

    elif decision == "y":
        print("Ok then... (UnU)")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Deleting all data from all sectors...")
        time.sleep(1)
        print("Cleaning out the storage and the garden...")
        time.sleep(1)
        print("...")
        Solmoro_plantS.plantDict.clear()            #clearing out plant dictionary
        Solmoro_plantS.savePlantDict(plantDict)     #saving the cleared dictionary
        Solmoro_fertilizer.fertDict.clear()         #clearing out fertilizer dictionary
        Solmoro_fertilizer.saveFertDict(fertDict)   #saving the cleared dictionary
        x.clear()                                   #clearing out logbook dictionary
        saveLogbook(x)                              #saving the cleared dictionary
        print(sadCat)
        print("Successfully... cleared out everything...")
        time.sleep(2)
        return x




#resetting data-------------------------------------------------------------------------------------------------

#menu choices
def handleLogChoice(choice, logDict):
    if choice == 1:
        print(catArt)
        print("Don't worry! We'll take care of the log entries! They shall be added as you go on about in the garden! (^v^)")
        time.sleep(2)
    elif choice == 2:
        viewAll(logDict)
    elif choice == 3:
        viewTransac(logDict)
    elif choice == 4:
        dataReset(logDict)
    elif choice == 5:
        print(catArt)
        print("Returning...")
        time.sleep(1)
        print("~~~")
        time.sleep(1)
        return False  #exit the fertilizer menu to return to the main menu
    return True

#References:
#TextArt. (n.d.). Book text art. TextArt. https://textart.sh/topic/book                                                                                       
