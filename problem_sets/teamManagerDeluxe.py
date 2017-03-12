# This sets a class so that it can be used later in the code.
class Player(object):
	def __init__(self, name, age, goals, jersey, position):
		self.name = name
    		self.age = age
    		self.goals = goals
    		self.jersey = jersey
    		self.position = position
    		# This makes it so that there can be a stats.
  	def getPlayerSummary(self):
    		Stats = "Player: " + self.name + "\n"
    		Stats = Stats + "Age: " + self.age + "\n"
    		Stats = Stats + "Goals: " + self.goals + "\n"
    		Stats = Stats + "Jersey Number:" + self.jersey + "\n"
   		Stats = Stats + "Position:" + self.position + "\n" 
		return Stats
#This function lets the user save their players.
def saveTeam(playerList, filename):
	file = open(filename + '.tmd', "a")
	for long in players:
		file.write(long.name + " " + str(long.age)+ " " + str(long.goals)+ " "  + str(long.jersey)+ " " + str(long.position))
	file.close()
#This function lets the user load platers from a different file.
def loadTeam(filename):
	players = []
	file = open(filename, "r")
	whoops = file.readline()
	while whoops != "":
		wow = whoops.split()
		players.append(Player(wow[0], wow[1], wow[2], wow[3], wow[4]))
		whoops = file.readline()	
		file.close()
	return players

print('Welcome to Team Manager Deluxe!')
print('Do you want to start with an new team or an existing team?')
print("Enter the number of your choice and press 'Enter'.")
print('(1): Start with a new team')
print('(2): Open a file of an exisiting team.')
choice = raw_input()
if choice == "1":
        pass
elif choice == "2":
        print("What's the filename for your existing team? Enter the whole name, including its .tmd extension.")
        filename = raw_input()
        players = loadTeam(filename)

# Lets it so the program can add players.
players = []

run = True
# the user can use pick from any of the choices below.
while run:
	print("What would you like to do? Enter the number of your choice and press 'Enter'.")
  	print('(1): Add players.')
  	print('(2): View players information.')
	print('(3): Save your players to a file.')
  	print('(0): Exit from teamManager.(Do not forget to save before exiting).')
  
    		# this is for the user to input their response.
  	response = raw_input()
  
  	if response == "0":
    		run = False
      		#Due to their selection they will brought to a different option.
		#This option lets the user input different information about specific players.
  	elif response == "1":
    		print('What is the name of the player?')
    		playersName = raw_input()
    		print('What is the age of the player?')
    		playersAge = raw_input()
    		print('How many goals have they made?')
    		playersGoals = raw_input()
    		print('What is the players jersey number?')
    		playerJersey = raw_input()
    		print('What is the players position?')
    		playerPosition = raw_input()

    		team = Player(playersName, playersAge, playersGoals, playerJersey, playerPosition)
    		players.append(team)
    
   		print('Okay! We go it, now it will appear in the list when you run it again.')
    		#This lets the user see the team players.
  	elif response == "2":
    		for p in players:
      			print(p.getPlayerSummary())
		#Once, the user inputs 3, they wil be directed to the save the players. 
	elif response == "3":
		print('What do you wish to call your file?')
		filename = raw_input()
		saveTeam(players, filename)
		print('Great! You may now exit Team Manager Deluxe or add more players.')
