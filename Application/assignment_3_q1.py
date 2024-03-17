import psycopg2  # Import the psycopg2 library for interacting with PostgreSQL
from psycopg2 import sql  # Import the sql module from psycopg2 for SQL query composition


# Establish connection to PostgreSQL database
def connect_to_db():
    conn = psycopg2.connect( dbname="assignment3_q1", user="postgres", password="istanbul1958", host="localhost", port='5432' )
    return conn


# Retrieves and displays all records from the students table
def get_all_students():
    conn = connect_to_db() # Connect to Database
    cursor = conn.cursor() # Create Cursor
    cursor.execute("SELECT * FROM students")  # Display all records from the students table
    students = cursor.fetchall()  # Get all records returned by the query
    conn.close()  # Close the connection
    return students  # Return the fetched records


# Inserts a new student record into the students table
def add_student(first_name, last_name, email, enrollment_date):
    conn = connect_to_db() # Connect to Database
    cursor = conn.cursor() # Create Cursor
    insert_query = sql.SQL("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)")  # SQL query to insert a new student record
    cursor.execute(insert_query, (first_name, last_name, email, enrollment_date))  # Execute the query with arguments given
    conn.commit()  # Commit changes
    conn.close()  # Close the connection


# Updates the email address for a student with the specified student_id
def update_student_email(student_id, new_email):
    conn = connect_to_db() # Connect to Database
    cursor = conn.cursor() # Create Cursor
    update_query = sql.SQL("UPDATE students SET email = %s WHERE student_id = %s")  # SQL query to update student email record
    cursor.execute(update_query, (new_email, student_id))  # Execute the query with arguments given
    conn.commit()  # Commit changes
    conn.close()  # Close the connection


# Deletes the record of the student with the specified student_id
def delete_student(student_id):
    conn = connect_to_db() # Connect to Database
    cursor = conn.cursor() # Create Cursor
    delete_query = sql.SQL("DELETE FROM students WHERE student_id = %s")  # SQL query to delete a student record
    cursor.execute(delete_query, (student_id,))  # Execute the query with arguments given
    conn.commit()  # Commit changes
    conn.close()  # Close the connection


# User prompt provided to access different functionalities of the DBMS application
def main():
    # Display User Options
    while True:
        print("Choose desired option: ")
        print("1 - View all students")
        print("2 - Add a new student")
        print("3 - Update a student's email")
        print("4 - Delete a student")
        print("5 - Exit")

        ui = input("Enter choice (1-5): ")  # Prompt user to enter their choice

        if ui == "1":
            print("All student records: ")
            students = get_all_students()  # Retrieve all student records
            for student in students:
                print(student)  # Display each student record

        elif ui == "2":
            firstname = input("Enter student's first name: ")
            lastname = input("Enter student's last name: ")
            email = input("Enter student's email address: ")
            enrollment_date = input("Enter student's enrollment date (YYYY-MM-DD): ")
            add_student(firstname, lastname, email, enrollment_date)
            print("Student added successfully.")

        elif ui == "3":
            student_id = input("Enter the student ID of the student that you wish to change their email: ")
            new_email = input("Enter the new email for the student: ")
            update_student_email(student_id, new_email)
            print("Email updated successfully.")

        elif ui == "4":
            student_id = input("Enter the ID of the student record you want to delete: ")
            delete_student(student_id)
            print("Student deleted successfully.")

        elif ui == "5":
            print("Exiting...")
            break  # Exit the loop
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")  # Prompt user for valid input


if __name__ == "__main__":
    main()




