Driill3.1
asterisk = int(input("Enter a number:"))
number = 1
while number <= asterisk:
    for j in range(0,cnt):
        print("*", end="")
        if (j != number):
            print(" ", end="")
    number = number + 1
    print()



#Drill3.2
rows = 3
columns = 5

for y in range(0,rows) :
    for x in range(0,columns) :
        if x%2 == 0:
            print("*", end="")
        else: 
            print("-", end="")
    print()



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


#Drill3.4
str = input("Enter a word: ")

previous_char_isvowel = False
curr_char = ""
current_char_isvowel = False
cnt = 0
syllable_cnt = 0

for c in str:
    curr_char = c
    if (c=="a") or (c=="e") or (c=="i") or (c=="o") or (c=="u") or (c=="y"):
        current_char_isvowel = True
    else:
        current_char_isvowel = False

    if cnt == 0:
        previous_char_isvowel = current_char_isvowel
        cnt = cnt + 1
        continue
    elif previous_char_isvowel and current_char_isvowel: 
        previous_char_isvowel = False
        continue
    elif previous_char_isvowel == False and current_char_isvowel == False:
        syllable_cnt = syllable_cnt + 1
        previous_char_isvowel = current_char_isvowel

if curr_char == "e": 
    syllable_cnt = syllable_cnt - 1
if syllable_cnt <= 0:
    syllable_cnt = 1
else:
    syllable_cnt = syllable_cnt + 1
    
print("Syllables: ", syllable_cnt)



#Drill3.5
rows = 11
columns = 20

for i in range(1,rows):
    for j in range(1,columns):
        if j == 1:                  
            print(i, end="")
        elif j == 3:             
            print(i*2, end="")
       elif j == 5:             
            print(i*3, end="")
        elif j == 7:      
            print(i*4, end="")
        elif j == 9:      
            print(i*5, end="")
        elif j == 11:      
            print(i*6, end="")
        elif j == 13:      
            print(i*7, end="")
        elif j == 15:      
            print(i*8, end="")
        elif j == 17:      
            print(i*9, end="")
        elif j == 19:      
            print(i*10, end="")
        else:                       
            print(" ", end="")
    print("")



#Drill3.6
N = int(input("Enter an integer for the side length of the squares: "))

if N > 0:           
    for i in range(N):
        for a in range (N) :
            print("*", end="")
        print()
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == N or j == N or i == N//3 or j == N//3:
                print("x", end="")
            else:
                print("", end="")
        print()

#Retrieved from https://stackoverflow.com/questions/50090389/display-squares-of-asterisks-filled-and-hollow-side-by-side

#Drill3.7
N = int(input("Enter an integer for the side length of diamond: "))

if N > 0:           
    for i in range(N):
        for s in range (N - i) :
            print(" ", end="")
        for j in range((i * 2) - 1):
            print("*", end="")
        print()
    for i in range(N, 0, -1):
        for s in range (N - i) :
            print(" ", end="")
        for j in range((i * 2) - 1):
            print("*", end="")
        print()

#Retrieved from https://stackoverflow.com/questions/32613579/creating-a-diamond-pattern-using-loops