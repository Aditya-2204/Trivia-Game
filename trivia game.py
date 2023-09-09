'''
triviagame.py
8/31
Aditya
Trivia Game
'''

import random
running = True
score = 0

questions = ["What countries made up the original Axis powers in World War II?", "Which country do cities of Perth, Adelade & Brisbane belong to?", "What geometric shape is generally used for stop signs?", "What is cynophobia?", "What punctuation mark ends an imperative sentence?"]
answers = ["Germany, Italy, and Japan", "Australia", "Octagon", "Fear of dogs", "A period or exclamation point"]

r = ""

print("Welcome")
t = True
counter = 0
while running:
    counter+=1
    r = random.choice(questions)
    n = input(r)
    if n != answers[questions.index(r)]:
        score-=1
        print(f"Score is {score}")
        print("Another chance")
        t = True
        while t:
            n = input(r)
            if n != answers[questions.index(r)]:
                score-=1
                print(f"Your score is {score}")
                print("Another chance")
            else:
                t = False
                break
    if n == answers[questions.index(r)]:
        print("Good job")
        score+=1
        print(f"Score is {score}")
    if counter == 3:
        print(f"The game has ended\n Your score is {str(score)}")
        print("Goodbye")
        running = False