print('Welcome to my basketball trivia quiz!')

playing = input("You think you know basketball? If so, do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Let's get started")
score = 0

question = input("Question 1. Which NBA team has the most championships? ")
if question.lower() == "lakers" or question.lower() == "la lakers" or question.lower() == "los angeles lakers":
    print("Correct! 6 Questions Remaining")
    score += 1
else:
    print("Incorrect. The correct answer is the Lakers. 6 Questions Remaining")

question = input("Question 2. Which Collge Basketball team has the most NCAA championships? ")
if question.lower() == "ucla":
    print("Correct! 5 Questions Remaining")
    score += 1
else:
    print("Incorrect. The correct answer is UCLA. 5 Questions Remaining")

question = input("Question 3. Which NBA team holds the record for the most regular season wins? ")
if question.lower() == 'warriors' or question.lower() == "golden state" or question.lower() == "golden state warriors":
    print("Correct! 4 Questions Remaining")
    score += 1
else:
    print("Incorrect. The correct answer is the Golden State Warriors. 4 Questions Remaining")

question = input("Question 4. How many teams are currently in the NBA? ")
if question == "30":
    print("Correct! 3 Questions Remaining")
    score += 1
else:
    print("Incorrect, the correct answer is 30. 3 Questions Remaining")

question = input("Question 5. What college basketball coach holds the record for the most wins of all time? ")
if question.lower() == "coach k" or question.title() == "Coach K" or question.title() == "Mike Krzyzewski" or question.title() == "Krzyzewski":
    print("Correct! 2 Questions Remaining")
    score += 1
else:
    print("Incorrect. The correct answer is Coach K. 2 Questioning Remaining")

question = input("Question 6. What NBA basketball coach holds the record for the most wins of all time? ")
if question.lower() == "gregg popovich" or question.title() == "Gregg Popovich" or question.title() == "Popovich":
    print("Correct! 1 Question Remaining")
    score +=1
else:
    print("Incorrect. The correct answer is Gregg Popovich. 1 question remaining")

question = input("Question 7. Who is a better college basketball team? North Carolina or Duke?")
if question.lower() == "north carolina" or question.lower() == "carolina" or question.title() == "North Carolina":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is North Carolina. Do better")

