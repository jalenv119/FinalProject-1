iimport csv
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


def main():
    csv_filename = input("Enter CSV file name: ")

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
