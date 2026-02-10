print('\nWelcome to Matchstick Game.')
print('There are 21 matchsticks.')
print('You can pick 1 to 4 matchsticks.')
print('You can pick 0 to exit the game.')
print('Whoever picks the last matchstick loses.')

matchsticks = 21
game_exited = False 

while matchsticks > 0:
    print('\nMatchsticks left:', matchsticks)

    while True:
        try:
            user_pick = int(input('Pick 1 to 4 matchsticks: '))
            if user_pick == 0:
                game_exited = True 
                break 
            elif user_pick < 1 or user_pick > 4:
                print('Please pick between 1 and 4.')
            elif user_pick > matchsticks:
                print('Not enough matchsticks left.')
            else:
                break
        except:
            print('Please enter a number.')

    if game_exited: 
        print('Bye')
        break 

    matchsticks -= user_pick

    if matchsticks == 0:
        print('\nYou picked the last matchstick.')
        print('You lost 🦆')
        break

    print('\nComputer turn...')

    computer_pick = 5 - user_pick

    if computer_pick > matchsticks:
        computer_pick = 1

    print('Computer picked:', computer_pick)
    matchsticks -= computer_pick

    if matchsticks == 0:
        print('\nComputer picked the last matchstick.')
        print('You won 🎉')
        break
