from Grading_system import calculate_grade, calculate_gpa

def test_calculate_grade():
    assert calculate_grade(95) == 'A'
    assert calculate_grade(85) == 'B'
    assert calculate_grade(75) == 'C'
    assert calculate_grade(65) == 'D'
    assert calculate_grade(55) == 'F'

def test_calculate_gpa():
    assert calculate_gpa(['A', 'B', 'C', 'D']) == 2.5
    assert calculate_gpa(['A', 'A', 'B', 'B']) == 3.5
    assert calculate_gpa([]) == 0.0
