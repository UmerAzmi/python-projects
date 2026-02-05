import random
print('\n\tWelcome to the Rock Paper Scissors game!')
user_points = 0
computer_points = 0

choice = ['rock','paper','scissors']
while True:
    user_pick = input('\nEnter your choice - Rock/Paper/Scissors or q to quit: ').lower()
    if user_pick.lower() == 'q':
       break
    if user_pick not in choice:
        print('Please enter a valid choice.')
        continue

    computer_pick = random.randint(0,2)
    computer_pick = choice[computer_pick]
    print(f'Computer picked {computer_pick}.')

    if user_pick == 'rock' and computer_pick == 'scissors':
        print('You won!')
        user_points += 1

    elif user_pick == 'paper' and computer_pick == 'rock':
        print('You won!')
        user_points += 1

    elif user_pick == 'scissors' and computer_pick == 'paper':
        print('You won!')
        user_points += 1

    elif user_pick == computer_pick:
        print('Its a tie!')

    else:
        print('You lost!')
        computer_points += 1

print(f'Your total points: {user_points} and Computer total points: {computer_points}')
if user_points == computer_points:
    print('Its a tie!')
elif user_points > computer_points:
    print('You won!')
else:
    print('You lost!')
