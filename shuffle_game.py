'''
SHUFFLE_GAME_SCRIPT
'''
from random import shuffle
### Ask the player if he wants to start the game ###
def ask_to_start():
    q_1 = True
    while q_1:
        answer = input('Do you want to start the game? (YES or NO): ')
        if answer == 'NO':
            print('Thank you for playing!')
            q_1 = False
        elif answer == 'YES':
            break
        else:
            print("\nINVALID, please type 'YES' or 'NO'")
    return q_1

### Gamelist Shuffler ###
def shuffle_gamelist(game):
    shuffle(game)
    return game

### Ask the player his guess ###
def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Select your position: (0, 1 ,2): ')
    return int(guess)

### Check if guess was correct ###
def check_guess(gamelist,guess):
    if gamelist[guess] == '0':
        print('Correct!')
        print(gamelist)
    else:
        print('Wrong Guess!')
        print(gamelist)
        print('Try again next time!')

### Ask the player if he wants to play again ###
def play_again():
    q_2 = True 

    while q_2:
        answer = input("Do you want to play again? 'YES' or 'NO': ")

        if answer == 'NO':
            q_2 = False
            print("Thank you for playing Shuffle Game!")
        elif answer == 'YES':
            q_2 = True
            break
        else:
            print("INVALID, please type 'YES' or 'NO'")
    return q_2

#### GAMEPLAY LOGIC ####
print('WELCOME TO SHUFFLE GAME!')
SYSTEM = True

while SYSTEM:
    START = ask_to_start()

    if START:
        GAMELIST = [' ','0',' ']

        shuffled_list = shuffle_gamelist(GAMELIST)
        shuffled_list

        USER_GUESS = player_guess()
        check_guess(GAMELIST,USER_GUESS)

        QUESTION = play_again()
        if not QUESTION:
            SYSTEM = False
        else:
            continue

    else:
        SYSTEM = False
