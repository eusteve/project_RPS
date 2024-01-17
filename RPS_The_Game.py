#simple rock,paper,scissors game implemented on the cli
import random

#game rules
print('welcome to Rock-Paper-Scissors.\
      Rock vs paper - paper wins . \
      Rock vs Scissors - Rock wins\
      paper vs Scissors - Scissors win')
#define functions ~get_user_choice,determine_winner,
def get_User_choice(): #function gets the user's choice
       choice = int(input('pick a  choice "\n 1: Rock "\t 2: Papers "\t 3: Scissors'))
       if choice<1 or choice >3:
            print('Invalid choice, try again:') #limits  user's choice to 3 values
            choice = int(input('pick a  choice "\n 1: Rock "\t 2: Papers "\t 3: Scissors'))
       return choice # function needs to return a choice

def get_bot_choice () :
    return random.randint(1,3)# range of values between 1 and 3.

players_choice = get_User_choice()
bot_choice = get_bot_choice()

#game logic
def determine_Winner(bot_choice,players_choice):
     if players_choice == bot_choice: #case draw  (1,1), (2,2) and (3,3)
          print(' the game is tied.')
          #case :player wins ~ (1,2),(2,3) and (3,1)
     elif players_choice == 1 and bot_choice == 2 or players_choice == 2 and bot_choice == 3 or players_choice == 3 and bot_choice==1 :
          print(' computer wins')
          #case player wins (1,3) and (2,1)
     elif players_choice == 1 and bot_choice == 3 or players_choice == 2 and bot_choice == 1 or players_choice == 3 and bot_choice == 2 :
          print('you win')
def gameControl ( ):
    while True: #makes sures the game is alway running
        get_User_choice()
        determine_Winner(players_choice,bot_choice)
#play switch ~determines the continuation of the game
        next_play_response = int(input('do you wanna play again:\n  1: yes  and 2:no'))
        if next_play_response != 1: #captures user response
            print(' thank you for participating ')
            break #ends the  play here
gameControl ()# function call for the game control function






