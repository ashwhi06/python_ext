# In Python, you can implement a FILO (First In, Last Out) data structure, commonly known as a stack, using lists. 
# Lists in Python already have built-in methods that support FILO behavior. 
# You can use the append() method to add elements to the end of the list (push operation), and the pop() method to remove and return the last element of the list (pop operation).
# 
# Recursive take more memory and resources. Not as efficient as iterating. Only use for smaller parts
# def find_fact(num):
#     if num == 1:
#         return 1   
#     else:
#         return (num * find_fact(num-1))

# n = 7
# print(find_fact(n))

#What is the largest I can get is iterations
def find_fact(num):
    factorial = 1
    
    for i in range(1, num + 1):
        factorial = factorial * i
        
    return factorial
n=4
print(find_fact(n))