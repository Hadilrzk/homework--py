import total
temps = []
while True:
    user_input = input("enter temperature or 'q' to quit:").lower().strip()
    if user_input == "q":
        break
    try:
        temp = float(user_input)
        temps.append(temp)
    except Exception as e :
        print (f"An unexpected error occurred: {e}")
highest = temps[0]
lowest = temps[0]
for temp in temps:
    if temp > highest:
        highest = temp
    elif temp < lowest:
        lowest = temp
print(f"the highest value is {highest}")
print(f"the lowest value is {lowest}")

x  = len(temps)
total = total.sum(temps)
average = total / x
print(f"the average to 1 decimal place is  {average:.1f}")



