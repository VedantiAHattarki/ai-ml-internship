Python basics

1.Variables:
-Variables are the names given to the memory location or data storage containers is known as variables 
-Identifiers are the names given to variables, functions, classes, etc.

2.Data Types:
Data Types are the type of data of a value that is stored in variable
Fundamental datatypes: integer,string,float,boolean,none 

3.Keywords & comments
-Keywords are the in-built words in python which cannot be used as variables or as identifiers in python and have a fixed meaning (reserved words)
EX:False, True, None, print,if, else ,and, or, not etc
-Comments are the sentences which are only meant for humans to understand the code and interpreter ignores it, written using # 

4.Style guide 
There are some rules for writing variables in python is style guide
ex: tot_price = 100 --> snake_case (_ is used) this is mostly recommended in python
totPrice = 100 --> camelCase (first letter of first word is small and first letter of second word is capital)
Totprice = 100 --> PascalCase (first letter of all words is capital)

5.Operators
-Operators are the symbols that are used to perform a specific operation between operands(variables) and values
Operators - arithmetic, relational or comparison, assignment, logical, bitwise , membership
-Operator Precedence is the priority of the operators
in an expression i.e if an expression contains more than 1 operator then operation should be performed based on precedence

6.Type conversion & Type casting
-Converting the type of data from one type to another
-Type conversion - implicit conversion i.e python does this conversion 
-Type casting - explicit conversion i.e user/developer writes the code

7.User Input
input() is the function that is used to take the input from the user

8.Conditional statements 
Conditional statements are used to check the statements according to the condition given such as if, if- elif, else
-Nesting - nesting is condition within another condition

9.Match case-alternative for if, elif, else
match - is used to match the variable
case - is the different conditions that are being matched

10.Loops in python
Loops are used to execute a block of code multiple times.
-for loop- is used when we know how many times to run
-while loop- is used when the condition is true

11.Loop control statements:
-break-stops the loop
-continue- skips the current iteration

12.range()- range function - is used to generate sequences 
-range(start,stop,step)

13.Functions in python
-Functions is a block of statement that perform a specific task or
-Functions are defined to perform a specific task using def keyword
-function def - in which we specify the task that a function should perform repeatedly
-function call - the section in which we call the function whenever it is necessary to perform that task
-Parameters -Parameters are variables defined in a function to receive values.
-Arguments - The values that are passed to the parameters are called as arguments.

14.types of functions: 
-built-in functions : print(),input(),type(),range(),
   functions that are built-in in python
-user defined functions : avg, sum, div calc, etc.,
   these are the functions that are defined by user
-lambda functions:
lambda function is the function that is defined using lambda keyword and 
used in simple single line function

15.Data structures:
-Strings - sequence of characters written in single, double, triple quotes
 (strings are immutable)
 Formatting in strings - creating dynamic strings i.e adding variables and values in strings 2 ways    - format(), f-strings

-List -  A list is a collection of multiple values stored in a single variable.
 It is a type of data structure and can store values of different data types
 It is mutable data structure
 Methods - append(),insert(),sort(),reverse()
 Loops using list are used to get the data from large records quickly.

-Tuples - Tuples - A tuple is a collection of multiple values stored in a single variable. 
It is a type of data structure and can store values of different data types and is immutable data structure. Methods of tuples are index, count etc

-Dictionary - A dictionary is a collection of key-value pairs stored in a single variable.
It is a type of data structure and can store values of different data types and is mutable data structure and unordered
Methods in dictionary are keys(),values(),items(),get(),update().

-Sets - A set is a collection of unique values stored in a single variable.
It is a type of data structure and can store values of different data types and is mutable but elements in set are immutable and is unordered
Methods in sets are add(),remove(),discard(),pop(),clear().
