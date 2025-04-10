import random

choices=["rock" , "paper", "scissor"]
user_score=computer_score = 0
print("Lets Play! ")

while True:
    user_input=input("Type Rock,Paper,Scissor or Q to quit: ").lower()
    if user_input == 'q':
        print(f'Final score -you:{user_score},computer:{computer_score}')
        print("Thanks for playing")
        break
    if user_input not in choices:
        print("Invalid input, please try again.")
        continue
    computer_chose =random.choice(choices)
    print(f'computer chose {computer_chose}')
    if user_input == computer_chose:
        print("It is a tie!")

    elif (user_input== "rock" and computer_chose == "scissor") or \
          (user_input == "paper" and computer_chose == "rock") or\
          (user_input == "scissor" and computer_chose == "paper"):
        print("You win")
        user_score +=1

    else:
        print("computer Wins!")
        computer_score =+ 1

    print(f'currently score - you :{user_score},computer:{computer_score}')