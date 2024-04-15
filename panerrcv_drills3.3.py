#Drill3.3
def is_prime(num): 
    if num < 2: 
        return False 
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0: 
            return False 
    return True 
 
def print_first_n_primes(n): 
    count = 0 
    num = 2 
    while count < n: 
        if is_prime(num): 
            print(num) 
            count += 1 
        num += 1 
        
x = int(input("Enter an integer:"))  
print_first_n_primes(x)

#Retrieved from https://www.quora.com/How-do-I-print-the-first-N-prime-numbers-in-Python