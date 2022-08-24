# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

# range() returns the sequence of the given number between the given range

x = 1
y = 0

for i in range(51):
    if i == 0:
        fib = 0
    elif i == 1:
        fib = 1
    else:
        fib = x + y
        x = y
        y = fib
    print(f'term: {i} / number: {fib}')
