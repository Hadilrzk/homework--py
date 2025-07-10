filename = "C:/Users/dell/Favorites/Documents/homework---py/homework7/grades.csv"
with open(filename, "r") as f:
    lines = f.readlines()

results = []    
for line in lines:
    line = line.strip()
    if not line:
        continue
    par = line.split(',')
    if len(par) <4 :
        continue
    name = par[0]
    s1 = int(par[1])  
    s2= int(par[2])
    s3= int(par[3])

    avr = (s1+s2+s3)/3

    if avr >= 50:
        status = "Pass"
    else:
        status = "Fail"

    results.append(name + ',' +str(round(avr,2)) + ',' + status)
    filename2 = "C:/Users/dell/Favorites/Documents/homework---py/homework7/averages.csv"
    with open(filename2, "w") as f:
        f.write('Name, Average, Result\n')
        for result in results:
            f.write(result + "\n")

    
