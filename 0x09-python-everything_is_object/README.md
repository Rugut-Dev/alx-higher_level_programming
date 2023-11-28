# Python - Everything is object

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

* Why Python programming is awesome
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address in the CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions

## Tasks

### 0. Who am I?
What function would you use to get the type of an object?

Write the name of the function in the file, without ().

### 1. Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

### 2. Right count
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 100

### 3. Right count=
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 89

### 4. Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a

### 5. Right count=+
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1

### 6. Is equal
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

### 7. Is the same
What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

....