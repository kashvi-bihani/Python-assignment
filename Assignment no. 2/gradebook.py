#Name - Kashvi Bihani
#Date- 21st Nov 2025
#Title-Analysing and Reporting Student Grades

#TASK 1 ----Project Setup and Initialization----

print("Welcome to my Gradebook project.")
print("This project will help in assigning grades & generates the summary report of students.")

# Task 2: ----Data Entry Functions----
import csv
def manual_entry():
    marks = {}
    n = int(input("How many students do you want to enter? "))

    for i in range(n):
        name = input("Enter student name: ")
        mark = int(input(f"Enter marks for {name}: "))
        marks[name] = mark
    return marks


def csv_file():
    marks = {}
    file_path = input("Enter the path of the CSV File: ")

    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if len(row) == 2:
                    name, mark = row
                    marks[name] = int(mark)

    except FileNotFoundError:
        print("File not found!")
    except ValueError:
        print("Error reading marks. Check file format.")
    return marks


print("Choose a method :")
print("1. Manual Entry")
print("2. Load from CSV File")

choice = input("Enter choice (1/2): ")

if choice == "1":
    marks = manual_entry()
elif choice == "2":
    marks = csv_file()
else:
    print("Invalid choice!")
    marks = {}

# Task 3: ----Statistical Analysis Functions----

def calculation_average(marks_dict):
    if not marks_dict:
        return 0
    return sum(marks_dict.values()) / len(marks_dict)


def calculate_median(marks_dict):
    if not marks_dict:
        return 0

    marks_list = sorted(marks_dict.values())
    n = len(marks_list)

    if n % 2 == 1:
        return marks_list[n // 2]
    else:
        marks_list1 = marks_list[n // 2 - 1]
        marks_list2 = marks_list[n // 2]
        return (marks_list1 + marks_list2) / 2


def find_max_score(marks_dict):
    if not marks_dict:
        return None, None
    max_name = max(marks_dict, key=marks_dict.get)
    return max_name, marks_dict[max_name]


def find_min_score(marks_dict):
    if not marks_dict:
        return None, None
    min_name = min(marks_dict, key=marks_dict.get)
    return min_name, marks_dict[min_name]


def display_summary(marks_dict):
    print("\n--- Analysis Summary ---")

    avg = calculation_average(marks_dict)
    median = calculate_median(marks_dict)
    max_name, max_score = find_max_score(marks_dict)
    min_name, min_score = find_min_score(marks_dict)

    print(f"Average Score: {avg:.2f}")
    print(f"Median Score: {median}")
    print(f"Highest Score: {max_score} ({max_name})")
    print(f"Lowest Score: {min_score} ({min_name})")

print("Final Data Stored:")
print(marks)
display_summary(marks)

#TASK 4 ----Grade Assignment and Distribution----

def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def gradebook(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        grades[name] = assign_grade(score)
    return grades
def grade_distribution(grades_dict):
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for grade in grades_dict.values():
        distribution[grade] += 1

    return distribution
def grades_summary(grades_dict):
    print("\n--- Gradebook (A–F) ---")
    for name, grade in grades_dict.items():
        print(f"{name}: {grade}")

    dist = grade_distribution(grades_dict)

    print("\n--- Grade Distribution ---")
    for grade, count in dist.items():
        print(f"{grade}: {count} students")

grades = gradebook(marks)

grades_summary(grades)

#TASK 5 ----Pass/Fail Filter with List Comprehension----

def pass_fail_filter(marks_dict):
    passed_students = [name for name, score in marks_dict.items() if score >= 40]
    failed_students = [name for name, score in marks_dict.items() if score < 40]
    return passed_students, failed_students

def display_pass_fail(marks_dict):
    passed, failed =pass_fail_filter(marks_dict)

    print("\n--- Pass/Fail Summary ---")
    print(f"Total Passed: {len(passed)}")
    print(f"Passed Students: {passed if passed else 'None'}")

    print(f"\nTotal Failed: {len(failed)}")
    print(f"Failed Students: {failed if failed else 'None'}")
display_pass_fail(marks)

#TASK 6 : -----Results Table and User Loop-----

def results_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("-" * 40)

    for name, mark in marks.items():
        print(f"{name:<12}{mark:<10}{grades[name]}")


while True:

    print("\n--- MAIN MENU ---")
    print("1. Show Final Data")
    print("2. Show Analysis Summary")
    print("3. Show Gradebook & Distribution")
    print("4. Show Pass/Fail Report")
    print("5. Show Results Table")
    print("6. Exit")

    user_choice = input("Enter your choice (1–6): ")

    if user_choice == "1":
        print("Final Data Stored:")
        print(marks)

    elif user_choice == "2":
        display_summary(marks)

    elif user_choice == "3":
        print("\n--- Gradebook ---")
        print(grades)
        dist = grade_distribution(grades)
        print("\n--- Grade Distribution ---")
        for g, c in dist.items():
            print(f"{g}: {c}")

    elif user_choice == "4":
        display_pass_fail(marks)

    elif user_choice == "5":
        results_table(marks, grades)

    elif user_choice == "6":
        print("Exiting program")
        break

    else:
        print("Invalid choice! Try again.")

print("Thanks for using gradebook analyzer. Hope you like it!!")




















