from random import randint
# from typing import Optional

# def win():
#     print ('You win!')

# def lose():
#     print ('You lose!')

while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves [random_move]

    if player_choice == computer_choice:
        print ('Draw!')
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print("you win")
    elif player_choice == 'paper' and computer_choice == 'scissors':
        print("you lose")
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print("you win")
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print("lose win")
    elif player_choice == 'paper' and computer_choice == 'rock':
        print("you win")
    elif player_choice == "rock"  and computer_choice == "sciessor":
        print("you lose")
    again = input('Do you want to play again? (y or n)').strip()                                                                                                 
    if again == 'n':
        break
          
