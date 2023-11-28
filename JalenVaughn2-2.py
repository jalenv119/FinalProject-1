import csv
from functions import *

def main():
    csv_filename = inputFileCheck()

    try:
        with open(csv_filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            csv_data = list(reader)

        check_csv_validity(csv_data)

        student_data = {}
        best = max(int(row['score']) for row in csv_data)

        for i, row in enumerate(csv_data, start=1):
            name = row['studentname']
            score = int(row['score'])
            grade = grade_score(score, best)
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
