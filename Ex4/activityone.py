# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(num1, num2, num3):
    greatest_number= max(num1, num2, num3)
    return greatest_number
print(max_num(50, 1000, 4)) 

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(num_list):
    result = 1
    for num in num_list:
        result *= num
    return result

numbers = [5, 5, 5, 5]
print(mult_list(numbers)) 


# Write a Python function called rev_string() to reverse a string.
def rev_string(x):
    return x[::-1]
mytxt =rev_string("taylor smith")

print(mytxt)

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(number, start, end): 
     return start <= number <= end
print(num_within(3, 2, 4))  
print(num_within(3, 1, 3))  
print(num_within(10, 2, 5))  

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the 
#two numbers above it added together.
def pascal(n):
    def binomial_coefficient(n, k):
        if k == 0 or k == n:
            return 1
        return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)
    
    for i in range(n):
        print(" " * (n - i - 1), end="")
        for j in range(i + 1):
            print(binomial_coefficient(i, j), " ", end="")
        print()
pascal(1)
pascal(5)