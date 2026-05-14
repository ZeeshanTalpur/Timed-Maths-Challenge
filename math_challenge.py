import random
import os
import time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def head(points,start, name):
    print("\t\t\t\tWelcome to the timed maths challenge\t\tTime left:",round(60-(time.time()-start),0)," seconds\tCorrect Answers: ",points)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlayer Name: ",name)
points=0
def problem_generator(mode,name) :
    global points
    if mode==1:
        min_operand=2
        max_operand=10
    elif mode==2:
        min_operand=5
        max_operand=20
    elif mode==3:
        min_operand=10
        max_operand=30
    operators=['+','-','*','/']
    start=time.time()
    while time.time()-start<=60:
        operand1=random.randint(min_operand,max_operand)
        operand2=random.randint(min_operand,max_operand)
        operator=random.choice(operators)
        expression=str(operand1)+operator+str(operand2)
        clear()
        head(points,start,name)
        print(expression)
        if operator == '+':
            correct_answer=operand1 + operand2
        elif operator == '-':
            correct_answer=operand1 - operand2
        elif operator == '*':
            correct_answer=operand1 * operand2
        elif operator == '/':
            correct_answer=operand1 / operand2
        answer=float(input("Your answer: "))
        if abs(answer - correct_answer)<0.1:
            print("Correct!")
            points+=1
            time.sleep(1)
        else:
            print("Incorrect!")
            time.sleep(1)

    print("Your score is ",points)
    if mode==1:
        mode="Easy"
    if mode==2:
        mode="Medium"
    if mode==3:
        mode="Difficult"
    with open("scorebaord.txt",'a') as f:
        f.write(f"Name: {name}\t\tScore: {points}\t\tMode: {mode}\n")
    print("Game Over!")
        
        

clear()
print("\t\t\tWelcome to the timed Mathematics Challenge")
name=input("Enter your name: ")
print("Do you want to play\n1. Easy\n2. Medium\n3. Difficult")
mode=int(input("Enter 1/2/3: "))
problem_generator(mode,name)