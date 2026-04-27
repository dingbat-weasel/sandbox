'''

input read character by character
no state

luhn formula:
double the value of every other digit
    starting at far right digit
sum all digits individually
    if '6' is doubled to '12', take sum of '1' and '2' = '3'
id is valid if value % 10 == 0

check digit is inserted at end of checksum to make total % 10 == 0

write a program that takes an id of arbitrary length
and determines if it is valid.
must process each char before reading the next one

sub-problems:
    - doubling the right digits
        - input will be read left to right, but we need to know the values
        right to left to know which to double
        - input is of arbitrary length
    - handling doubled digits 10 or greater
    - knowing we've reached the end of the number
    - need to read each digit one by one

will handle sub problems individually, then work to combine
'''


def sumDouble(n: int):
    double = n * 2
    if double >= 10:
        sum = 1 + double % 10
    else:
        sum = double
    return sum

'''
for fun, and to replicate the problem in the book, which is being solved with
c++, i will parse the input using ord() and an ascii handler, rather than int()
- also we may need to handle whitespace intentionally, which int() does not
'''

def charToInt(digit: str) -> int:
    sum = ord(digit) - ord('0')
    return sum

'''
which digits to double?
- try limited to fix length (simple checksum validation: fixed length)
    - even w/o doubling first to further simplify
    - takes an id number including check digit, of len 6
    - determines whether number is valid under simple sum & % 10 check
    - then check while doubling for fixed length:
        - len 6, double index 1, 3, 5
            - i % 2 == 0
        - then any even length number
- then of arbitrary length (luhn checksum validation: fixed length)
'''
import sys


def validation():
    position = 1
    evenLengthChecksum = 0
    oddLengthChecksum = 0
    ascii_offset = ord('0')
    print('Enter a number: ')
    digit = sys.stdin.read(1)
    digit_ascii = ord(digit)
    while (digit_ascii != 10):
        if position % 2 == 0:
            evenLengthChecksum += digit_ascii - ascii_offset
            oddLengthChecksum += sumDouble(digit_ascii - ascii_offset)
        else:
           evenLengthChecksum += sumDouble(digit_ascii - ascii_offset)
           oddLengthChecksum += digit_ascii - ascii_offset
        print(digit, evenLengthChecksum, oddLengthChecksum)
        print(position)
        digit = sys.stdin.read(1)
        digit_ascii = ord(digit)
        position += 1
    print(f'odd length checksum: {oddLengthChecksum}, even length checksum: {evenLengthChecksum}')
    if (position - 1) % 2 == 0:
        checksum = evenLengthChecksum
    else:
        checksum = oddLengthChecksum
    print(f'checksum: {checksum}')
    if checksum % 10 == 0:
        print('Valid')
    else:
        print('Invalid')

'''
this will create an continuous input that prints the ascii value of any
character, including whitespace/newline (10)
'''
def whitespace():
    while True:
        digit = sys.stdin.read(1)
        if not digit:
            break
        # if digit.isspace():
            # print(f'\nEnd of input detected via whitespace: {digit}')
        print(ord(digit))




