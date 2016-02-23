#!/usr/bin/ruby -w
=begin
    Solution for Project Euler, problem 3, in ruby
=end


$primes = [2]

=begin
    Determine if candidate is a factor of goal

    Coerce the goal into a float and divide by candidate. If the result is an
    integer then the candiadte is a factor of goal.
=end
def is_factor(goal, candidate)
    return candidate != 0 && goal * 1.0 / candidate % 1 == 0
end

=begin
    Determine if a number is a prime
=end
def is_prime?(n, existing_primes=[])
  existing_primes.each { |prime| return false if n % prime == 0 }
  true
end

=begin
    Add another prime to the list of primes.

    We will build our list of primes dynamically as large limits will would mean
    we spend forever calculating primes we never use.
=end
def add_prime(limit=10000000)
    i = $primes[-1]
    while i <= limit * 1.0 do
        if i % 2 == 1 && is_prime?(i, $primes)
            $primes.push(i)
            return true
        end
        i +=1
    end
end

=begin Solution

1. Check for factors, starting with the smallest prime

2. If goal number is prime, add to list

3. If factor, add factor to the list. Replace original number with co-product

4. Else try again with next prime

5. Repeat until product is 0

6. Return the hightst prime factor

=end
def find_highest_prime_factor(goal)

    product = goal
    factors = []
    index = 0

    while product > 0 do

        if $primes.length >= index
            add_prime(goal)
        end

        if $primes.include? product
            factors.push(product)
            product = 0
        elsif is_factor(product, $primes[index])
            factors.push($primes[index])
            product /= $primes[index]
        end
        index +=1
    end

    return factors[-1]
end

if find_highest_prime_factor(13195) == 29
    puts find_highest_prime_factor(600851475143)
else puts 'Test failed'
end
