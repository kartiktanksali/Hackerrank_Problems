#Rock PAper scissors 
import random

ch1 = input("Player 1 Enter Rock or Paper or Scissor ")
rn = random.randint(1,3)

if(rn==1):
	ch2 = "rock"
elif(rn==2):
	ch2 = "paper"
else:
	ch2 = "scissor"

print("Computer plays " + ch2)

if(ch1=="rock" and ch2=="scissor"):
	print("Player 1 wins")
elif(ch1=="scissor" and ch2=="paper"):
	print("Player 1 wins")
elif(ch1=="paper" and ch2=="rock"):
	print("Player 1 wins")
elif(ch1==ch2):
	print("Match Draw")
else:
	print("Player 2 wins")
