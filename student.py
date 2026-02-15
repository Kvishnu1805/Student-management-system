import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS students(
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT,
            marks REAL
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def execute(self, query, values=()):
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor


class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks


class StudentManagementSystem:
    def __init__(self):
        self.db = Database()

    # CREATE
    def add_student(self):
        print("\n--- Add New Student ---")

        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        marks = float(input("Enter marks: "))

        student = Student(name, age, course, marks)

        query = """
        INSERT INTO students(name, age, course, marks)
        VALUES (?, ?, ?, ?)
        """

        self.db.execute(query, (student.name, student.age, student.course, student.marks))

        print("✅ Student added successfully.")

    # READ
    def view_students(self):
        print("\n--- Student List ---")

        query = "SELECT * FROM students"
        result = self.db.execute(query)

        students = result.fetchall()

        if not students:
            print("No students found.")
            return

        print("\nID | Name | Age | Course | Marks")
        print("-" * 40)

        for student in students:
            print(student[0], "|", student[1], "|", student[2], "|", student[3], "|", student[4])

    # UPDATE
    def update_student(self):
        print("\n--- Update Student ---")

        student_id = int(input("Enter student ID to update: "))

        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        course = input("Enter new course: ")
        marks = float(input("Enter new marks: "))

        query = """
        UPDATE students
        SET name=?, age=?, course=?, marks=?
        WHERE student_id=?
        """

        self.db.execute(query, (name, age, course, marks, student_id))

        print("✅ Student updated successfully.")


    # DELETE
    def delete_student(self):
        print("\n--- Delete Student ---")

        student_id = int(input("Enter student ID to delete: "))

        query = "DELETE FROM students WHERE student_id=?"

        self.db.execute(query, (student_id,))

        print("✅ Student deleted successfully.")

    # SEARCH (Real life feature)
    def search_student(self):
        print("\n--- Search Student ---")

        name = input("Enter student name: ")

        query = "SELECT * FROM students WHERE name LIKE ?"

        result = self.db.execute(query, ('%' + name + '%',))

        students = result.fetchall()

        if students:
            for student in students:
                print(student)
        else:
            print("Student not found.")

    # MENU
    def menu(self):
        while True:
            print("\n====== Student Management System ======")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Search Student")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.update_student()

            elif choice == "4":
                self.delete_student()

            elif choice == "5":
                self.search_student()

            elif choice == "6":
                print("Thank you for using system.")
                break

            else:
                print("Invalid choice.")



if __name__ == "__main__":
    system = StudentManagementSystem()
    system.menu()