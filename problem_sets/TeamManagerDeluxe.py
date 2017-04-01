# This sets a class so that it can be used later in the code.
class Player(object):
	def __init__(self, name, age, goals, jersey_number, position):
		self.name = name
		self.age = age
		self.goals = goals
		self.jersey_number = jersey_number
		self.position = position
		# This makes it so that there can be a stats.
	def getPlayerSummary(self):
		print("\n")
		print("Name: " + self.name)
		print("Age: " + str(self.age))
		print("Goals: " + str(self.goals))
		print("Jersey Number: " + str(self.jersey_number))
		print("Position: " + str(self.position))
		print("\n")

#This function lets the user save their players.
def saveTeam(playerList, filename):
	my_file = open(filename + '.tmd', 'w')
	for p in playerList:
		my_file.write(p.name + ' ' 
				+ str(p.age) + ' '
				+ str(p.goals) + ' '
				+ str(p.jersey_number) + ' '
				+ p.position + '\n')
	my_file.close()
#This function lets the user load platers from a different file.
def loadTeam(filename):
	my_players = []
	my_file = open(filename, 'r')
	line = my_file.readline()
	while line:
		player = line.split()
		my_players.append(Player(player[0],
			player[1],
			player[2],
			player[3],
			player[4]))
		line = my_file.readline()
	my_file.close()
	return my_players
print("Welcome to Team Manager Deluxe!")
print("Do you want to start with a new team or an existing team?")
print("Enter the number of your choice and press 'Enter'.")
print("(1) Start with a new team")
print("(2) Open a file for an existing team")
choice = int(raw_input())

if choice == 2:
	print("What's the filename for your existing team? Enter the whole name, including its .tmd extension.")
	filename = raw_input()
	players = loadTeam(filename)
	# Lets it so the program can add players.
else:	
	players = []
# the user can use pick from any of the choices below.
while choice != 0:
	print("What do you want to do? Enter the number of your choice and press Enter.")
	print("(1): Add a player")
	print("(2): View player information.")
	print("(3): Save your players to a file.")
	print("(0): Exit from Team Manager Deluxe. (Don't forget to save before exiting!)")
		# this is for the user to input their response.
	choice = int(raw_input())
	#Due to their selection they will brought to a different option.
	#This option lets the user input different information about specific players.
	if choice == 1:
		print("Enter name:")
		player_name = raw_input()
		print("Enter age:")
		player_age = int(raw_input())
		print("Enter number of goals scored this season:")
		player_goals = int(raw_input())
		print("Enter the jersey number worn by this player:")
		jersey_num = int(raw_input())
		print("Enter the position that this player plays:")
		position = raw_input()
		players.append(Player(player_name, player_age, player_goals, jersey_num, position))
		print("Okay! We got it,now it will appear in the list when you run it again.")

	# if the user wants to print the players, call printStats for each Player
	if choice == 2:
		for player in players:
			player.getPlayerSummary()
			#This lets the user see the team players.
			#Once, the user inputs 3, they wil be directed to the save the players. 
	if choice == 3:
		print("Ok, what would you like to name the file? We'll add on a .tmd file extension to whatever you enter.")
		filename = raw_input()
		saveTeam(players, filename)
