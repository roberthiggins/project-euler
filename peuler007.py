'''
Created on 5/06/2013

@author: Robert Higgins

This is intended to solve problem 007 from Project Euler.

This is a simple enough problem to do by brute-force.  For a number as small
as 10000 we can happily check the primeness of each number with little regard
for time constraints.

'''

# Determines if a number is prime.  As all primes except for 2 must be odd we
# can avoid half the search space.
def is_prime(candidate):
    if candidate < 2: return False
    elif candidate == 2: return True
    elif candidate % 2 == 0: return False

    # A list comprehension here could use unnecessary memory
    for i in range(2, candidate):
        if i % 2 != 0 and candidate % i == 0:
            return False

    return True


def find_nth_prime(n): 
    prime_count = 0
    index = 0
    
    while prime_count < n:            
        prime_count = prime_count + 1 if is_prime(index) else prime_count
        index += 1
    
    return index - 1


if __name__ == '__main__':
    # Problem: find the 10,001st prime number.
    
    # Brute Force.  This is unacceptably slow and I will try another approach
    print('The 10,001st prime is', find_nth_prime(10001))
