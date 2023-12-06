from gui import *
from PyQt6.QtWidgets import *
import os.path
import csv

class Logic(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.submitCsvButton.clicked.connect(self.getStudentScoresCSV)
        self.input_filename = ''
        self.output_filename = ''

    def getStudentScoresCSV(self):
        try:
            self.input_filename=self.inputFileCheck()
            self.output_filename=self.outputFileCheck()
            student_data = {}
            with open(self.input_filename, 'r') as csvfile:
                openedInputCSV = csv.DictReader(csvfile)
                for row in openedInputCSV:
                    student_data[(row['Name'])] = [row['Score']] 

                best = max(student_data.values())
                
                for row in student_data:
                    student_data[row].append(self.grade_score(int( student_data[row][0] ),int(best[0])))
            with open(self.output_filename, 'w', newline='') as output_file:
                writer = csv.writer(output_file)

                writer.writerow(['Name','Score','Grade'])
                for name, data in student_data.items():
                    writer.writerow([
                    name,
                    data[0],
                    data[1]
                    ])
            self.label_3.setText("Results have been written to 'output.csv'.")

        except FileNotFoundError:
            if self.input_filename == '':
                self.label_3.setText("Please enter an input filename")
            if self.input_filename == '' and self.output_filename == '':
                self.label_3.setText("Please enter an output and input filename.")
                #TODO please fix output_filename method
        except ValueError as e:
            self.label_3.setText(f"Error: {e}")



    def inputFileCheck(self) -> str:
        while True:
            try:
                fileName = self.lineEdit.text()
                with open(fileName) as inputFile:
                    break
            except FileNotFoundError:
                return 'File does not exist!'
        return fileName

    def outputFileCheck(self) -> str:
        fileName = input("Output file name: ").strip()
        while os.path.isfile(fileName):
            while True:
                overwrite = input('Overwrite existing file? (y/n): ').strip().lower()
                if (overwrite == 'y'):
                    return fileName
                elif (overwrite == 'n'):
                    fileName = 'files/'+input('New output file name: ').strip()
        return fileName

    def grade_score(self, score, best) -> str:
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
 
    def searchScore(self,data_dict,name_to_search) -> str:
        if name_to_search in data_dict:
            return name_to_search
        else:
            return 1  

    # def extract_student_info(self,row) :
    #     name_match = re.search(r'(?i)studentname', row)
    #     score_match = re.search(r'(?i)score', row)
    #
    #     if name_match and score_match:
    #         name_col = name_match.group()
    #         score_col = score_match.group()
    #
    #         name = re.search(rf'(?i){name_col}\s*,\s*(?P<name>[\w\s]+)', row).group('name')
    #         score = int(re.search(rf'(?i){score_col}\s*,\s*(?P<score>\d+)', row).group('score'))
    #
    #         return name, score
    #     else:
    #         raise ValueError("CSV file must contain 'studentname' and 'score' columns.")

