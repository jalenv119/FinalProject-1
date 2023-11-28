import csv
from functions import *

def main():
    csv_filename = inputFileCheck()

    try:
        with open(csv_filename, 'r') as csvfile:
            student_data = csv.DictReader(csvfile)
            for row in student_data:
                print(row)

        best = max(int(row['score']) for row in student_data)
        print(student_data)
        for i, row in enumerate(student_data, start=1):
            name = row['studentname']
            score = int(row['score'])
            grade = grade_score(score, best)
            print(name,score,grade)
            student_data[f'student {i}'] = {'name': name, 'score': score, 'grade': grade}

        with open('output.csv', 'w', newline='') as output_file:
            fieldnames = ['Student', 'Name', 'Score', 'Grade']
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()

            for student, data in student_data.items():
                writer.writerow({
                    'Student': student,
                    'Name': data['name'],
                    'Score': data['score'],
                    'Grade': data['grade']
                })

        print("Results have been written to 'output.csv'.")

    except FileNotFoundError:
        print("File not found.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
