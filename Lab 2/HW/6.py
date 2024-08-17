import random

def playRockPaperScissors(rounds):
    player_score = 0
    comp_score = 0

    for i in range(rounds):
        player = input("")
        computer = random.choice(["rock","paper","scissor"])
        print(f"Computer: {computer}")

        if player == computer:
            continue
        elif (
            (player == "rock" and computer == "scissor") or 
            (player == "paper" and computer == "rock") or 
            (player == "scissor" and computer == "paper")
        ):
            player_score += 1
        else:
            comp_score += 1

    return player_score, comp_score

round = int(input(""))
player,computer = playRockPaperScissors(round)
print(f"Your Score: {player}")
print(f"Computer's Score: {computer}")

if player > computer:
    print("You have won the game!")
elif player == computer:
    print("The game is a tie!")
else:
    print("Computer has won the game!")