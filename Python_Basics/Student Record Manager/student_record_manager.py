"""

Mini project: Student Record Manager (Self Evaluation)

Objective:

Build a small console application to practice Python fundamentals using a real-world scenario.

Features:
- Create a console menu that runs in a loop until the user exits.
- Add a student record with name and marks
- View all student records
- Search a student by name
- Update a student’s marks
- Delete a student record
- Save records to a file
- Load records automatically when the program starts
- Handle invalid inputs gracefully

Rules:

- Use a class-based approach
- Use a list or dictionary for storage
- Use file handling for persistence

Bonus challenges:

- Show average, highest, and lowest marks
- Sort students by marks
- Add basic validation for inputs

"""

import os

DATA_FILE = "students.txt"

class StudentRecordManager:
    def __init__(self):
        self.students = self.load_records()

    # ---------------------------
    # File handling 
    # ---------------------------

    def load_records(self):
        data = {}
        try:
            with open(DATA_FILE, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        name, marks = line.split(",")
                        data[name] = float(marks)
        except FileNotFoundError:
            pass
        return data

    def save_records(self):
        with open(DATA_FILE, 'w') as file:
            for name, marks in self.students.items():
                file.write(f"{name},{marks}\n")

    def get_marks(self):
        while True:
            value = input("Enter the student's marks: ")
            try:
                return float(value)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def average_marks(self):
        if not self.students:
            print("No records available to calculate average.")
            return None
        return sum(self.students.values()) / len(self.students)
    
    def highest_marks(self):
        if not self.students:
            print("No records available to find highest marks.")
            return None
        return max(self.students.values())
    
    def lowest_marks(self):
        if not self.students:
            print("No records available to find lowest marks.")
            return None
        return min(self.students.values())
    
    def add_student(self):
        while True:
            name = input("Enter the student's name: ")

            if not name.replace(" ", "").isalpha():
                print("Error: Name should contain only alphabets.")
                continue
            if name in self.students:
                print(f"Student '{name}' already exists. Use update option to change marks.")
                return
            break

        marks = self.get_marks()
        self.students[name] = marks
        print(f"Student '{name}' added successfully with marks {marks}.")

    def view_students(self):
        if not self.students:
            print("No student records available.")
            return
        
        print("\nStudent Records:")
        for name, marks in self.students.items():
            print(f"{name}: {marks}")

    def search_student(self):
        while True:
            name = input("Enter the student's name to search: ")
            if not name.replace(" ", "").isalpha():
                print("Error: Name should contain only alphabets.")
                continue
            break

        if name in self.students:
            print(f"Student '{name}' found with marks: {self.students[name]}")
        else:
            print(f"Student '{name}' not found.")


    def update_marks(self):
        while True:
            name = input("Enter the student's name to update marks: ")
            if not name.replace(" ", "").isalpha():
                print("Error: Name should contain only alphabets.")
                continue

            break
        if name in self.students:
            marks = self.get_marks()
            self.students[name] = marks
            print(f"Marks for student '{name}' updated to {marks}.")
        else:
            print(f"Student '{name}' not found. Please add the student first.")


    def delete_student(self):
        while True:
            name = input("Enter the student's name to delete: ")
            if not name.replace(" ", "").isalpha():
                print("Error: Name should contain only alphabets.")
                continue
            break

        if name in self.students:
            del self.students[name]
            print(f"Student '{name}' deleted successfully.")
        else:
            print(f"Student '{name}' not found.")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

def main():

    manager = StudentRecordManager()

    while True:
        print("\nStudent Record Manager")
        print("----------------------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Show Average Marks")
        print("7. Show Highest Marks")
        print("8. Show Lowest Marks")
        print("9. Clear Screen")
        print("10. Exit")
        print("----------------------")

        choice = input("Enter your choice: ")

        if not choice.isdigit():
            print("Invalid input. Please enter a number corresponding to the menu options.")
            continue

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.view_students()
        elif choice == '3':
            manager.search_student()
        elif choice == '4':
            manager.update_marks()
        elif choice == '5':
            manager.delete_student()
        elif choice == '6':
            avg = manager.average_marks()
            if avg is not None:
                print(f"Average Marks: {avg:.2f}")
        elif choice == '7':
            high = manager.highest_marks()
            if high is not None:
                print(f"Highest Marks: {high:.2f}")
        elif choice == '8':
            low = manager.lowest_marks()
            if low is not None:
                print(f"Lowest Marks: {low:.2f}")
        elif choice == '9':
            manager.clear_screen()
        elif choice == '10':
            manager.save_records()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()