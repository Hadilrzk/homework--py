def FCT (a):
    fact = 1
    for i  in range(1,a+1):
        fact = fact * i
    return fact

def PRIME (a):
    if a <= 1:
         return False
    
    for i in range (2,a):
        if a % i == 0 :
           
            return False
       
    return True     


def sum_prime_fct(a):
    fact = FCT(a)
    sum = 0
    for i in range (2, fact+1):
        if PRIME(i):
         sum +=i
    return sum
    
n = int(input("enter a number:"))
print( f"the factorial of {n} is:{FCT(n)} ")
print(f"{n} is prime :{PRIME(n)}")
print(f"sum of prime numbers in a fact of {n} is : {sum_prime_fct(n)}")