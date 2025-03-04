
# Example 1: Using conditionals to check for names

names = ['evan', 'molly', 'hameed', 'khalil', 'jaydene']

for name in names:
    if name == 'molly':
        print(name.upper())
    elif name == 'khalil':
        print(name.title())
    elif name == 'hameed':
        print(name.split())
    elif name == 'jaydene':
        print(name.split())
    else:
        print(f"its none of the other names, so it must be {name}")


# Example 2: finding even numbers

for i in range(1, 101):
    if i % 2 == 0:
        print(f'{i} is even')
    # if it isn't even, we know it is odd, no extra check necessary
    else:
        print(f'{i} is odd')


# Example 3: (complex) finding prime numbers and their divisors

# begin loop similar to even check
for i in range(1, 101):
    # on each loop of outer loop, initialize an empty list
    divisors = []
    # loop through every number <= i
    for j in range(1, i + 1):
        # if i % j == 0, j is a divisor
        if i % j == 0:
            # append divisor to list
            divisors.append(j)
    # if the list length is 2 (1 and the number itself) number is prime
    if len(divisors) == 2:
        # divisors should always be [1, (whatever the number is)]
        print(f"{i} is prime: {divisors}")
