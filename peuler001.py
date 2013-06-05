'''
Created on 3/06/2013

@author: Robert Higgins

This is intended to solve problem 001 from Project Euler.

A trivial example it can be solved with brute force. I intend this module to
have multiple solutions to the problem. For the moment I will stick with the
quickest solution I developed.

'''


# Find all the multiples of the factor up and including the limit. 
def find_multiples(limit, factor):
    
    if factor <= 0 or limit <= 0: return {}
    
    return set(i for i in range(0, limit) if i % factor == 0)
    

if __name__ == '__main__':
    
    # Problem: Find the sum of all multiples of members of the set {3,5} less
    # than 1000.
    limit = 1000
    factors = {3, 5}
    
    # Solution 01: Brute force
    multiples = set()
    
    for f in factors:
        multiples.update(find_multiples(limit, f))
     
    brute_force = sum(multiples)
    # Solution 01

    
    
    print('The sum of all multiples of 3 and 5 less than 1000:', brute_force)
    
