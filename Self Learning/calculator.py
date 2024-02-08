a = float(input('Enter the first number '))
b = float(input('Enter the second number '))
opn = str(input('Enter an operator [(+,-,/,*,^) are supported as of now] '))

#Validating if the operator entries are are correct.
if opn not in ['+','-','/','*','^']:
    print('Invalid Operator Entered. Please try again. ')
    exit()

if opn == "+":
    print(f'The sum is {(a + b)}')
elif opn == "-":
    print(f'The difference between the numbers is {a - b}')
elif opn == "*":
    print(f'The product of the numbers is {a * b}')
elif opn == "/":
    if b == 0:
        print(f'Invalid Operation: Division by zero is not possible.')
        exit()
    else:
        print(f'{a} divided by {b} is {a/b}')
    exit()
elif opn == "^":
    print(f'The {a} powered to {b} is {a ** int(b)}')
exit()