This Python program is designed to assist students by calculating their grades and GPA based on the scores they input for multiple subjects. Here's a detailed overview of the program:

Youtube video Url: https://youtu.be/TaVIgkfKX9Y

Features:

User Information Collection: The program starts by asking the user to input their name and the number of subjects they want to input grades for.

Grade Calculation Functions:

calculate_grade(score): Takes a numerical score and returns the corresponding letter grade based on a standard grading scale (A, B, C, D, F).

calculate_gpa(grades): Computes the GPA (Grade Point Average) based on a list of letter grades using a standard GPA scale (4.0 for A, 3.0 for B, etc.).
Main Process:

main(): Orchestrates the entire process.

Calls get_student_info() to collect the student's name and number of subjects.

Invokes get_subject_grades() to collect grades for the specified number of subjects.

Utilizes calculate_grade() to convert scores into letter grades.

Uses calculate_gpa() to calculate the GPA based on the letter grades.

Displays the results using display_results().

User Interaction:

The program prompts the user to enter their name, the number of subjects, and grades for each subject.
After collecting the data, it calculates the corresponding letter grades and GPA.
Finally, it presents the user with their letter grades and GPA for the entered subjects.
Execution:
When executed, the program guides the user through the process of inputting their name, specifying the number of subjects they want to input grades for, and then entering the grades for each subject. Afterward, it displays the calculated letter grades and GPA based on the entered data.

The code structure is modular, allowing for easy expansion or modification to suit specific requirements or additional functionalities.

This program aims to provide a simple yet effective tool for students to compute their grades and GPA quickly and accurately based on their input.






