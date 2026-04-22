# 1. VARIABLES & DATA TYPES

name = "Joe"       # string
age = 23           # integer
height = 5.4       # float
is_student = True   # boolean

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

# 8. CONDITIONAL STATEMENTS

print("\n Conditional Statements ")
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 9. NESTED CONDITIONAL STATEMENTS

print("\n Nested Conditional Statements ")

age = 25
has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"

if age >= 18:
    if has_id:
        print("Allowed to enter")
    else:
        print("ID required")
else:
    print("Not allowed")

# 10. MATCH CASE STATEMENT

day = input("Enter a day of the week: ").lower()

match day:
    case "monday":
        print("Start of week")
    case "friday":
        print("Weekend coming")
    case "sunday":
        print("Holiday")
    case _:
        print("Normal day")

# 11. FOR LOOP       

print("\n For Loop ")
for i in range(5):
    print(i)

# 12. WHILE LOOP

print("\n While Loop ")
count = 0

while count < 5:
    print(count)
    count += 1

# 13. LOOP CONTROL STATEMENTS

print("\n Loop Control Statements ")
for i in range(10):
    if i == 3:
        continue  # Skip the rest of the loop when i is 3
    if i == 7:
        break     # Exit the loop when i is 7
    print(i)

# 14. range() FUNCTION
print("\n Range Function ")
for i in range(1, 10, 2):
    print(i)    


# 15. FUNCTIONS DEFINITION & CALLING 

print("\n Functions ")

def greet(name):  #definition of function
    return f"Hello, {name}!"
print(greet("Alice"))  #calling the function

# 16. LAMBDA FUNCTION

print("\n Lambda Function ")
square = lambda x: x * x
print(square(5))

# 17. TYPES OF FUNCTIONS

#Built-in functions
print("Built-in function")
print(type(10))
print(len("hello"))

#user-defined functions

print("\n User-defined Function ")
def average(a, b):
    return (a + b) / 2

print(average(10, 20))

# 18. STRINGS

print("\n Strings ")
word1 = "Hello"
word2 = "Python"
print("Length of string:", len(word2))  # length of string
print(word1 + " " + word2)             # concatenation
print(word2[0])                       # index -> position
print(word2[0:3])                     # slicing a string str[start index:end index]
print(word2[-4:-2])                   # negative index slicing

# 19. LISTS

print("\n Lists ")

my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Accessing first element
print(my_list[-1]) # Accessing last element
print(len(my_list)) # Length of the list
my_list.append(6)  # Adding an element to the end of the list
print(my_list)
my_list.insert(2, 10)  # Inserting an element at index 2
print(my_list)
my_list.sort()  # Sorting the list  
print(my_list)
my_list.reverse()  # Reversing the list     
print(my_list)
