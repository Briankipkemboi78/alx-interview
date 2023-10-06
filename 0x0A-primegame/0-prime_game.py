#!/usr/bin/python3
""" Prime Game  """


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def isWinner(x, nums):
    if not nums or x <= 0:
        return None

    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        if prime_count % 2 == 0:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None