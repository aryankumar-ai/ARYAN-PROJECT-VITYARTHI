# Problem Statement: Student Attendance Management System

## 1. Introduction & Background
In many educational institutions and training centers, tracking student attendance manually using paper registers or disjointed spreadsheets is inefficient, prone to human error, and time-consuming. Instructors often struggle to quickly compute attendance percentages or retrieve historical attendance trends for individual students. 

## 2. Problem Definition
The objective is to design and implement a lightweight, console-based **Student Attendance Management System** in Python. The system must provide an intuitive interface for instructors to seamlessly perform core administrative tasks—registering students, marking daily attendance, and generating performance reports—without requiring a complex database setup.

## 3. Key Objectives & Functional Requirements
* **Record Management**: 
  * Allow the registration of students using a unique Student ID, Name, and Course/Branch.
  * Prevent duplicate student entries and handle empty input validation.
* **Attendance Tracking**: 
  * Enable quick daily attendance logging using binary status indicators (`P` for Present, `A` for Absent) mapped to specific student IDs.
* **Reporting & Analytics**: 
  * Compute total classes held, total present counts, total absences, and the final attendance percentage rounded to two decimal places for any given student.
* **User Experience (CLI)**: 
  * Provide a continuous, menu-driven command-line interface that allows users to perform multiple operations seamlessly until they choose to exit.

## 4. Target Audience
* Instructors, teachers, and trainers who need a fast, reliable, and straightforward tool to keep track of student attendance during sessions.