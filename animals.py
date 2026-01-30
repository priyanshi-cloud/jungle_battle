import random
options=["lion","elephant","mouse"]
player_score=0
computer_score=0
print("""welcome to the jungle battle 🐘🐭🦁,
In this wild game ,you'll face off against the computer:
-lion roars🦁,
elephant stomps🐘,
mouse sneaks 🐭,
lion kills mouse,
elephant kicks lion,
mouse outsmarts elephant,                        
type your choice wisely or be eaten,
type 'quit' anytime to escape the jungle""")
while True:
    player_choice=input("enter a choice-elephant,mouse,lion\n").lower()
    if player_choice=="quit":
        break
    if player_choice not in options:
        print("invalid choice😓")
        continue
    #let's see computer choice
    computer_choice=random.choice(options)
    print(f'computer choice is {computer_choice}')

    if computer_choice==player_choice:
        print("it's a draw🤦‍♂️")
    elif (player_choice=="lion" and computer_choice=="mouse") or (player_choice=="elephant" and computer_choice=="lion") or(player_choice=="mouse" and computer_choice=="elephant"):
        print("you won👻👻👻")
        player_score+=1
    else:  
        print("computer won 😎")
        computer_score+=1

print("The game is over🐸")
print(f'your score is{player_score}')
print(f"computer's score is {computer_score}")







