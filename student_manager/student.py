import random

filename = "C:/Users/dell/Favorites/Documents/homework---py/student_manager/students.csv"
departments = ["CS", "Math", "ST", "Data science"]

def init_file():
    try:
        with open(filename, "r") as f:
            if f.read().strip() != "":
                return
    except:
        pass

    with open(filename, "w") as f:
        f.write("Surname,Name,Score,Department\n")
        for i in range(5):
            s = f"Surname{i+1}"
            n = f"Name{i+1}"
            score = str(random.randint(0, 100))
            dept = random.choice(departments)
            f.write(f"{s},{n},{score},{dept}\n")

def read_students():
    students = []
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            for i in range(1, len(lines)):
                line = lines[i].strip()
                if line != "":
                    parts = line.split(",")
                    students.append(parts)
    except:
        pass
    return students

def write_student(students):
    with open(filename, "w") as f:
        f.write("Surname,Name,Score,Department\n")
        for i in range(len(students)):
            s = students[i]
            f.write(s[0] + "," + s[1] + "," + s[2] + "," + s[3] + "\n")

def show_menu():
    print("\n-- STUDENT MANAGER--")
    print("1/ Add Student") 
    print("2/ Update Student") 
    print("3/ Delete Student") 
    print("4/ Search for a student") 
    print("5/ List all students") 
    print("6/ Top N Students") 
    print("7/ Create Random student") 
    print("q/ Quit")

def create_student():
    s = input("Surname: ")
    n = input("Name: ")     
    sc = input("Score: ")  
    dept = input("Department: ")
    return [s, n, sc, dept]

def add_student(students):
    student = create_student()
    students.append(student)
    write_student(students)
    return 1

def update_student(students, name):
    name = name.lower()
    for i in range(len(students)):
        s = students[i]
        if s[1].lower() == name:
            print("1. Update Surname")  
            print("2. Update score")
            print("3. Update department")    
            choice = input("Your choice: ")
            if choice == "1":
                s[0] = input("New surname: ")      
            elif choice == "2":
                s[2] = input("New score: ")    
            elif choice == "3":
                s[3] = input("New department: ")     
            write_student(students)
            return 1
    return 0

def delete_student(students, name):
    name = name.lower()
    new_list = []
    found = False
    for i in range(len(students)):
        s = students[i]
        if s[1].lower() != name:
            new_list.append(s)
        else:
            found = True
    if found:
        write_student(new_list)
        return 1
    else:
        return 0

def search_student(students, name):
    name = name.lower()
    for i in range(len(students)):
        s = students[i]
        if s[1].lower() == name:
            print("Found:", s[0] + ", " + s[1] + ", " + s[2] + ", " + s[3])
            return 1
    return 0

def list_students(students):
    if len(students) == 0:
        print("No students found")
        return 0
    for i in range(len(students)):
        s = students[i]
        print(s[0] + ", " + s[1] + ", " + s[2] + ", " + s[3])
    return 1

def top_n_student(students, n):
    try:
        # Convert scores to int, strip whitespace first
        for i in range(len(students)):
            students[i][2] = int(students[i][2].strip())

        top_students = []
        temp_students = students[:]  # copy to avoid modifying original list
        count = 0

        while count < n and len(temp_students) > 0:
            max_score = -1
            top_index = -1
            for i in range(len(temp_students)):
                if temp_students[i][2] > max_score:
                    max_score = temp_students[i][2]
                    top_index = i
            if top_index >= 0:
                top_students.append(temp_students[top_index])
                del temp_students[top_index]
                count += 1
            else:
                break

        for i in range(len(top_students)):
            s = top_students[i]
            print(f"{s[0]}, {s[1]}, {s[2]}, {s[3]}")

        # Convert scores back to strings
        for i in range(len(students)):
            students[i][2] = str(students[i][2])
        for i in range(len(top_students)):
            top_students[i][2] = str(top_students[i][2])

        return 1
    except:
        return 0

def create_random_students(students, count):
    count2 = 0
    try:
        for i in range(count):
            s = f"Surname{count2}"
            n = f"Name{count2}"
            sc = str(random.randint(0, 100))
            dept = random.choice(departments)
            students.append([s, n, sc, dept])
            count2 += 1
        write_student(students)
        return 1
    except:
        return 0


