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

question = input("Which NBA team holds the record for the most regular season wins? ")
if question.lower() == 'warriors' or question.lower() == "golden state" or question.lower() == "golden state warriors":
    print("Correct")
    score += 1
else:
    print("Incorrect. The correct answer is the Golden State Warriors.")

question = input("How many teams are currently in the NBA? ")
if question == "30":
    print("Correct!")
    score += 1
else:
    print("Incorrect, the correct answer is 30.")

question = input("What college basketball coach holds the record for the most wins of all time? ")
if question.lower() == "coach k" or question.title() == "Coach K" or question.title() == "Mike Krzyzewski" or question.title() == "Krzyzewski":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Coach K.")

question = input("What NBA basketball coach holds the record for the most wins of all time? ")
if question.lower() == "gregg popovich" or question.title() == "Gregg Popovich" or question.title() == "Popovich":
    print("Correct!")
    score +=1
else:
    print("Incorrect. The correct answer is Gregg Popovich.")