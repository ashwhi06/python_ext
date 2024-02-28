
#1. What is the time complexity for function1?
def function1(values):
    #O(n)
  for value in values:
    print(value)

#Ans: The output scales based on the number of elements in the list. 
    # This means the function has linear complexity, O(n).

#2. What is the time complexity for function2?
def function2(values):
   #O(2)
  print(values[0])
  print(values[1])


#Ans: The values at index 0 and 1 stay the same regardless of whether the list size grows. 
    # Technically, adding each section would give us O(1) + O(1) = O(2), but O(2) is a constant, so we would be left with O(1). 
    # In other words, adding two constants results in a constant.
            
            

#3. What is the time complexity for function3?
def function3(values):
    #O(n^2)
  for x in values:
    for y in values:
      print(x, y)

#Ans:  Each value in the list has n outputs, so we have n*n = n^2 for the number of outputs. 
        # This means the function has quadratic complexity, O(n^2).


#4. What is the time complexity for function4?       
def function4(values):
    #O(4)
  for i in range(4):
    print("Python is great")
    #O(2)
  print("Software Engineering is awesome!")
  print("Software Engineering is awesome!")
    #O(n)
  for value in values:
    print(value)
    #O(n)
  for value in values:
    print(value)

#Ans: The time complexity is linear, O(n). 
    # When we break down each section, we have: O(4) + O(2) + O(n) + O(n) = 6 + O(2n). 
    # As n gets larger and larger (closer and closer to infinity), the dominant term we are left with is n. 
    # This is why the time complexity is linear, O(n).


#5. What would be the time and space complexity for the following algorithm? Why?

def function5(n):
    #O(n)
  test_list=[]
    #O(n)
  for num in range(n):
    test_list.append('add me')

  return test_list

print(function5(3))

#Ans: The time complexity is linear, O(n). O(n) + O(n)