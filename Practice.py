# This is a comment. Comments are written with a '#' symbol.

# Variables
x = 10  # Integer variable
y = 3.14  # Float variable
character = 'A'  # Character variable
name = "Abdullah"  # String variable
is_student = True  # Boolean variable

# Constants
PI = 3.14159  # Constant variable (written in uppercase)
CONST = 42

# Type conversion
num_str = "100"
num_int = int(num_str)  # Convert string to integer
num_float = float(num_str)  # Convert string to float

num = 'A'
num_int = int(A) # Wrong conversion

# Input and Output
print("Enter a number:")
number = input()
print("You entered:", number)

# Basic arithmetic operations
a = 15
b = 4
sum_result = a + b
diff_result = a - b
prod_result = a * b
div_result = a / b
mod_result = a % b
exp_result = a ** b
floor_div_result = a // b
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Division:", div_result)
print("Modulus:", mod_result)
print("Exponentiation:", exp_result)
print("Floor Division:", floor_div_result)

# Conditionals
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# Loops
for i in range(5):
    print("Iteration:", i)

count = 0
while count < 5:
    print("Count:", count)
    count += 1