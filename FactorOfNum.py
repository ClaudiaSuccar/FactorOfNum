x = input('Enter a number 1-100: ') # User is prompted to enter a number they would like to find the factors of.
    
for num in range(1, 101): # The loop check numbers from 1 to 100.
    r = int(x) % int(num) # Modulo operator used to find remainder 'r'. Arguments converted to integer type.
    if r == 0: # num is a factor of x if the remainder 'r' is equal to 0
        print('[',num,']') # Factors of x are highlighted with brackets.
    else:
        print(num) # All other numbers that are not a factor of x are simply printed out.