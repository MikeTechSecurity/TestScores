# TestScores - Python
# https://github.com/MikeTechSecurity/
# Define a class called TestScores
class TestScores:
    def __init__(self):
        # Constructor method to initialize fields
        self.studentName = ""
        self.testScore1 = 0.0
        self.testScore2 = 0.0
        self.testScore3 = 0.0

    # Accessor methods to get values of fields
    def getStudentName(self):
        return self.studentName

    def getTestScore1(self):
        return self.testScore1

    def getTestScore2(self):
        return self.testScore2

    def getTestScore3(self):
        return self.testScore3

    # Mutator methods to set values of fields
    def setStudentName(self, name):
        self.studentName = name

    def setTestScore1(self, score):
        self.testScore1 = score

    def setTestScore2(self, score):
        self.testScore2 = score

    def setTestScore3(self, score):
        self.testScore3 = score

    # Method to calculate the average of the test scores
    def calculateAverage(self):
        average = (self.testScore1 + self.testScore2 + self.testScore3) / 3
        return average

# Define the main function
def main():
    # Create an instance of the TestScores class
    studentScores = TestScores()

    # Ask the user for the student's name
    studentName = input("Enter student's name: ")
    studentScores.setStudentName(studentName)

    # Ask the user for the three test scores and convert them to floating-point numbers
    testScore1 = float(input("Enter test score 1: "))
    studentScores.setTestScore1(testScore1)

    testScore2 = float(input("Enter test score 2: "))
    studentScores.setTestScore2(testScore2)

    testScore3 = float(input("Enter test score 3: "))
    studentScores.setTestScore3(testScore3)

    # Calculate the average of the test scores
    averageScore = studentScores.calculateAverage()

    # Display the average test score
    print("Average test score:", averageScore)

# Check if this script is being run as the main program
if __name__ == "__main__":
    main()
