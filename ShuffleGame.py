'''
SHUFFLE GAME SCRIPT
'''
### Ask the player if he wants to start the game ###
def ask_to_start():
    
    q = True
    while q == True:
        answer = input('Do you want to start the game? (YES or NO): ')
        if answer == 'NO':
            print('Thank you for playing!')
            q == False
            return False
        elif answer == 'YES':
            q == True
            return True
        else:
            print("\nINVALID, please type 'YES' or 'NO'")
    
### Gamelist Shuffler ###    
from random import shuffle

def shuffle_gamelist(game):
    shuffle(game)
    return game

### Ask the player his guess ###
def player_guess():
    
    guess = ''
    
    while guess not in ['0', '1', '2']:
        guess = input('Select your position: (0, 1 ,2): ' )
    return int(guess)

### Check if guess was correct ###
def check_guess(gamelist,guess):
    if gamelist[guess] == '0':
        print('Correct!')
    else:
        print('Wrong Guess!')
        print(gamelist)
        print('Try again next time!')

### Ask the player if he wants to play again ###
def play_again():
    
    q = True 
    
    while q == True:
        answer = input("Do you want to play again? 'YES' or 'NO': ")
        
        if answer == 'YES':
            q = False
            return True
        elif answer == 'NO':
            q = False 
            return False
        else:
            print("INVALID, please type 'YES' or 'NO'")

#### GAMEPLAY LOGIC ####
print('WELCOME TO SHUFFLE GAME!')
system = True

while system == True:
    start = ask_to_start()

    if start == False:
        system = False
        break

    elif start == True:
        gamelist = [' ','0',' ']

        shuffled_list = shuffle_gamelist(gamelist)
        shuffled_list
        
        user_guess = player_guess()
        check_guess(gamelist,user_guess)

        question = play_again()
        if question == True:
            system = True
            continue
        elif question == False:
            print("Thank you for playing Shuffle Game!")
            system = False
            break
