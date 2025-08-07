MAX_GRADE = 100
MIN_GRADE = 0
FAILING_THRESHOLD = 55


def get_grade(subject: str, student_name: str) -> float:
    """Take input from user, validate, output (zero or greater) float."""
    while True:
        try:
            input_float = float(input(f"\t-Enter {student_name}'s {subject} grade: "))
            if input_float < MIN_GRADE or input_float > MAX_GRADE:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid grade: ( 0 <= grade <= 100 ).")

    return input_float


def get_student_info(subjects: list) -> dict:
    """Get student name, ask for grades for subjects in list 'subjects'. Output dict with collected info."""

    student_info = {}

    while True:
        try:
            student_name = str(input("\nEnter student name: "))
            if len(student_name) < 1:  # No empty strings == Prevents accidental double-taps
                raise ValueError
            break
        except ValueError:
            print("Please enter student name.")

    student_info['name'] = student_name

    for subject in subjects:
        grade = get_grade(subject, student_name)
        student_info[subject] = grade

    return student_info


def get_avg_grades(subjects: list, all_students: list) -> tuple:
    """Calculates averages per subject(item in subjects list) and Overall Average"""
    avg_grades = []
    total = 0

    for subject in subjects:
        sum_of_grades = 0
        for student in all_students:
            sum_of_grades += student[subject]
            total += student[subject]
        avg_grade = sum_of_grades / len(all_students)
        avg_grades.append(avg_grade)



    return tuple(avg_grades)  # tuple - as per requirement - dicts (items in tuple) scalable w/ different subject lists


def calculate_failing_grades(all_students: list) -> dict:
    """Sum total grades at/under failing threshold, per person, all students"""
    failing_grades = {}

    for student in all_students:
        failing_subjects = 0

        for key in student:
            if key != 'name':  # only grades to be counted
                if student[key] <= FAILING_THRESHOLD:
                    failing_subjects += 1

        name = student['name']
        failing_grades[name] = failing_subjects

    failing_grades['Class Total'] = sum(failing_grades.values())

    return failing_grades


def print_student_info(subjects: list, student_info: list) -> None:
    """Prints a report of best grade, average grade, by student name."""
    for item in student_info:  # print out individual grades
        print(f"\nStudent name: {item['name']}")

        student_grades = item.copy() #preserving input data
        del student_grades['name']
        best_subjects = []

        for subject in student_grades: #in case of identical best grades in multiple subjects
            if int(student_grades[subject]) == max(student_grades.values()):
                best_subjects.append(subject)

        print(f"\t-Best Grade: {max(student_grades.values())} (", end = "")
        for subject in best_subjects:
            if subject == best_subjects[-1]: #closing parentheses
                print(f"{subject})")
            else:
                print(f"{subject}, ", end = "")

        total = 0
        for subject in subjects: #calculate average
            total += item[subject]
        total_avg = total / len (subjects)  # sum of grades / (num students * num subjects per student)
        print(f"\t-Average Grade: {total_avg:.02f}")


def print_avg_grades(subjects: list, student_info: list) -> None:
    """print average grade statistics for entire input"""
    avg_grades = get_avg_grades(subjects, student_info)  # overall stats
    print(f"\nOverall Student Statistics:")
    for subject in subjects:
        print(f"\t-Average {subject} grade: {avg_grades[subjects.index(subject)]:.2f}")
    print(f"Overall Average grade across all subjects: {avg_grades[-1]:.2f}")


def print_failing_grades(student_info: list) -> None:
    """print out failing grades, per student. If none, note success"""
    failing_grades = calculate_failing_grades(student_info)  # failed grades
    print(f"\nFailing Grades:")
    for key in failing_grades:
        if key != 'Class Total':
            if failing_grades[key] > 0:
                print(f"\t{key}: {failing_grades[key]} failing grade(s).")
            else:
                print(f"\t{key}: passed all subjects successfully.")
        else:
            print(f"Total failing grades: {failing_grades[key]}")


def main():
    subjects = ["English", "Math"]
    student_info = []

    while True:  # validate input
        try:
            student_number = int(input("\nEnter number of students: "))
            if student_number < 1:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid number of students (> 0).")

    for i in range(student_number):
        student_info.append(get_student_info(subjects))

    print_student_info(subjects, student_info)
    print_avg_grades(subjects, student_info)
    print_failing_grades(student_info)


if __name__ == "__main__":
    main()
