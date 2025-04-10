import random

stages= ['''

  ---------
  |       |
  |
  |
  |
  |
  ---------
  ''',

  '''
  ---------
  |       |
  |       O
  |
  |
  |
  ---------
  ''',
  '''
  ---------
  |       |
  |       O
  |       |
  |
  |

  ''',
  '''
  ---------
  |       |
  |       O
  |       /| \\
  |
  |
  ---------
  ''',
  '''
  ---------
  |       |
  |       O
  |      /|\\
  |       /
  |
  ---------
  
  ''',
  '''
  ---------
  |       |
  |       O
  |      /|\\
  |       / \\
  |
  ---------
  '''
  ]
words=['apple','banana','grapes','orange','kiwi','mango','peach','pear']

choosen_words=random.choice(words)
word_display =['_' for _ in choosen_words]
guess_letters=[]
lives=len(stages)-1

print("welcome to Hangman!")
print("Guess the  fruits word.")

while True:
    print(" " .join(word_display))
    guess=input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess)!=1:
        print("please enter a valid letter.\n")
        continue

    if guess in guess_letters:
        print("You already guessed that letter.Try again.\n")
        continue

    guess_letters.append(guess)

    if guess in choosen_words:
        print(f"Good Guess! '{guess}' is in the word.")
        for index,letter in enumerate(choosen_words):
            if letter == guess:
                word_display[index] =guess
    else:
        print(f"Sorry,'{guess}' is not in the word.")
        print(stages[len(stages) - lives -1 ])
        lives -= 1
        print(f"you have {lives} lives left")

        if lives == 0:
            print(stages[lives])
            print(f"you lose!The word was '{choosen_words}' .")
            break