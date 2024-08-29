"""
CMPS 6100  Lab 1
Author: Gabrielle Blahusiak
"""

### the only imports needed are here
import math
import time
###

def is_divisible_by(num, i):
    if num % i == 0:
        return True
    else:
        return False

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) +1):
        if num % i == 0:
            return False

    return True

def generate_primes(upper_bound):
    for num in range(2, upper_bound):
        if is_prime(num):
            print(num)

def count_primes(upper_bound):
    count = 0
    for num in range(2, upper_bound):
        if is_prime(num):
            count += 1
    return count

def generate_twin_primes(upper_bound):
    if upper_bound > 5:
        print((3, 5))
    for n in range(1, (upper_bound // 6) +1):
        prime1 = 6 * n - 1
        prime2 = 6 * n + 1
        if prime1 < upper_bound and is_prime(prime1) and prime2 < upper_bound and is_prime(prime2):
            print((prime1, prime2))

def count_twin_primes(upper_bound):
    twin_prime_count = 0
    if upper_bound > 5 and is_prime(3) and is_prime(5):
        twin_prime_count += 1
    for n in range(1, (upper_bound // 6) +1):
        prime1 = 6 * n - 1
        prime2 = 6 * n + 1
        if prime1 < upper_bound and is_prime(prime1) and prime2 < upper_bound and is_prime(prime2):
            twin_prime_count += 1
    return twin_prime_count
upper_bound = int(input("Enter the upper bound to generate twin primes: "))
start = time.time()
generate_twin_primes(upper_bound)
end = time.time()
elasped_time_ms = (end - start) * 1000
print("Elapsed Time: {:.2f} milliseconds".format(elasped_time_ms))
