# Module B - Prime Check (maths/prime_check.py)
Tested by: Danish (24F-3037)

## What I looked at
The prime_check function checks whether an input integer is a prime number. It handles positive integers, even numbers, odd numbers, and non-prime edge cases such as 0, 1, and negative integers.

## ECP (equivalence classes)
prime_check(number)
- valid primes: numbers greater than 1 that have no divisors other than 1 and themselves (e.g., 2, 3, 5, 11, 97)
- valid composites: numbers greater than 3 that have additional factors (e.g., 4, 9, 100)
- invalid / special non-primes: zero (0), one (1), and all negative integers (e.g., -1, -5, -99)

## BVA (boundary values)
- lower non-prime bounds: -1, 0, 1 (1 is neither prime nor composite)
- smallest prime boundary: 2 (the only even prime)
- smallest composite boundary: 4
- upper values: large prime (97) and large composite (100)

## Things I noticed while testing
- The function handles 0, 1, and negative numbers cleanly by returning False rather than throwing an exception.
- Even numbers greater than 2 exit early, making small composites like 4 quick to return False.

## Test files
- tests_assignment/module_B_functions.py : tests for core function logic and standard prime/composite inputs
- tests_assignment/module_B_class.py : tests for boundary values (0, 1, negatives) and ECP edge cases
Run with: python -m pytest tests_assignment -v