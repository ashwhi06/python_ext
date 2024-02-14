# 1. Write a program that takes a positive number as an argument and prints the numbers from n to zero.
# Before we begin coding, we want to break down this problem and think about it recursively.
# We want to define a function that takes a number, let's say n , prints it, and calls itself again with the value of n-1. The function will keep calling itself until the base case is met.
# One way to do this is to determine if the number is equal to 0 and when it is, stop the function. 
# Think about what the base case and recursive case would be.
def print_numbers(n):
    #Base Case: If n equals 0, stop the function.
    if n < 0:
        return
    
    #recursive case
    print("Print number:", n) # print current number
    print_numbers(n-1) # call the function again going down with n-1

n =5
print_numbers(n)

#2. Write a function that prints the natural numbers from 1 to n.

def nat_num(t, current_number=1):
    #Base Case: If the number we are trying to print is greater than n, stop the function.
    if current_number > t:
        return
    #recursive case
    else:
        print("Current Number:", current_number)
        nat_num("Natural Number:",t, current_number+1)

#3. Write a function that returns the nth elements in the Fibonacci Sequence.
# The Fibonacci Sequence is the series of numbers where the next number is found by adding up the two numbers before it: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# For example, if n=4, then the result would be '2' and if n=2, the result would be '1'
# Here is more information on the Fibonacci Sequence.
# Hint: Look back at the factorial example as the structure of the algorithm may help you.

# def fib(n):
#    #Base Case: If the numerical input, n, is less than or equal to 1, return the value of n.
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

# print("First Fib is:",fib(2))
# print("Next Fib is:",fib(4))
# print("Last Fib is:",fib(8))

def fib(n):
    #Base Case: If the numerical input, n, is less than or equal to 1, return the value of n.
    if n <= 1:
        print("Do not pass me")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
 

#4. Write a function that calculates the value of 'a' to the power of 'b'.
# For example if a=2 and b=4, then power(2,4) would be calculating 2^4=2*2*2*2 so the result would be 16.
def power(a,b):
    #base case
    if b == 0:
        return 1
    #recursive case
    else:
        return a * power(a,b-1)
print("First Power is:", power(2,0))
print("Second Power is:", power(2,1))
print("Third Power is:", power(2,5))

#5.Write a function that checks whether a string is a palindrome or not. 
# The program should take in a string and return True if the string is a palindrome and False if not.
# A palindrome is a word that is the same when it is reversed, such as madam, radar, kayak, or tacocat.
def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and is_palindrome(string[1:-1])

print("Is madam a Palindrome",is_palindrome("madam"))
print("Is radar a Palindrome",is_palindrome("radar"))
print("Is kayak a Palindrome",is_palindrome("kayak"))
print("Is tacocat a Palindrome", is_palindrome("tacocat"))

#Bonus: Write a function that when given two numbers, finds their greatest common divisor.
# The greatest common divisor of two integers is the largest positive integer that divides both of the integers. 
# For example, look at the numbers 10 and 15: 10 can be divided by 1, 5, and 10, 15 can be divided by 1, 3, 5, and 15.
# When we say 'can be divided' here we mean divided evenly, so in other words there is no remainder. 
# For example when 15 is divided by 6, there is a remainder of 3 because 15=6(2)+3 so 6 is not a divisor of 15.
# The greatest common divisor of 15 and 10 is 5 since both numbers can be divided by 5.
def gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(10,15))