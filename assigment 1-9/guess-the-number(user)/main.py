import random

print("Welcome to the guessing number game! ")

secret_number=random.randint(1,10)
print("I have secret number between 1 and 10.can you guess it: ")

while True:
    try:
        guess=int(input("Enter Your guess: "))
        if guess > secret_number:
            print("Too hihg ! Try agian,")
        elif guess < secret_number:
            print("Too low ! gtry agian,")
        else:
            print("congatulations ! You have guessed the number!")
            break
    except ValueError:
        print('Invalid input.please enter a number between 1 and 10')
