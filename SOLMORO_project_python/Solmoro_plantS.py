#Kriztian Mer J. Solmoro
#G-6L
#Description: This will serve as the file for the plant section of the project

import time

#Ascii art stuff----------------------------------------------------------------
flower_row = r"""

								

                         wWWWw               wWWWw
                   vVVVv (___) wWWWw         (___)  vVVVv
                   (___)  ~Y~  (___)  vVVVv   ~Y~   (___)
                    ~Y~   \|    ~Y~   (___)    |/    ~Y~
                    \|   \ |/   \| /  \~Y~/   \|    \ |/
                   \\|// \\|// \\|/// \\|//  \\|// \\\|///
	=============== ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ===============
"""

catArt = r"""
 /\_/\  
( o.o ) @~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@
 > ^ <
 """

PlantSelection = """
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
+---------+  +---------+  +---------+  +---------+  +---------+  +---------+  +---------+
|   (1)   |  |   (2)   |  |   (3)   |  |   (4)   |  |   (5)   |  |   (6)   |  |   (7)   |
|         |  |         |  |         |  |         |  | Update  |  |         |  |         |
|  Add a  |  |Remove a |  | View a  |  | Modify  |  |Nourish- |  | Nourish |  |  Main   |
|  Plant  |  |   Plant |  |   Plant |  |  Plant  |  |   ment  |  |  Plant  |  |  Menu   |
+---------+  +---------+  +---------+  +---------+  +---------+  +---------+  +---------+
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

"""

plant_ascii = r"""
                          ____   _                _
                         |  _ \ | |  __ _  _ __  | |_  ___
                         | |_) || | / _` || '_ \ | __|/ __|
                         |  __/ | || (_| || | | || |_ \__ \
                         |_|    |_| \__,_||_| |_| \__||___/


"""
sadCat = r"""
 /\_/\  
( u.u )  -------------------------------------------------------------
 > ^ <
"""

viewFlower = r"""
==========================
|| __.=./\ / \ /\.=.__  ||
||(-.'-;  |   |  ;-'.-) || 
||   \ `\/     \/` /    ||
||    ;  `\   /`  ;     ||
||    |    | |    |     ||
||    ;,"-.-"-.-",;     ||
||     \\/^\ /^\//      ||
||      \   `   /       ||
||       ',___,'        ||
||        \\V//         ||
||         |||          ||
||         |||          ||
||         |||          ||
||      Art By jgs      ||
==========================
"""

#Ascii art stuff-----------------------------------------------------------------



#the plant dictionary
plantDict = {}
id_counter = 1 #counter for the unique plant id

#for the id counter------------------------------------------------------------------------------------
def saveCounter(x):
	global id_counter

	try: 
		with open("Plant_Dictionary.dat", "r") as sPlantD: #brings an error if the counter loads with the dat file empty, so check if it has content first
			if sPlantD.readline(): #check if the first line in the .dat file exists

				plantIds = [x for x in x.keys()] #create a list of all the plant ids
				lastID = int(plantIds[-1][-1]) #get the number of the last plant id
				id_counter = lastID + 1 #assign it plus 1

			else:
				id_counter = 1

	except FileNotFoundError:
		id_counter = 1


#for the id counter------------------------------------------------------------------------------------

#plant menu------------------------------------------------------------------------------------------

def displayPlantMenu():
		print(flower_row)
		print(plant_ascii)
		print(PlantSelection)
		print(catArt)

def plantMenu():
	#choosing process
	while True:
				displayPlantMenu()  #call the display plant menu
				try:
						plantChoice = int(input("How may we be of assistance? "))
						if plantChoice in range(1, 8):
								if not handlePlantChoice(plantChoice, plantDict):
										break  #exit if the user chooses "Return" (option 7)
						else:
								print("Please select from one of the options (>n<)!")
								time.sleep(1)
				except ValueError:
						print("Please enter a valid number from the choices (>n<)!")
						time.sleep(1)
#plant menu---------------------------------------------------------------------------------------------


#save the plant to the file----------------------------------------------------------------------------
def savePlantDict(x):
		with open("Plant_Dictionary.dat", "w") as sPlantD: #opens the separate file
			for plantId, plantInfo in x.items(): #iterates over the dictionaries and assigns their values for thus function's scope (learned the hard way)
				pName = plantInfo["Plant Name"]
				pStor = plantInfo["Plant Storage"]
				pNourish = ", ".join(f"{key}: {value}" for key, value in plantInfo["Plant Nourishment"].items()) #iterates over every info in the plant nourishment dictionary and joins them with "," as a string to be written into the dat file
				sPlantD.write(f"{plantId}, {pName}, {pStor}, {pNourish}\n")  #save the plant data in the dat file itself
