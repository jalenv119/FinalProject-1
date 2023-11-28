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

def extract_student_info(row):
    
    name_match = re.search(r'(?i)studentFile', row)
    score_match = re.search(r'(?i)scoreFile', row)

    if name_match and score_match:
        name_col = name_match.group()
        score_col = score_match.group()

        # Extract values using regex
        name = re.search(rf'(?i){name_col}\s*,\s*(?P<name>[\w\s]+)', row).group('name')
        score = int(re.search(rf'(?i){score_col}\s*,\s*(?P<score>\d+)', row).group('score'))
        
        return name, score
    else:
        raise ValueError()

def main():
    read_from_csv = True

    if read_from_csv:
        csv_filename = input("Enter CSV file name: ")
        with open(csv_filename, 'r') as csvfile:
            csv_data = csvfile.read()
            student_info_list = [extract_student_info(row) for row in csv_data.splitlines()]

    else:
        student_amount = int(input('Total number of students: '))
        student_info_list = []
        while len(student_info_list) < student_amount:
            try:
                temp_student_info = input(f'Enter {student_amount} student info (e.g., "Name, Score"): ')
                name, score = extract_student_info(temp_student_info)
                student_info_list.append((name, score))
            except ValueError as e:
                print(f'Error: {e}')

    best = max(student_info_list, key=lambda x: x[1])[1]
    student_data = {}

    for i, (name, score) in enumerate(student_info_list, start=1):
        grade = grade_score(score, best)
        student_data[f'student {i}'] = {'name': name, 'score': score, 'grade': grade}

    for student, data in student_data.items():
        print(f"{student} {data['name']}'s score is {data['score']} and grade is {data['grade']}")

if __name__ == "__main__":
    main()


main()
