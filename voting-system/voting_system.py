print('Welcome to Voting System.')

votes = {
    'A': 0,
    'B': 0,
    'C': 0
}

def cast_vote():
    choice = input('Vote for A / B / C: ').upper()
    if choice in votes:
        votes[choice] += 1
        print('Vote cast successfully.')
    else:
        print('Invalid vote.')

def view_results():
    for candidate, count in votes.items():
        print(f'{candidate} : {count}')

while True:
    print('\n1. Cast Vote')
    print('2. View Results')
    print('3. Exit')

    choice = input('Choose an option: ')

    if choice == '1':
        cast_vote()
    elif choice == '2':
        view_results()
    elif choice == '3':
        print('Exiting...')
        break
    else:
        print('Invalid choice.')
