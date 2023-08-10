#!/usr/bin/python3

""" Has a single character H with two operations: Copy All and Paste
    Give number n, write a method that calculates operations to result
    in exactly n H.
    Prototype: def minOperations(n)
    Return an integer
    if n is impossible to achieve, return 0
    """


def minOperations(n):
    if n == 1:
        return 0
    
    # Initialize the minimum operations for each index up to n
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        dp[i] = i  # Initialize with a value that is easy to beat
        
        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n]
