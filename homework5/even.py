def filter_even(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0 :
            even.append(num)
    return even    


List_Number  = [12,4,6,3,2,2,2,7,9,15,8,10,9]
x = filter_even(List_Number)
print(f"even numbers : {x}")       
    