#save the plant to the file----------------------------------------------------------------------------

#load the plant file------------------------------------------------------------------------------------
def loadPlantDict(x):
	try:
		with open("Plant_Dictionary.dat", "r") as sPlantD:
			for line in sPlantD:
				plantInfo = line.strip().split(", ")
				plantId = plantInfo[0]
				pName = plantInfo[1]
				pStor = plantInfo[2]
				print(plantInfo)
				pNourish = {} #for plant nourishment
				for nourishVal in plantInfo[3:]: #for every index starting from 3
					fert, amount = nourishVal.split(": ") #split the entries using a colon and then convert them into a dictionary
					pNourish[fert] = int(amount)

				#enter them into the dictionary
				x[plantId] = {
					"Plant Name": pName,
					"Plant Storage": pStor,
					"Plant Nourishment": pNourish
					}
	except FileNotFoundError:
			print(catArt)
			print("~ The garden is currently empty... time to start planting!!! ~")
#load the plant file------------------------------------------------------------------------------------

loadPlantDict(plantDict) #load the file into the dictionary


saveCounter(plantDict) #the id values follow suit

#addplant----------------------------------------------------------------------------------------
def addPlant(x): #adding the plant
	print(catArt)
	global id_counter #to access the counter, had no choice but to resort to global as the

	while True: #loop in case the user wants to add multiple plants without going back to the menu
		pName = str(input("What is the name of the plant? ")).lower().capitalize()
		pNourish = {}

		#check for the required storage values------
		pStor = str(input("How should the plant be stored? [INDOOR/OUTDOOR] ")).strip().upper() #for case sensitivity
		while pStor not in ["INDOOR", "OUTDOOR"]:
			print("I'm sorry! That won't be possible, please choose from the prescribed options UwU")
			pStor = str(input("How should the plant be stored? [INDOOR/OUTDOOR] ")).strip().upper()
		#---------------------------------------------

		#generating plant Ids
		plantId = f"P{id_counter}"
		id_counter += 1
		#---------------------------------------------

		#Adding the entry into the dictionary
		x[plantId] = {
			"Plant Name": pName,
			"Plant Storage": pStor,
			"Plant Nourishment": pNourish
		}


		#saves the plants into the file
		savePlantDict(plantDict)

		#---------------log-------------------------
		from Solmoro_Logbook import addLogEntry
		from Solmoro_Logbook import logDict
		from Solmoro_Logbook import saveLogbook

		action = "add_plant"
		fertId = "NA"

		addLogEntry(logDict, plantId, fertId, action)
		saveLogbook(logDict)
		print("~Successfully logged!~")

		#---------------log-------------------------


		print(f"Awesome (>w<)! The new plant {pName} has joined the garden!")

		#asks if you want another plant
		print (catArt)
		newPlant = input("Would you like to add another plant (OwO)? [y/n] ").strip().lower()
		while newPlant not in ["y", "n"]: #in case the user chooses something else
			newPlant = input("Please answer me properly! (UnU) [y/n]")

		if newPlant == "n":

			print("Ok!")
			break #go back to the main menu
	 
#addPlant--------------------------------------------------------------------------------------

#remove the plant-------------------------------------------------------------------------------
def removePlant(x):
	print(catArt)
	toRemove = str(input("Oh no! Which plant would you like to remove? Please enter its ID! ")).strip().upper()

	if toRemove in x: #check if it is in the dictionary
		print(sadCat)
		print(f"{x[toRemove]['Plant Name']} has been removed... UnU")
		x.pop(toRemove)
		savePlantDict(plantDict) #save the updated plantDict into the separate file

		loadPlantDict(plantDict) #load the file into the dictionary
		saveCounter(plantDict) #so that the id will save even if a plant is removed

		#---------------log-------------------------
		from Solmoro_Logbook import addLogEntry
		from Solmoro_Logbook import logDict
		from Solmoro_Logbook import saveLogbook

		action = "delete_plant"
		fertId = "NA"

		addLogEntry(logDict, toRemove, fertId, action)
		saveLogbook(logDict)
		print("~Successfully logged!~")

		#---------------log-------------------------
		time.sleep(3)


	else:
		print(f"Sorry, there is no plant with the ID {toRemove} in the garden!")
		time.sleep(3)

	return x
