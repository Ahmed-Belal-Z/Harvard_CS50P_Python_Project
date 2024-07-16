
def main():
    student_data = get_student_info()
    grades = get_subject_grades(student_data['name'], student_data['num_subjects'])
    letter_grades = [calculate_grade(grade) for grade in grades]
    gpa = calculate_gpa(letter_grades)
    display_results(student_data['name'], letter_grades, gpa)

def calculate_grade(score):

    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def calculate_gpa(grades):

    grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    total_grade_points = sum(grade_points[grade] for grade in grades)
    return total_grade_points / len(grades) if len(grades) > 0 else 0.0

def get_student_info():

    name = input("Enter your name: ").capitalize()
    num_subjects = int(input("Enter the number of subjects: "))
    return {'name': name, 'num_subjects': num_subjects}

def get_subject_grades(name, num_subjects):

    print(f"Hello, {name}!")
    subject_grades = []
    for i in range(1, num_subjects + 1):
        grade = int(input(f"Enter grade for subject {i}: "))
        subject_grades.append(grade)
    return subject_grades

def display_results(name, letter_grades, gpa):

    print(f"\n{name}'s Letter grades: {letter_grades}")
    print(f"{name}'s GPA: {gpa:.2f}")

if __name__ == "__main__":
    main()
    