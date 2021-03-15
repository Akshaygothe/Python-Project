import random

def play():
    user = input("Enter your Choice:")
    if user == 'e':
        return 'exit'
    computer = random.choice(['r','p','s'])
    #print(computer)
    
    if user == computer:
        return "It's a Tie"
    #print('p')
    
    if is_win(user, computer):
        return ('You Won!')
    
    return ('You Lost!')
    
def is_win(player, opponent):
    #return True if player is win
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

if __name__ == "__main__":
    while True:
        print("\t Game: Rock Paper Scissors!")
        print("\t Enter your choice:\n\t 'r' for Rock. \n\t 'p' For Paper. \n\t 's' For Scissors. \n\t 'e' For Exit from Game.")
        message = play()
        if message == 'exit':
            print('You Exit The Game!')
            break
        print(message)