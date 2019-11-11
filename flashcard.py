#sys is a module. it let us access command line arguments through sys.argv.

import sys
import random

#print(sys.argv)

if len(sys.argv) < 2:
    print("Please supply a flashcard file.")
    exit(1)

flashcard_filename = sys.argv[1]
f = open(flashcard_filename, "r")

question_dict = {}

for line in f:
	entry = line.strip().split(",")
	question = entry[0]
	answer = entry[1]
	question_dict[question] = answer

f.close()

print("Welcome to the flashcard quizzer.")
print("At any time, type 'quit' to quit.")
print("")

questions = list(question_dict.keys())


while True:
    question = random.choice(questions)
    answer = question_dict[question]
    print("Question: " + question)
    
    guess = input("Your Guess > ")
    
    if guess == "quit":
        print("Goodbye!")
        break
    elif guess == answer:
        print("Correct!")
    else:
        print("Sorry the answer is: " + answer)

    
