[readme (1).md](https://github.com/user-attachments/files/32833059/readme.1.md)
# Student Attendance Management System

A simple, lightweight command-line application written in Python to manage student records and track their daily attendance efficiently.

---

## 🚀 Features

- **Add New Students**: Register students with a unique Student ID, Name, and Course/Branch.
- **View Student Directory**: Display a formatted list of all registered students.
- **Mark Attendance**: Record daily attendance using simple status indicators (`P` for Present, `A` for Absent).
- **Attendance Reporting**: Generate individual attendance reports showing total classes attended, total absences, and the overall percentage rounded to two decimal places.
- **Interactive CLI**: Easy-to-use menu-driven terminal interface.

---

## 🛠️ Prerequisites

Make sure you have **Python 3.x** installed on your machine. You can check your Python version by running:

```bash
python --version
```

---

## 📥 Installation & Running the Application

1. **Clone the repository** (or download the source code file):
   ```bash
   git clone https://github.com/your-username/student-attendance-system.git
   cd student-attendance-system
   ```

2. **Run the script**:
   ```bash
   python main.py
   ```

---

## 🧭 How to Use

When you launch the application, you will see the following interactive menu:

```text
===== Student Attendance Management System =====
1. Add Student
2. View Students
3. Mark Attendance
4. View Attendance Report
5. Exit
```

- **Option 1**: Enter the student's unique ID, full name, and course to register them.
- **Option 2**: View all currently saved students and their details.
- **Option 3**: Enter an existing student ID and input `P` or `A` to record attendance.
- **Option 4**: Enter a student ID to view their detailed attendance breakdown and percentage.
- **Option 5**: Exit the program.

---

## 📂 Code Structure

The project is structured cleanly using functional programming principles:
- `add_student()`: Handles validation and creation of new student records.
- `view_students()`: Iterates through the in-memory dictionary to display students.
- `mark_attendance()`: Appends attendance statuses to specific student records.
- `view_report()`: Computes attendance statistics and percentages.
- `main()`: Controls the application's interactive loop.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/student-attendance-system/issues).

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
