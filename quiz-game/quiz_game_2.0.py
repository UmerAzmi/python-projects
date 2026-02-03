score=0
print('Welcome to Quizimania 2.0.')
answer = input('Do you wanna play the quiz game? ')
if answer.lower() == 'yes':
     print("\n\tOkay let's play")
else:
     print('\n\tWhy did you run the program then?')
     quit()

questions = {
    "1) What do cows drink?": {
        "options": ["a) Milk", "b) Water", "c) Fanta", "d) Tea/Coffee"],
        "answer": "b"
    },
    "2) If you freeze water, what do you get?": {
        "options": ["a) Ice", "b) Boiled Water", "c) Cake", "d) Frozen Pizza"],
        "answer": "a"
    },
    "3) What does 'LOL' stand for in chats?": {
        "options": ["a) Lots of Love", "b) Laugh Out Loud", "c) League of Legends", "d) Laddoo or Lassi"],
        "answer": "b"
    },
    "4) What is the capital of Mars (according to aliens 🤖)?": {
        "options": ["a) Winterfell", "b) Elon Mars", "c) Mars doesn’t have a capital", "d) Hogwarts"],
        "answer": "c"
    },
    "5) How many sides does a triangle have?": {
        "options": ["a) 2", "b) 3", "c) 4", "d) Depends on my mood"],
        "answer": "b"
    },
    "6) If you have 0 chocolates and you eat 1, what do you have?": {
        "options": ["a) -1 chocolate", "b) Stomach pain", "c) Depression", "d) None of the above"],
        "answer": "d"
    },
    "7) Who let the dogs out?": {
        "options": ["a) Who, who, who, who, who?", 'b) John Cena?', 'c) Krrish?', "d) Cow drinks water"],
        "answer": "a"
    },
    "8) Which year was Umer born? ": {
        "answer": "2002"
    }
}
for q,ans in questions.items():
    print('\n',q)
    if "options" in ans:
        for options in ans['options']:
           print(options)
    user_answer = input('Ans. ')

    if user_answer == ans['answer']:
        print('Correct')
        score += 1
    else:
        print('Incorrect')

percentage= score/8 * 100
print('\nWell Done! You have completed the quiz.')
print(f"You've got {score} correct answers")
print(f"You got {percentage}%.\n")
if percentage > 80:
    print('Well done! You have smashed the Quiz')
elif percentage > 35:
    print('Well done! You have passed the Quiz. Try again if you want to smash it')
else:
    print('Well done! You have failed the Quiz. You should be proud of your self. Go study!')

