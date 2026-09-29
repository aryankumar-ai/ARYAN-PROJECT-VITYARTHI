#STUDENT-ATTENDEANCE-MANAGEMENT

students = {}


def add_student():
    student_id = input("Enter student ID: ").strip()

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter student name: ").strip()
    course = input("Enter course/branch: ").strip()

    if name == "" or course == "":
        print("Name and course cannot be empty.")
        return

    students[student_id] = {
        "name": name,
        "course": course,
        "attendance": []
    }

    print("Student added successfully.")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\n--- Student List ---")

    for student_id, student in students.items():
        print("ID:", student_id)
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("--------------------")


def mark_attendance():
    if not students:
        print("No students available.")
        return

    student_id = input("Enter student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    status = input("Enter attendance (P/A): ").strip().upper()

    if status not in ["P", "A"]:
        print("Please enter P for Present or A for Absent.")
        return

    students[student_id]["attendance"].append(status)

    if status == "P":
        print("Attendance marked as Present.")
    else:
        print("Attendance marked as Absent.")


def view_report():
    student_id = input("Enter student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]
    attendance = student["attendance"]

    total_classes = len(attendance)
    present = attendance.count("P")
    absent = attendance.count("A")

    if total_classes > 0:
        percentage = (present / total_classes) * 100
    else:
        percentage = 0

    print("\n--- Attendance Report ---")
    print("Student ID:", student_id)
    print("Name:", student["name"])
    print("Total Classes:", total_classes)
    print("Present:", present)
    print("Absent:", absent)
    print("Attendance:", round(percentage, 2), "%")


def main():
    while True:
        print("\n===== Student Attendance Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Mark Attendance")
        print("4. View Attendance Report")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            mark_attendance()

        elif choice == "4":
            view_report()

        elif choice == "5":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please try again.")


main()