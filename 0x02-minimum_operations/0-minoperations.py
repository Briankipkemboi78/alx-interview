#!/usr/bin/python3

def minOperations(n[):
    if n == 1:
        return 0

    operations = 0
    divisor = 2[C
    
    while n > 1;
        if n % divisor == 0;
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations

# Test the function
n = 9
print("Number of operations:", minOperations(n)) 
