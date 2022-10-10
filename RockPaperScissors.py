import random

def rps():
    user = input("What's your choice? 'R' for rock, 'P' for paper, 'S' for scissors\n").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (f'It\'s a tie, the computer also chose {computer}!')

    if win(user, computer):
        return (f'You won! The computer chose {computer}')

    return (f"You lost! The computer chose {computer}") 
# remember the rules
# rock > scissors, scissors > paper, paper > rock

def win(player, opponent):
    # returns true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True 

print(rps())