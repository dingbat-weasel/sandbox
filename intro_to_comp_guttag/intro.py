from math import sqrt
from functools import reduce

def largest_odd(x, y, z):
    ans = min(x, y, z)
    if x%2 != 0:
        ans = x
    if y%2 != 0 and y > ans:
        ans = y
    if z%2 != 0 and z > ans:
        ans = z
    print(ans)

def birthday():
    user_bday = input("Enter ur bday in mm/dd/yyyy: ")
    print(f"U were born in the year: {user_bday[-4:len(user_bday)]}")

def print_x():
    num_x = int(input("print how many times? "))
    to_print = ''
    num_iterations = 0
    while num_iterations < num_x:
        to_print = to_print + 'X'
        num_iterations = num_iterations + 1
        print(to_print)

def largest_odd_from_input():
    print("Please input 10 numbers.")
    usr_10 = []
    usr_odds = []
    loop = 1
    while loop < 11:
        usr_input = int(input(f"you're entering #{loop}: "))
        if usr_input%2 != 0:
            usr_odds.append(usr_input)
        loop = loop + 1
        usr_10.append(usr_input)
    print(usr_10)
    print(f"The largest odd you entered is: {max(usr_odds)}")

def cube_root(x: int):
    ans = 0
    while ans**3 < abs(x):
        ans = ans + 1
    if ans**3 != abs(x):
        print(x, 'is not a perfect cube')
    else:
        if x < 0:
            ans = -ans
        print(f'Cube root of {x} is {ans}')

def count_up(max_val):
    i = 0
    while i < max_val:
        i = i + 1
    print(i) #takes about 8 digits for there to be a pause

def prime_ee_v1(x: int):
    smallest_divisor = None
    largest_divisor = None
    for guess in range(2, x):
        if x%guess == 0:
            smallest_divisor = guess
            largest_divisor = x / smallest_divisor
            break
        
    if smallest_divisor != None:
        print(f'smallest divisor of {x} is {smallest_divisor}\nlargest divisor is {largest_divisor}')
    else:
        print(f'{x} is a prime number')

# faster but more complex code
def prime_ee_v2(x: int):
    smallest_divisor = None
    largest_divisor = None
    if x%2 == 0:
        smallest_divisor = 2
        largest_divisor = x / 2
    else:
        for guess in range(3, x, 2):
            if x%guess == 0:
                smallest_divisor = guess
                largest_divisor = x / smallest_divisor
                break
    if smallest_divisor != None:
        print(f'Smallest div of {x} is {smallest_divisor}\n largest div is {largest_divisor}')
    else:
        print(f'{x} is a prime')

def prime_sum():
    primes = []
    for x in range(3, 1000, 2):
        smallest_divisor = None
        for g in range(3, x, 2):
            if x%g == 0:
                smallest_divisor = g
                
                break
        if smallest_divisor != None:
            print(f'{x} is divisible by {smallest_divisor}')
        else:
            print(f'{x} is PRIME')
            primes.append(x)
    sum_primes = reduce(lambda x, y: x + y, primes)
    print(primes)
    print(sum_primes)

def root_check(x: int):
    for pwr in range(1, 6):
        root = 0
        while root**pwr < abs(x):
            root = root + 1
        if root**pwr != abs(x):
            print(f'{x} does not have a perfect {pwr}root')
        
        else:
            if x < 0:
                root = -root
            print(f'{root}^{pwr} = {x}')
      
def sqrt_ee(x):
    epsilon = 0.01
    step = epsilon**2
    num_guesses = 0
    ans = 0.0
    while abs(ans**2 - x) >= epsilon and ans <= x:
        ans += step
        num_guesses += 1
    print(f'number of guesses: {num_guesses}')
    if abs(ans**2 - x) >= epsilon:
        print(f'Failed on sqrt of {x}')
    else:
        print(f'{ans} is close to sqrt of {x}')
        