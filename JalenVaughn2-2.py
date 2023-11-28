import os.path
import csv
import re

def grade_score(score, best):
    if score >= best - 10:
        return 'A'
    elif score >= best - 20:
        return 'B'
    elif score >= best - 30:
        return 'C'
    elif score >= best - 40:
        return 'D'
    else:
        return 'F'

def inputFileCheck():
    while True:
        try:
            scoreFile = input('Input file name: ').strip()
            with open(scoreFile) as inputFile:
                break
        except FileNotFoundError:
            print('File does not exist!')
    return scoreFile

def main():
    scoreFile = inputFileCheck()
    student_scores = []
    while len(student_scores) < student_amount:
        try:
            temp_student_scores = (input(f'Enter {student_amount} score(s):'))
            temp_scores = list(map(int, temp_student_scores.split()))
            if len(temp_scores) >= student_amount:
                student_scores.extend(temp_scores[:student_amount])
            else:
                print('Try Again!')
        except ValueError:
            print('F')
            
    best = max(student_scores)
    for i in range(student_amount):
        score = student_scores[i]
        grade = grade_score(score, best)
        student_number = i + 1
        print(f'student {student_number} score is {score} and grade is {grade}')


    
    #print(student_scores)


main()
