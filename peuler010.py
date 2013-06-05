'''
Created on 5/06/2013

@author: Robert Higgins

This is intended to solve problem 010 from Project Euler.

'''

# Finds all the prime numbers below limit and returns as a list.
#
# An implementation of the Sieve of Eratosthenes as found on the Wikipedia
# page of the same name.  Memory usage here might get out of hand for large
# limits though that number would have to be extraordinarily large. In such a
# case it would be better to segment the sieve into manageable chunks.
def sieve_of_eratosthenes(limit):
    candidates = [True for cand in range(0, limit)]
    first_p = 2  # values below index of first prime can be ignored
    for i in range(first_p, limit):
        if candidates[i]:
            p = 1
            j = i * i
            while j < limit:
                candidates[j] = False
                j = (i * i) + (p * i)
                p += 1
               
    return [i for (i, is_p) in enumerate(candidates) if is_p and i >= first_p]        

if __name__ == '__main__':
    # Problem: Find the sum of all primes below 2,000,000
    
    # Solution 01:   
    print('The sum of all primes below 2,000,000 is', \
          sum(sieve_of_eratosthenes(2000000)))   
