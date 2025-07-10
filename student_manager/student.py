import random
filename = "C:/Users/dell/Favorites/Documents/homework---py/student_manager/students.csv"
departments = ["CS", "Math","ST","Data science"]
names =["name12", "name14", "name45", "name55"]
surnames = ["Alice", "Bob", "Diana", "Evan"]
#random init file
def init_file():
    try:
        with open(filename, "r") as f:
            if f.read().strip() == "":
                return
    except:
        pass
    with open(filename, "w") as f:
        f.write("Surname, Name,Score,Department\n")  
        for _  in range(5):
            s = random.choice(surnames)
            n = random.choice(names)
            score = str((random.randint(0,100)))
            dept = random.choice(departments)
            f.write(f"{s},{n},{score},{dept}\n")

def read_students():
    with open(filename, "r") as f:
        lines = f.readlines
        for line in lines:
            return line.strip().split(',')
def write_student(students):
    with open(filename, "w") as f:
        f.write("surname,Name,Score,Departement\n")
        for s in students:
            f.write(",".join(s) + "\n")

def show_menu():
    print("\n-- STUDENT MANAGER--")
    print("1/ Add Student") 
    print("2/Update Student ") 
    print("3/ Delete Student") 
    print("4/ Search for a student") 
    print("5/List all students ") 
    print("6/ Top N Students ") 
    print("7/ Create Random student ") 
    print("8/ Randomize Only scores ") 
    print("q/  Quit") 

def create_student():
    s = input("Surname:")
    n = input("Name:")     
    sc = input("Score:")  
    dept = input("Department:")
    return [s,n,sc,dept]

def add_student(students):
    s = create_student()
    students.append(s)
    write_student(students)
    return 1

def update_student(students, name):
    for s in students:
        if s[1] == name:
            print("1. Update Surname")  
            print("2. Update score")
            print("3. Update department")    
            choice = input("your choice:")
            if choice == "1":
                s[0] = input("new surname:")      
            elif choice == "2":
                s[2] = input("new score:")    
            elif choice == "3":
                s[3] = input("new department")     
            write_student(students)
            return 1
    return 0

def delete_student(students, name):
    new_list = [ s for s in students if s[1] != name]
    if len(new_list) == len(students):
        return 0
    write_student(new_list)
    return 1

def search_student(students, name):
    for s in students:
        if s[1] == name:
            print("found:", ",".join(s))
            return 1
    return 0

def list_students(students):
    if not students:
        print("No students found")
        return 0
    for s in students:
        print(",".join(s))
    return 1

def top_n_student(students, n):
    try:
        #convert the score from string 
        for s in students:
            s[2] = int(s[2])

        top_student = []
        for _ in range(n):
            if not students:
                break
            #find student with max score 
            max = -1
            top = None
            for s in students:
                if s[2] > max:
                    max = s[2]
                    top = s
            if top:
                top_student.append(top)
                students.remove(top)
        # print top student
        for s in top_student:
            print(f"{s[0]}, {s[1]}, {s[2]}, {s[3]}")
        # convert score back to string
        for s in top_student + students:
            s[2] = str(s[2])     
        #add removed students back to original list
        students.extend(top_student)
        return 1
    except:
        return 0
    

def create_random_students(students, count):
    try:
        for _ in range(count):
            s= random.choice(surnames)
            n = random.choice(names)
            sc = str(random.randint(0,100))
            dept = random.choice(departments)
            students.append([s, n, sc, dept])
        write_student(students)
        return 1
    except:
        return 0
def randomize_score_only():
    try:
        students = read_students()
        for student in students:
            student[2] = str(random.randint(0,100))
        write_student(students)
        return 1
    except:
        return 0    



             
    