#removePlant--------------------------------------------------------------------------------------  

#viewPlant--------------------------------------------------------------------------------------
def viewPlant(x):
	print(catArt)
	toView = input("What is the name of the plant that you would like to view?").strip().lower()
	print("==============================================================================")

	foundPlant = False #checker

	for plantIds, plantInfo in x.items(): #iterates through the dictionaries within the dictionary
		if plantInfo["Plant Name"].lower() == toView: #checks if the plant name is in the dictionary
			foundPlant = True
			#the actual display
			print(catArt)
			print("We found the plant! UwU")
			print(viewFlower)
			print(f"||Plant ID: {plantIds}")
			print(f"||Plant Name: {plantInfo['Plant Name']}")
			print(f"||Storage: {plantInfo['Plant Storage']}")
			print(f"||Nourishment: {plantInfo['Plant Nourishment']}")
			time.sleep(3)
			return

	if not foundPlant: #if the plant name is not in the dictionary
			print(sadCat)
			print(f"My apologies, we did not find any plant named {toView} in the garden...")
			time.sleep(5)
#viewPlant-------------------------------------------------------------------------------------------

#editPlant----------------------------------------------------------------------------------------
def editPlant(x):
	print(catArt)
	toEdit = input("Oh, please enter the ID of the plant you wish to modify!").upper()
	print("====================================================================================")

	#user inputs
	if toEdit in x.keys():
		newName = str(input("What would the new name of the plant be?")).strip() 

		newStorage = input("How would you store it? [INDOOR/OUTDOOR]").strip().upper() #for case sensitivity
		while newStorage not in ["INDOOR", "OUTDOOR"]: #if the user entered anoher value
			newStorage = input("I'm sorry, please choose only from the two options! [INDOOR, OUTDOOR]").strip().upper()

		#editing the dictionary
		x[toEdit]["Plant Name"] = newName
		x[toEdit]["Plant Storage"] = newStorage

		#save the changes to the separate file
		savePlantDict(plantDict)

		#show changes
		print(catArt)
		print(f"Plant {toEdit} has been successfully edited! The new details are:")
		print(f"| Plant ID: {toEdit} | Plant Name: {x[toEdit]['Plant Name']} | Storage: {x[toEdit]['Plant Storage']} |")
		print("=====================================================================================")
		time.sleep(3)

	else:
		print(sadCat)
		print(f"Oh no! There are no plants with the Plant ID {toEdit} in the garden!")
		time.sleep(2)
#editPlant--------------------------------------------------------------------------------------

#updateNourishment------------------------------------------------------------------------------------
def updateNourishment(x):
	print(catArt)
	toUd = input("OwO ~Please enter the plant name for which you would like to modify the information for nourishment~ OwO ").strip().lower()

	#checker if the plant is found
	foundPlant = False

	for plantIds, plantInfo in x.items(): #iterates through the dictionaries within the dictionary
		if plantInfo["Plant Name"].lower() == toUd: #checks if the plant name matches
			foundPlant = True #update it to true

			print(catArt)
			plantNrsh = str(input("What is the name of the fertilizer? ")).strip().lower().capitalize()

			while True: 
				try:
					nrshAmount = float(input("What is the needed amount?"))
					if nrshAmount <= 0: #we can't have negative fertilizers can we
						print("Please enter a valid amount (>n<) ! [Positive number]")
					else:
						break
				except ValueError: #if the user enters something that results in an error for int function
					print("Please enter a valid number for fertilizer amount (>n<)! [Positive number!")

			#nourishment assignment
			plantInfo["Plant Nourishment"][plantNrsh] = nrshAmount

			#saves the nourishment to the separate file
			savePlantDict(plantDict)

			#show changes
			print(catArt)
			print(f"Plant {toUd} has been successfully edited! The new details are:")
			print(f"| Plant Name: {plantInfo['Plant Name']} | Fertilizer Name: {plantNrsh} | Amount: {nrshAmount}")
			print("=====================================================================================")
			time.sleep(3)
			return

	if not foundPlant: #if the plant is not found, alert the user
		print(f"Oh gosh golly (0o0)! There are no plants named {toUd} in the garden!")
		time.sleep(3)
