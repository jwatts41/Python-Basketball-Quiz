print('Welcome to my basketball trivia quiz!')

playing = input("You think you know basketball? If so, do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Let's get started")
score = 0

question = input("Which NBA team has the most championships? ")
if question.lower() == "lakers" or question.lower() == "la lakers" or question.lower() == "los angeles lakers":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is the Lakers.")

question = input("Which Collge Basketball team has the most NCAA championships? ")
if question.lower() == "ucla":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is UCLA.")