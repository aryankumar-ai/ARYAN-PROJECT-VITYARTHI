# Project Execution Report: Student Attendance Management System

## 1. Project Overview
* **Project Name**: Student Attendance Management System
* **Technology Stack**: Python 3.x (Procedural Programming, In-memory Data Structures)
* **Execution Period**: Standard Software Development Life Cycle (SDLC) Phase
* **Status**: Successfully Implemented & Tested

## 2. Execution Phases & Milestones

### Phase 1: Requirement Analysis & Design
* **Objective**: Identify the core pain points of manual attendance tracking and define the technical scope.
* **Deliverables**: Problem statement definition, system architecture design using nested Python dictionaries, and functional module scoping (`add_student`, `view_students`, `mark_attendance`, `view_report`).

### Phase 2: Core Development & Implementation
* **Objective**: Write clean, modular, and maintainable Python code for the command-line interface (CLI).
* **Key Implementation Steps**:
  * Developed the persistent loop `main()` function providing a user-friendly menu navigation system.
  * Implemented robust input validation checks (e.g., duplicate student ID prevention, empty field detection, and strict `P`/`A` status filtering).
  * Built real-time attendance ratio calculation logic with rounding precision.

### Phase 3: Testing & Quality Assurance
* **Objective**: Ensure software reliability and fault tolerance against malformed user inputs.
* **Testing Scenarios Executed**:
  * *Negative Testing*: Entered blank strings for names and courses; verified that error warnings appeared and state remained unchanged.
  * *Boundary Testing*: Requested attendance reports for students with zero classes logged; verified that division-by-zero exceptions were avoided by returning $0\%$ cleanly.
  * *State Persistence Testing*: Added multiple students and logged records across consecutive loops to verify in-memory dictionary stability.

### Phase 4: Documentation & Deployment Readiness
* **Objective**: Prepare all essential artifacts for GitHub repository publishing.
* **Generated Assets**:
  * `README.md`: Setup instructions, feature list, and usage guide.
  * `statement.md`: Problem definition and functional requirements.
  * `project_report.md`: Comprehensive engineering breakdown and technical review.
  * `project_execution_report.md`: Project lifecycle and milestone tracking.

## 3. Challenges & Resolutions
* **Challenge**: Potential crashes due to invalid choice inputs or missing student IDs during reporting/attendance marking.
* **Resolution**: Implemented strict membership checks (`if student_id not in students:`) and defensive conditional branches (`else:` handlers for menu choices) to ensure graceful failure recovery without terminating the application unexpectedly.

## 4. Conclusion & Future Roadmap
The project execution was completed successfully within scope. The system provides a strong foundation that can be expanded in future versions to include file I/O persistence (JSON/CSV) and graphical user interfaces (GUIs).