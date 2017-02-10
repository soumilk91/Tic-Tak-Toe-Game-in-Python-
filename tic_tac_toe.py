import sys 

board = ['1','2','3','4','5','6','7','8','9']
position_index_mapping = {'1':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8}
winning_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
player_identifier_dict = {}
def is_anyone_winning():
	for i in winning_combinations:
		x_count = 0
		for j in i:
			if (board[j] == 'X'):
				x_count += 1
		if x_count == 3:
			print_board()
			print "\nPlayer with identifier 'X' wins the Game !!!!!!  "
			return True
		o_count = 0
		for j in i:
			if (board[j] == 'O'):
				o_count += 1
		if o_count == 3:
			print_board()
			print "\nPlayer with identifier 'O' wins the Game !!!!!! "
			return True
	return False

def get_player_identifiers():
	player_1 = ''
	player_2 = ''
	print "Enter Player 1 Identifier :-"
	while(1):
		identifier = raw_input("Input you selection ('X' OR 'O') : ")
		identifier = identifier.upper()
		if ((identifier=='X') or (identifier=='O')):
			if (player_1=='' and player_2==''):
				player_1 = identifier
				player_identifier_dict["player_1"]  = player_1
				break
		else:
			print "Wrong Selection. You must select either 'X' or 'O'"
	print "Enter Player 2 Identifier :-"
	while(1):

		identifier = raw_input("Input you selection ('X' OR 'O') : ")
		identifier = identifier.upper()
		if ((identifier =='X') or (identifier =='O')):
			if (player_1!='' and player_2==''):
				if player_1 == identifier:
					print "Both Players cannot select one identifier !!"
				else:
					player_2 = identifier
					player_identifier_dict["player_2"] = player_2
					break
		else:
			print "Wrong Selection. You must select either 'X' or 'O'"

def print_board():
	print "\n The Current condition of the Game is :"
	print "| %s | %s | %s |"%(board[0], board[1], board[2])
	print "| %s | %s | %s |"%(board[3], board[4], board[5])
	print "| %s | %s | %s |"%(board[6], board[7], board[8])
	print "Player 1 Identifier : %s"%player_identifier_dict["player_1"]
	print "Player 2 Identifier : %s"%player_identifier_dict["player_2"]


def play_the_game():
	get_player_identifiers()
	print_board()
	for i in range (9):
		if (i%2 == 0):
			print "\nPlayer 1, your move : "
			while (1):
				inp = raw_input("Enter the Positon you want to place your identifier on: ")
				if inp not in position_index_mapping:
					print "You must Enter a number in the range 1-9 both inclusive..... Please Try Again "
				else:
					if ((board[position_index_mapping[inp]] == "X") or (board[position_index_mapping[inp]] == "O")):
						print "That posoiton is already filled, Please Try Again"
					else:
						board[position_index_mapping[inp]] = player_identifier_dict["player_1"]
						print_board()
						break
			if (is_anyone_winning()):
				print "PLAYER 1 : CONGRATS !!!!! YOU HAVE WON THIS GAME ......"
				break

		else:
			print "\nPlayer 2, your move : "
			while(1):
				inp = raw_input("Enter the position you want to place your identifier on: ")
				if inp not in position_index_mapping:
					print "You must Enter a number in the range 1-9 both inclusive..... Please Try Again "
				else:
					if ((board[position_index_mapping[inp]] == "X") or board[position_index_mapping[inp]] == "O"):
						print "This Position is already filled, Please Try Again "
					else:
						board[position_index_mapping[inp]] = player_identifier_dict["player_2"]
						print_board()
						break
			if (is_anyone_winning()):
				print "PLAYER 2 : CONGRATS !!!!! YOU HAVE WON THIS GAME ....."
				break

while_variable = 0
while (while_variable==0):
	play_the_game()		
	decision = raw_input("Do you want to play again ??? (y/n)")
	allowed_answers = ['y', 'Y', 'n', 'N']
	while(1):
		if decision in allowed_answers:
			if ((decision == 'y') or decision == 'Y'):
				print "\nLETS PLAY AGAIN ....."
				board = ['1','2','3','4','5','6','7','8','9']
				break
			else:
				print "Thank you for playing !!!! Have a great day !!!"
				while_variable = 1
				break







