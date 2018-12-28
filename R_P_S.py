#Rock Paper Scissors game with the computer

# INPUT: human player enters the number of point required for a win

import string
import random

def compar_str(letter1,letter2):
    
    if letter1.upper() == "R" and letter2.upper() == "P":
        letter2 > letter1
        s2 = 1
        s1 = 0
    elif letter1.upper() == "R" and letter2.upper() == "S":
        letter1 > letter2
        s2 = 0
        s1 = 1
    elif letter1.upper() == "P" and letter2.upper() == "S":
        letter2 > letter1
        s2 = 1
        s1 = 0

    elif letter1.upper() == "P" and letter2.upper() == "R":
        letter2 > letter1
        s2 = 0
        s1 = 1
    elif letter1.upper() == "S" and letter2.upper() == "R":
        letter1 > letter2
        s2 = 1
        s1 = 0
    elif letter1.upper() == "S" and letter2.upper() == "P":
        letter2 > letter1
        s2 = 0
        s1 = 1
    elif letter1.upper() == letter2.upper():
        letter2 = letter1
        s2 = 0
        s1 = 0
    
    a = [s1,s2]
    return a

def choice_displ(lett):
    if lett == "R":
        choice = "Rock"
    elif lett == "P":
        choice = "Paper"
    elif lett == "S":
        choice = "Scissors"
    return choice

print("Welcome to Rock, Paper, Scissors!!")
win_score = int(input("How many points are required for a win? "))
mylist = ["R", "P", "S"]
comp_score = 0
huma_score = 0

while comp_score < win_score and huma_score < win_score:
    huma_choice = input("Choose (R) for Rock, (P) for Paper or (S) for Scissors: ").upper()
    comp_choice = random.choice(mylist)
    [score1,score2]=compar_str(comp_choice,huma_choice)
    
    if score1 > score2:
        comp_score +=1
        result = "    Computer wins!"  
    elif score1 < score2:
        huma_score += 1
        result = "    Human wins!"
    elif score1 == score2:
        result = "    A draw"
        
    print("Human:",choice_displ(huma_choice.upper()),"  Computer: ",choice_displ(comp_choice.upper()),result)
    print("Score: Human ",huma_score,"  Computer ",comp_score)  
if comp_score == win_score or huma_score == win_score:
    print("Final Score: Human ",huma_score,"  Computer ",comp_score)




      
