# PROGRAMMING PROJECT #1

# 1. Change the function name from sum to add.

# 2. In the renamed function, use a new variable to store the sum, and return this new variable.

# 3. Just before the print statement, use a variable to store the result of calling the add
#    function and change the print statement to output the sum using the new variable.

# 4. Change this program to multiply two numbers.

def multiply(a, b):
    product = a * b
    return product

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

total = multiply(a, b)
print(f'Sum of {a} and {b} is {total}')




