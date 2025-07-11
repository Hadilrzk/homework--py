import student

def main():
    student.init_file()
    students = student.read_students()

    while True:
        student.show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            student.add_student(students)
            students = student.read_students()

        elif choice == "2":
            name = input("Enter the Name of student to update: ")
            if student.update_student(students, name):
                print("Student updated successfully.")
                students = student.read_students()
            else:
                print("Student not found.")

        elif choice == "3":
            name = input("Enter the Name of student to delete: ")
            if student.delete_student(students, name):
                students = student.read_students()
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        elif choice == "4":
            name = input("Enter the Name of student to search: ")
            if not student.search_student(students, name):
                print("Student not found.")

        elif choice == "5":
            if not student.list_students(students):
                print("No students to list.")

        elif choice == "6":
            try:
                n = int(input("Enter N: "))
                if student.top_n_student(students, n):
                    print(f"Top {n} student(s) listed above.")
                else:
                    print("Error showing top students.")
            except:
                print("Invalid input.")

        elif choice == "7":
            try:
                count = int(input("Enter number of random students to add: "))
                if student.create_random_students(students, count):
                    print(f"{count} random student(s) added.")
                    students = student.read_students()
                else:
                    print("Failed to add random students.")
            except:
                print("Invalid input.")

        elif choice.lower() == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
