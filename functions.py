import os.path
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
            fileName = input('Input file name: ').strip()
            with open(fileName) as inputFile:
                break
        except FileNotFoundError:
            print('File does not exist!')
    return fileName

def outputFileCheck():
    fileName = input("Output file name: ").strip()
    while os.path.isfile(fileName):
        while True:
            overwrite = input('Overwrite existing file? (y/n): ').strip().lower()
            if (overwrite == 'y'):
                return fileName
            elif (overwrite == 'n'):
                fileName = 'files/'+input('New output file name: ').strip()
    return fileName

def extract_student_info(row):
    name_match = re.search(r'(?i)studentname', row)
    score_match = re.search(r'(?i)score', row)

    if name_match and score_match:
        name_col = name_match.group()
        score_col = score_match.group()

        name = re.search(rf'(?i){name_col}\s*,\s*(?P<name>[\w\s]+)', row).group('name')
        score = int(re.search(rf'(?i){score_col}\s*,\s*(?P<score>\d+)', row).group('score'))

        return name, score
    else:
        raise ValueError("CSV file must contain 'studentname' and 'score' columns.")

