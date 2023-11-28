import csv
from functions import *

def main():
    csv_filename = 'input.csv'

    try:
        student_data = {}
        with open(csv_filename, 'r') as csvfile:
            openedInputCSV = csv.DictReader(csvfile)
            for row in openedInputCSV:
                student_data[(row['Name'])] = [row['Score']] 

            best = max(student_data.values())
            
            for row in student_data:
                student_data[row].append(grade_score(int( student_data[row][0] ),int(best[0])))
            for x in student_data:
                print(x,student_data[x])


        with open('output.csv', 'w', newline='') as output_file:
            fieldnames = ['Student', 'Name', 'Score', 'Grade']
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()

            for name, data in student_data.items():
                writer.writerow({
                'Name': name,
                'Score': student_data['Score'],
                'Grade': student_data['Grade']
                })

        print("Results have been written to 'output.csv'.")

    except FileNotFoundError:
        print("File not found.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