#updateNourishment------------------------------------------------------------------------------------

#Nourishing the plant---------------------------------------------------------------------------------

def nourishPlant(x):
	#import the fertilizer dictionary
	from Solmoro_fertilizer import fertDict
	from Solmoro_fertilizer import saveFertDict


	print(catArt)
	toNourish = input("0w0 Please enter the name of the plant that you would like to nourish 0w0 ").strip().lower()

	#checker if plant is found
	plantFound = False

	for plantIds, plantInfo in x.items(): #iterates through the dictionaries within the dictionary
		if plantInfo["Plant Name"].lower() == toNourish: #checks if the plant name matches
				plantFound = True
				if not plantInfo["Plant Nourishment"]:
					print("sadCat")
					print("Ooops, this plant has no nourishment requirements yet!!! (0o0)")
					time.sleep(3)
					return
		 
				#get the nourishment information in the plant nourishment dictionary
				for reqFert, reqAm in plantInfo["Plant Nourishment"].items():
					print(catArt)
					print(f"Getting the materials to nourish the {plantInfo['Plant Name']}~ Looking for: {reqFert}")
					time.sleep(1)
					print("---")
					time.sleep(1)
					print("---")
					time.sleep(1)

					fertFound = False #for the fertilizer

					for fertIds, fertInfo in fertDict.items(): #loop through fertilizer dictionary
						if fertInfo["Fertilizer Name"].lower() == reqFert.lower(): #checks if the fertilizer name matches the one in plant nourishment
							#compare the amounts and subtract if valid
							if fertInfo["Amount"] >= reqAm:
								fertInfo["Amount"] -= reqAm
								fertFound = True

								print(catArt)
								print(viewFlower)
								print(f"{plantInfo['Plant Name']} thanks you for the nourishment of {reqFert}!")
								print(f"There are currently {fertInfo['Amount']} units of {reqFert} left in the storage...")
								time.sleep(3)
								saveFertDict(fertDict) #save the subtracted amount to the .dat file

								#---------------log-------------------------
								from Solmoro_Logbook import addLogEntry
								from Solmoro_Logbook import logDict
								from Solmoro_Logbook import saveLogbook

								action = "nourish"

								addLogEntry(logDict, plantIds, fertIds, action)
								saveLogbook(logDict)
								print("~Successfully logged!~")

								#---------------log-------------------------


							else:
								print(sadCat)
								print(f"!! Oh no! There aren't enough {reqFert} in the storage to nourish {plantInfo['Plant Name']}! (UnU) !!")
								time.sleep(2)
								return

					if not fertFound:
						print(sadCat)
						print(f"There are no {reqFert} units in the fertilizer storage...")
						time.sleep(2)
						return

				#if all fertilizer requirements were met, mark nourishment as complete
				print(catArt)
				print(f"Supercalifragilistic Expialidocious (>w<)!! {plantInfo['Plant Name']} has been successfully nourrished!! ")



	if not plantFound:
		print(sadCat)
		print(f"My apologies, it seems there are no plants named {toNourish} in the garden...")
		time.sleep(3)

#Nourishing the plant---------------------------------------------------------------------------------



#the main menu stuff
def handlePlantChoice(choice, plantDict):
		# Depending on the choice, call the relevant plant function
		if choice == 1:
				addPlant(plantDict)  #function to add a plant
		elif choice == 2:
				removePlant(plantDict)  #function to remove a plant
		elif choice == 3:
				viewPlant(plantDict)  #function to view a plant
		elif choice == 4:
				editPlant(plantDict)  #function to edit a plant
		elif choice == 5:
				updateNourishment(plantDict)  #function to update nourishment
		elif choice == 6:
				nourishPlant(plantDict)  #function to nourish a plant
		elif choice == 7:
				print(catArt)
				print("Returning...")
				time.sleep(1)
				print("~~~")
				time.sleep(1)
				return False  #exit the plant menu to return to the main menu
		return True




#References:
#OpenAI. (2024). ChatGPT (Version 4). Retrieved from https://chat.openai.com
#Stark, J. G.: (n.d.). ASCII flower. ASCII Art Copy. Retrieved November 11, 2024, from https://www.asciiartcopy.com/ascii-flower.html
#W3Schools. (n.d.). Python tutorial. W3Schools. Retrieved November 27, 2024, from https://www.w3schools.com/python/


