# 1. VARIABLES & DATA TYPES

name = "Joe"         # string
age = 23             # integer
height = 5.4         # float
is_student = True    # boolean

print("Variables & Data Types ")
print(name, age, height, is_student)



# 2. KEYWORDS 


print("\n Keywords Example ")

# Using 'for', 'in', 'range' etc are the keywords in python

print("Numbers from 1 to 5:")

for i in range(1, 6):
    print(i)



# 3. OPERATORS


print("\n Operators ")

a = 10
b = 5

# Arithmetic Operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Comparison Operators
print("a > b:", a > b)
print("a == b:", a == b)

# Logical Operators
print("a > 5 and b < 10:", a > 5 and b < 10)



# 4. TYPE CONVERSION (automatic)


print("\n Type Conversion")

x = 5
y = 2.5

result = x + y  # int + float → float
print("Result:", result)



# 5. TYPE CASTING


print("\n Type Casting ")

num = "10"
type_casting = int(num)

print("Type casted:", type_casting + 5)


# 6. INPUT + CONDITIONAL STATEMENTS


print("\n User Input & Conditions ")

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# 7. EXAMPLE

print("\n Student Grade Calculator ")

student_name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
else:
    grade = "C"

print(f"{student_name}, your grade is {grade}")