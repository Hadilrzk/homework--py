filename = "C:/Users/dell/Favorites/Documents/homework---py/grades-homework/grades.csv"
results = []    
with open(filename, "r") as f:
    for line in f:
        line = line.strip().split(",")
        name = line [0]
        grades = []
        for grade in line[1:]:
            grades.append(int(grade))
            avg = sum(grades) / len(grades) 
        if avg >= 50:
          status = "Pass"  
        else: "Fail"    
        results.append(f"{name},{avg:.2f},{status}")

filename2 = "C:/Users/dell/Favorites/Documents/homework---py/grades-homework/averages.csv" 
with open(filename2, "w") as f:
    for result in results:
        f.write(result + "\n")           



    

    
