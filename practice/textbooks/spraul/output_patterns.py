# only output '#' and \n

def triangle(val):
    for row in range(val):
        for i in range(1, 6 - row):
            print('#', end='')
        print()

def sideways(val):
    for row in range(1, val * 2):
        for i in range(0, val - (abs(val - row))):
            print('#', end='')
        print()

def count(val):
    for row in range(1, val + 1):
        print(4 - (abs(4 - row)))
