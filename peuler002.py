'''
Created on 3/06/2013

@author: Robert Higgins

This is intended to solve problem 001 from Project Euler.

Like problem 001 this can be solved through brute force alone.

'''

# A brute force solution for the general problem of finding the sum of the
# even fibonacci numbers with values less than limit
def brute_force(limit):
    
    sum = 0
    for i in range(0, limit):
        f = fib(i)
        if f >= limit: break
        if f % 2 == 0: sum += f
        
    return sum


# Finds the nth fibonacci number where n = index
def fib(index):
    
    assert (index >= 0)

    if index < 2: return index
    
    prev = 1
    value = 1
    for i in range(2, index):
        tmp = value
        value += prev
        # TODO How best to limit the potential size of the long?
        prev = tmp
    
    return value
    

if __name__ == '__main__':
    # Problem: Find the sum of the even fibonacci numbers with values less
    # than 4,000,000

    print('Sum of even fibonacci numbers less than 4,000,000:', \
          brute_force(4000000));
