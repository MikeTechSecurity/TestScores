# TestScores
This Python code defines the TestScores class with its methods and the main function. It allows the user to input the student's name and three test scores and then calculates and displays the average score.

# Explanation:

    We define a TestScores class with fields for the student's name and three test scores. It includes constructor, accessor, mutator methods, and a method to calculate the average score.

    In the main function:

We create an instance of the TestScores class called studentScores.
We use the input function to get the student's name and three test scores from the user.
We convert the test scores to floating-point numbers using float() to ensure that the calculations will be performed correctly.
We call the appropriate setter methods to set the values for the studentScores object.
We calculate the average score by calling the calculateAverage method of the studentScores object.
Finally, we display the average test score using the print function.

    The if __name__ == "__main__": block ensures that the main function is executed when the script is run as the main program but not when it's imported as a module into another script.
