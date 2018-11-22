print("Rock...")
print("Paper...")
print("Scissors...")


player1 = input("Player 1, make your move: ")

player2 = input("Player 2, make your move: ")


# if player1 == "paper" and player2 == "rock":
# 	print("SHOOT!")
# 	print("Player 1 wins!")
# elif player1 == "scissors" and player2 == "rock":
# 	print("SHOOT!")
# 	print("Player 2 wins!")
# elif player1 == "rock" and player2 == "paper":
# 	print("SHOOT!")
# 	print("Player 2 wins!")
# elif player1 == "scissors" and player2 == "paper":
# 	print("SHOOT!")
# 	print("Player 1 wins!")
# elif player1 == "rock" and player2 == "scissors":
# 	print("SHOOT!")
# 	print("Player 1 wins!")
# elif player1 == "paper" and player2 == "scissors":
# 	print("SHOOT!")
# 	print("Player 2 wins!")
# elif player1 == player2:
# 	print("SHOOT!")
# 	print("It's a tie!")
# else:
# 	print("Something went wrong")


if player1 == player2:
	print("It's a tie!")
elif player1 == "paper": 
	if player2 == "rock":
		print("Player 1 wins!")
	elif player2 == "scissors":
		print("Player 2 wins!")
elif player1 == "scissors": 
	if player2 == "paper":
		print("Player 1 wins!")
	elif player2 == "rock":
		print("Player 2 wins!")
elif player1 == "rock":
	if player2 == "scissors":
		print("Player 1 wins!")
	elif player2 == "paper":
		print("Player 2 wins!")
else:
	print("Something went wrong")



p1 = input("Player 1: rock, paper, or scissors ")
p2 = input("Player 2: rock, paper, or scissors ")
 
if p1 == p2:
    print("Draw")
elif p1 == "rock" and p2 == "scissors":
    print("p1 wins")
elif p1 == "paper" and p2 == "rock":
    print("p1 wins")
elif p1 == "scissors" and p2 == "paper":
    print("p1 wins")
else:
    print("p2 wins")



############ CODE FOR HUMAN VS COMPUTER RPS ############

import random

print("Rock...")
print("Paper...")
print("Scissors...")


player = input("Player, make your move: ").lowercase()
rand_num = random.randint(0,2)
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
	else:
		print("Computer wins!")
elif player == "scissors": 
	if computer == "paper":
		print("Player wins!")
	else:
		print("Computer wins!")
elif player == "rock":
	if computer == "scissors":
		print("Player wins!")
	else:
		print("Computer wins!")
else:
	print("Something went wrong")