from gui import *
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
import os.path
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Initializes the Logic class.
        """
        super().__init__()
        self.setupUi(self)
        self.submitCsvButton.clicked.connect(self.getStudentScoresCSV)
        self.submitManualEntryButton.clicked.connect(self.getStudentScoresManual)
        self.manualEntryNextStudent.clicked.connect(self.inputStudents)
        self.input_filename: str = ""
        self.output_filename: str = ""
        self.student_data: dict = {}

    def getStudentScoresCSV(self) -> None:
        """
        Reads student scores from a CSV file, and writes results to the specified output file.
        """

        try:
            self.student_data = {}
            self.input_filename = self.inputFileCheck()
            self.output_filename = self.outputFileCheck()
            if self.output_filename == "donot":
                raise IndexError
            with open(self.input_filename, "r") as csvfile:
                openedInputCSV = csv.DictReader(csvfile)
                for row in openedInputCSV:
                    self.student_data[(row["Name"])] = [row["Score"]]

                best = max(self.student_data.values())

                for row in self.student_data:
                    self.student_data[row].append(
                        self.grade_score(int(self.student_data[row][0]), int(best[0]))
                    )

            with open(self.output_filename, "w", newline="") as output_file:
                writer = csv.writer(output_file)

                writer.writerow(["Name", "Score", "Grade"])
                for name, data in self.student_data.items():
                    writer.writerow([name, data[0], data[1]])
            self.label_3.setText(
                f"Results have been written \nto '{self.output_filename}'."
            )

        except FileNotFoundError:
            if self.input_filename == "":
                self.label_3.setText("Please enter an \ninput filename.")
            if self.input_filename == "" and self.output_filename == "":
                self.label_3.setText("Please enter an \noutput and input filename.")
            elif self.output_filename == "":
                self.label_3.setText("Please enter an \noutput filename.")

        except ValueError as e:
            self.label_3.setText(f"Error: {e}")
        except IndexError:
            pass

    def inputStudents(self) -> None:
        """
        Grabs and splits the entry line for student data, requires a space split
        Raises ValueError for both non-alphanumeric inputs, and if the input has a non-integer for score
        Resets the error box for manual entry, and the manual entry box upon succsessfull addition of score
        """
        try:
            if not self.lineEdit_3.text().split()[0].isalnum():
                raise ValueError
            if not self.lineEdit_3.text().split()[1].isnumeric():
                raise ValueError
            self.student_data[self.lineEdit_3.text().strip().split()[0]] = [
                self.lineEdit_3.text().strip().split()[1]
            ]
            self.manerror.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_3.setFocus()

        except IndexError:
            self.manerror.setText("Please enter a name & score")

        except ValueError:
            if not self.lineEdit_3.text().split()[1].isnumeric():
                self.manerror.setText("Score is not a number")
            else:
                self.manerror.setText(
                    "Please input only numbers & \nletters with a space delimiter"
                )

    def getStudentScoresManual(self) -> None:
        """
        Processes manually entered scores and writes results to specified output file.
        """
        try:
            self.output_filename = self.outputFileCheckManual()
            best = max(self.student_data.values())
            if self.output_filename == "donot":
                raise IndexError
            for row in self.student_data:
                if len(self.student_data[row]) > 1:
                    raise IndexError
                self.student_data[row].append(
                    self.grade_score(int(self.student_data[row][0]), int(best[0]))
                )

            with open(self.output_filename, "w", newline="") as output_file:
                writer = csv.writer(output_file)

                writer.writerow(["Name", "Score", "Grade"])
                for name, data in self.student_data.items():
                    writer.writerow([name, data[0], data[1]])
            self.manerror.setText(
                f"Results have been written \nto '{self.output_filename}'."
            )

        except FileNotFoundError:
            if self.input_filename == "":
                self.manerror.setText("Please enter an \ninput filename.")
            if self.input_filename == "" and self.output_filename == "":
                self.manerror.setText("Please enter an \noutput and input filename.")
            elif self.output_filename == "":
                self.manerror.setText("Please enter an \noutput filename.")

        except ValueError as e:
            self.label_3.setText(f"Error: {e}")
        except IndexError:
            pass

    def outputFileCheckManual(self) -> str:
        """
        Checks for prexisting files, and asks the user if they want to overwritite the file.
        Returns the outputs filename.
        Only for manual entry method
        """
        self.output_filename = self.lineEdit_4.text()
        if os.path.isfile(self.output_filename):
            confirmation = QMessageBox.question(
                self,
                "File Overwrite Confirmation",
                f"The file '{self.output_filename}' already exists. Do you want to overwrite it?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )
            if confirmation == QMessageBox.StandardButton.No:
                return "donot"  # Returns donot to stop overwrite

        return self.output_filename

    def outputFileCheck(self) -> str:
        """
        Checks for prexisting files, and asks the user if they want to overwritite the file.
        Returns the outputs filename.
        """
        self.output_filename = self.lineEdit_2.text()
        if os.path.isfile(self.output_filename):
            confirmation = QMessageBox.question(
                self,
                "File Overwrite Confirmation",
                f"The file '{self.output_filename}' already exists. Do you want to overwrite it?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )
            if confirmation == QMessageBox.StandardButton.No:
                return "donot"  # Returns donot to stop overwrite

        return self.output_filename

    def inputFileCheck(self) -> str:
        """
        Prompts the user for an input filename until a valid one is used
        Returns input filename
        """
        while True:
            fileName = self.lineEdit.text()
            try:
                with open(fileName) as inputFile:
                    break
            except:
                self.label_3.setText("File does not exist!")
                break
        return fileName

    def grade_score(self, score, best) -> str:
        """
        Determines the grade of student based on score and best score
        Returns the grade
        """
        if score >= best - 10:
            return "A"
        elif score >= best - 20:
            return "B"
        elif score >= best - 30:
            return "C"
        elif score >= best - 40:
            return "D"
        else:
            return "F"

    def searchScore(self, data_dict, name_to_search) -> str:
        """
        uses hashtable lookup to search dictionary via key
        returns key upon succsess
        returns fail upon failure

        Currently unused
        """

        if name_to_search in data_dict:
            return name_to_search
        else:
            return "fail"
