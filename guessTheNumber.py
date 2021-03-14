import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess The Number Between 1 and {x}: '))
        if guess < random_number:
            print("Sorry, Guess again. Too Low.")
        elif guess > random_number:
            print("Sorry, Guess again. Too High")
    print(f'yay, Congrats. You have guessed the number {random_number} correctly.')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(f'Is {guess}, To High (H), To Low (L), or Correct (C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay, I(computer) Guess your number {guess} correctly!!')
    
if __name__ == "__main__":
    while True:
        print('\t Guess The Number Game')
        print('\t Choose The Game:')
        print('\t 1. User Is Guessing The Number.\n\t 2. Computer Is Guessing The Number.\n\t 3. Exit Game.')
        num = int(input('Enter Your Choise:'))
        if num == 1:
            x = int(input('Enter the Max Limit of range:'))
            guess(x)
        elif num == 2:
            x = int(input('Enter the Max Limit of range:'))
            computer_guess(x)
        else:
            print('You are exit the Game.')
            break