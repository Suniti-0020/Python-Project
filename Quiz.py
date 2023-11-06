# JSON is a syntax for storing and exchanging data.
# Python has a built-in package called json, which can be used to work with JSON data.
import json
# Python Random module is an in-built module of Python which is used to generate random numbers. 
import random
# No echo input ( passwords aren't shown )

import matplotlib.pyplot as plt
import numpy as np



def Quiz_Start(f) :
    print("\n==========QUIZ START==========")
    score = 0  
    j = json.load(f)
    for i in range(10):
        no_of_questions = len(j)
        ch = random.randint(0, no_of_questions-1)
        print(f'\nQ{i+1} {j[ch]["question"]}\n')
        for option in j[ch]["options"]:
            print(option)
        answer = input("\nEnter your answer: ")
        if j[ch]["answer"][0] == answer[0].upper():
            print("\nYou are correct")
            score+=1
        else:
            print("\nYou are incorrect")
        del j[ch]
    print(f'\nFINAL SCORE: {score}')
    y = np.array([score,10-score])
    mylabels = ["Correct", "Incorrect"]
    myexplode = [0.1,0]
    plt.pie(y,labels = mylabels, explode = myexplode)
    plt.show() 
	

def play():
	choice = 1
	while choice != 6:
		print('\n========Select any topic==========')
		print('-----------------------------------------')
		print('1. Sports  ')
		print('2. Entertainment')
		print('3. History')
		print('4. Science')
		print('5. CS Fundamentals')
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			with open("assets/sports.json", 'r+') as f:
				Quiz_Start(f)
		elif choice == 2:
			with open("assets/entertainment.json", 'r+') as f:
				Quiz_Start(f)
		elif choice == 3:
			with open("assets/history.json", 'r+') as f:
				Quiz_Start(f)
		elif choice == 4:
			with open("assets/science.json", 'r+') as f:
				Quiz_Start(f)
		elif choice == 5:
			with open("assets/csfundamentals.json", 'r+') as f:
				Quiz_Start(f)
		elif choice == 6:
			break
		else:
			print('WRONG INPUT. ENTER THE CHOICE AGAIN')
	
def addQuestion(f,ques,opt,ans) :
    questions = json.load(f)
    dic = {"question": ques, "options": opt, "answer": ans} 
    questions.append(dic)
    f.seek(0)
    json.dump(questions, f)
    f.truncate()
    print("Question successfully added.")	

def quizQuestions():	
    print('\n==========ADD QUESTIONS==========\n')
    ques = input("Enter the question that you want to add:\n")
    opt = []
    print("Enter the 4 options with character initials (A, B, C, D)")
    for _ in range(4):
        opt.append(input())
    ans = input("Enter the answer:\n")
    choice = 1 
    while choice != 6:
        print('\n========Select any topic==========')
        print('-----------------------------------------')
        print('1. Sports  ')
        print('2. Entertainment')
        print('3. History')
        print('4. Science')
        print('5. CS Fundamentals')
        choice = int(input('ENTER YOUR CHOICE: '))
        if choice == 1:
            with open("assets/sports.json", 'r+') as f:
                addQuestion(f,ques,opt,ans)
            break
        elif choice == 2:
            with open("assets/entertainment.json", 'r+') as f:
                addQuestion(f,ques,opt,ans)
            break
        elif choice == 3:
            with open("assets/history.json", 'r+') as f:
                addQuestion(f, ques,opt,ans)
            break
        elif choice == 4:
            with open("assets/science.json", 'r+') as f:
                addQuestion(f, ques,opt,ans)
            break
        elif choice == 5:
            with open("assets/csfundamentals.json", 'r+') as f:
                addQuestion(f, ques,opt,ans)
            break
        elif choice == 6:
            break
        else:
            print('WRONG INPUT. ENTER THE CHOICE AGAIN')
					
		

def rules():
	print('''\n==========RULES==========
1. Each round consists of 10 random questions. To answer, you must press A/B/C/D (case-insensitive).
Your final score will be given at the end.
2. Each question consists of 1 point. There's no negative point for wrong answers.
	''')

def about():
	print('''\n==========ABOUT US==========
This project has been created by Suniti , Sarika and Nidhi .
It is a basic Python Project for my 3rd Semester.''')

if __name__ == "__main__":
	choice = 1
	while choice != 4:
		print('\n=========WELCOME TO QUIZ MASTER==========')
		print('-----------------------------------------')
		print('1. PLAY QUIZ')
		print('2. ADD QUIZ QUESTIONS')
		print('3. SEE INSTRUCTIONS ON HOW TO PLAY THE GAME')
		print('4. EXIT')
		print('5. ABOUT US')
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			play()
		elif choice == 2:
			quizQuestions()
		elif choice == 3:
			rules()
		elif choice == 4:
			break
		elif choice == 5:
			about()
		else:
			print('WRONG INPUT. ENTER THE CHOICE AGAIN')