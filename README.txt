## Basic Information - Student DBMS

This Python application provides basic functionalities to manage students in a PostgreSQL database. It allows users to view all students, add a new student, update a student's email, or delete a student.

### Prerequisites

Before running the application, ensure you have the following:

- Python 3.x installed on your system.
- psycopg2 library installed. You can install it using pip: `pip install psycopg2`. (Make sure IDE PATH is activated in your IDE installation)

### Setup

1. Make sure you have PostgreSQL installed and running on your machine.
2. Create a database named `assignment3_q1`.
3. Set up a table named `students` in the `assignment3_q1` database with columns `student_id` (serial primary key), `first_name`, `last_name`, `email`, and `enrollment_date`. (script provided in Database_Setup_Query_Script.txt)

### Usage

1. Clone this repository to your local machine or download the `student_management.py` file.
2. Modify the database connection parameters (`dbname`, `user`, `password`, `host`, `port`) in the `connect_to_db()` function according to your PostgreSQL configuration.
3. Run the application by executing the 'assignment_3_q1.py' file.

### Functionality

The application provides the following functionalities:

1. **View all students:** Display all students currently stored in the database.
2. **Add a new student:** Add a new student to the database by providing their first name, last name, email, and enrollment date.
3. **Update a student's email:** Update the email of a student by providing their ID and the new email.
4. **Delete a student:** Delete a student from the database by providing their ID.
5. **Exit:** Exit the application.

### Running the Application

Run the 'assignment_3_q1.py' file. Follow the prompts displayed in your IDE terminal to navigate through different options and manage students as you wish.

### Contributors

- Pietro Adamvoski

### Video Link
https://youtu.be/vcrL29JiMhg


