
############ CODE FOR HUMAN VS COMPUTER RPS ############

from random import randint
player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score:
	print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
	print("Rock...")
	print("Paper...")
	print("Scissors...")

	player = input("Player, make your move: ").lower()
	if player == "quit" or player == "q":
		break
	rand_num = randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"
	print(f"Computer plays {computer}")

	if player == computer:
		print("It's a tie!")
	elif player == "paper": 
		if computer == "rock":
			print("Player wins!")
			player_wins += 1
		else:
			print("Computer wins!")
			computer_wins += 1
	elif player == "scissors": 
		if computer == "paper":
			print("Player wins!")
			player_wins += 1
		else:
			print("Computer wins!")
			computer_wins += 1
	elif player == "rock":
		if computer == "scissors":
			print("Player wins!")
			player_wins += 1
		else:
			print("Computer wins!")
			computer_wins += 1
	else:
		print("Something went wrong")
if player_wins > computer_wins:
	print("Congrats, you won!!")
elif player_wins == computer_wins:
	print("It's a tie!")
else:
	print("Oh no, the computer won...")
