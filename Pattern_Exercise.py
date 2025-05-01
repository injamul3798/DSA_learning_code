# Problem 1: Pattern 1 - Print a rectangular grid of asterisks.
"""
Problem 1: Pattern 1 - Print a rectangular grid of asterisks.

Example for m=5, n=5:
*****
*****
*****
*****
*****
"""
def pattern1(m, n):
    for i in range(m):
        for j in range(n):
            print("*", end="")
        print("\n")


# Problem 2: Pattern 2 - Print an increasing triangle of asterisks.
"""
Problem 2: Pattern 2 - Print an increasing triangle of asterisks.

Example for m=5:
*
**
***
****
*****
"""
def pattern2(m, n):
    for i in range(m):
        for j in range(i + 1):
            print("*", end="")
        print("\n")


# Problem 3: Pattern 3 - Print an increasing triangle of numbers starting from 1.
"""
Problem 3: Pattern 3 - Print an increasing triangle of numbers starting from 1.

Example for m=5:
1
12
123
1234
12345
"""
def pattern3(m, n):
    for i in range(m):
        for j in range(i + 1):
            print(j + 1, end="")
        print("\n")


# Problem 4: Pattern 4 - Print an increasing triangle of numbers, where each line contains the same number repeated.
"""
Problem 4: Pattern 4 - Print an increasing triangle of numbers, where each line contains the same number repeated.

Example for m=5:
1
22
333
4444
55555
"""
def pattern4(m, n):
    for i in range(m):
        for j in range(i + 1):
            print(i + 1, end="")
        print("\n")


# Problem 5: Pattern 5 - Print a decreasing triangle of asterisks.
"""
Problem 5: Pattern 5 - Print a decreasing triangle of asterisks.

Example for m=5:
*****
****
***
**
*
"""
def pattern5(m, n):
    for i in range(m):
        for j in range(n - i):
            print("*", end="")
        print("\n")


# Problem 6: Pattern 6 - Print a decreasing triangle of numbers.
"""
Problem 6: Pattern 6 - Print a decreasing triangle of numbers.

Example for m=5:
12345
1234
123
12
1
"""
def pattern6(m, n):
    for i in range(m):
        for j in range(n - i):
            print(j + 1, end="")
        print("\n")


# Problem 7: Pattern 7 - Print an inverted pyramid of stars.
"""
Problem 7: Pattern 7 - Print an inverted pyramid of stars.

Example for m=5, n=9:
    *    
   ***   
  *****  
 ******* 
*********
"""
def pattern7(m, n):
    for i in range(m):
        # First spaces before star
        for j in range((n // 2) - i):
            print(" ", end="")
        # Print the star
        for k in range(2 * i + 1):
            print("*", end="")
        # Print the next spaces (Optional)
        for m in range((n // 2) - i):
            print(" ", end="")
        print()


# Problem 8: Pattern 8 - Print an inverted triangle pyramid of stars.
"""
Problem 8: Pattern 8 - Print an inverted triangle pyramid of stars.

Example for m=5, n=9:
*********
 ******* 
  *****  
   ***   
    *
"""
def pattern8(m, n):
    for i in range(m):
        # First spaces before star
        for j in range(i):
            print(" ", end="")
        # Print the star
        for k in range(n - (2 * i)):
            print("*", end="")
        # Print the next spaces (Optional)
        for m in range(i):
            print(" ", end="")
        print()


# Problem 9: Pattern 9 - Print two pyramids back-to-back.
"""
Problem 9: Pattern 9 - Print two pyramids back-to-back.

Example for m=5, n=9:
    *    
   ***   
  *****  
 ******* 
*********
*********
 ******* 
  *****  
   ***
    *
"""
def pattern9(m, n):
    mm = m
    nn = n

    # first print the first one
    for i in range(m):
        # First spaces before star
        for j in range((n // 2) - i):
            print(" ", end="")
        # Print the star
        for k in range(2 * i + 1):
            print("*", end="")
        # Print the next spaces (Optional)
        for m in range((n // 2) - i):
            print(" ", end="")
        print()

    # Print the second one
    for row in range(mm):
        # First spaces before star
        for x in range(row):
            print(" ", end="")
        # Print the star
        for y in range(nn - (2 * row)):
            print("*", end="")
        # Print the next spaces (Optional)
        for z in range(row):
            print(" ", end="")
        print()


# Problem 10: Pattern 10 - Print an hourglass shape of stars.
"""
Problem 10: Pattern 10 - Print an hourglass shape of stars.

Example for m=5, n=9:
*    
***   
*****  
*******
*********
*********
*******
*****
***
*  
"""
def pattern10(m, n):
    mm = m
    nn = n

    # first print the first one
    for i in range(m):
        # Print the star
        for k in range(2 * i + 1):
            print("*", end="")
        print()

    # Print the second one
    for row in range(mm):
        # Print the star
        for y in range(nn - (2 * row)):
            print("*", end="")
        print()


# Problem 12: Pattern 12 - Print an increasing triangle of numbers starting from 1.
"""
Problem 12: Pattern 12 - Print an increasing triangle of numbers starting from 1.

Example for m=5:
1
12
123
1234
12345
"""
def pattern11(m, n):
    for i in range(m):
        for j in range(i + 1):
            print(j + 1, end="")
        print("\n")


# Problem 13: Pattern 13 - Print an increasing triangle of alphabets.
"""
Problem 13: Pattern 13 - Print an increasing triangle of alphabets.

Example for m=5:
A
AB
ABC
ABCD
ABCDE
"""
def pattern12(m, n):
    for i in range(m):
        for j in range(i + 1):
            print(chr(65 + j), end="")
        print()


# Input for m and n
m, n = map(int, input().split())

# Calling the functions for each problem

# P1
pattern1(m, n)

# P2
pattern2(m, n)

# P3
pattern3(m, n)

# P4
pattern4(m, n)

# P5
pattern5(m, n)

# P6
pattern6(m, n)

# P7
pattern7(m, n)

# P8
pattern8(m, n)

# P9
pattern9(m, n)

# P11
pattern10(m, n)

# P12
pattern11(m, n)

# P13
pattern12(m, n)
