# Functional Prompt
# Implement a function that will flatten and sort an array of integers in ascending order, 
# and which adheres to a functional programming paradigm.

# Remember, when writing in a functional style:
# Keep variables immutable
# Write only pure functions
# Remember, functions may be higher order
# Once a functional solution to this problem has been implemented,
# answer the following questions.

# How does this solution ensure data immutability?
# Is this solution a pure function? Why or why not?
# Is this solution a higher order function? Why or why not?
# Would it have been easier to solve this problem using a different programming style?
# Why in particular is functional programming a helpful paradigm when solving this problem?

# 1. create a function that takes in an array of intergers in argument?
# 2. loop through input 
# 3. check if each element in input is in an ascending order

def flatten_and_sort(my_array): 
    flattened_array = []
    for sublist in my_array:
        for item in sublist:
            flattened_array.append(item)
    sorted_array = sorted(flattened_array)
    return sorted_array

result = flatten_and_sort([[10, 18], [100, 1, 50], [90, 87, 565]])
print(result)

# 1. How does this solution ensure data immutability?
# This solution ensures data immutability by not modifying input data, creating 
# new data structures for intermediate results, and ensuring the returned value 
# remains unchanged, the provided solution maintains data immutability throughout its execution. 

# 2. Is this solution a pure function? Why or why not?
# Yes, this solution is a pure function because my output produces
# the same elements that are in my input and also because 
# none of my variables are being modified outside of my flatten_and_sort function 

# 3. Is this solution a higher order function? Why or why not?
# No, this solution is not a higher order function because I did not create 
# more than one function or return a function as my result. 

# 4. Would it have been easier to solve this problem using a different programming style?
# Yes, the list comprehension programming style I feel would have been a easier method to solve this 
# problem easier. 

# 5. Why in particular is functional programming a helpful paradigm when solving this problem?
# Functional progamming is helpuful for solving this problem because I know that
# if I needed to flatten and sort a different array of numbers, all I would need to 
# do is change my num c bers and my function will produce the same evaluation 
# and this is because in functional progamming it always produces the same
# output for the same input.


# Object Oriented Prompt
# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to
# the following criteria.

# First, he'll need a general Podracer class defined with
# max_speed, condition (perfect, trashed, repaired) and price attributes.
# Define a repair() method that will update the condition of the podracer to "repaired".
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special
#  method called boost that will multiply max_speed by 2.
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
      
    def repair(self):
        self.condition = "repaired"
        print("Prodacer has been repaired")

class AnakinsPod(Podracer):
    def boost(self):
       self.max_speed *= 2
       print("Anakin's prodacer has been boosted! New max speed:", self.max_speed, "\U0001F4A8")

class SebulbasPod(Podracer):
  def flame_jet(self, other_podracer):
      other_podracer.condition = "trashed"
      print("Sebulba's podracer used flame jet! Your opponent podracer has been trashed \U0001F525")

pod = Podracer(max_speed=400, condition="damaged", price=30000)
print("Repair:", pod.condition)
pod.repair()
print("Repair:", pod.condition)

new_pod = AnakinsPod(max_speed=200, condition="good", price=100000)
print("Before boost:", new_pod.max_speed)
new_pod.boost()
print("After boost:", new_pod.max_speed)

third_pod = SebulbasPod(max_speed=600, condition="perfect", price=40000)
print("Before flame jet:", third_pod.condition)
third_pod.flame_jet(new_pod)
print("After flame jet:", new_pod.condition)


    
# Once an Object Oriented solution has been implemented, answer the following questions:

# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them,
# describe only those that apply)
# Encapsulation - Demonstrated within wrapping the methods within my functions.
# Inheritance - I reused the max_speed, condition, and price code from the main podracer. 
# Polymorphism - Demonstrated within the boost and flame_jet methods where they can be used interchangeably. 

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# No not necessairly because object oriented programming has all of the methods 
# that enabled me to solve the problem easier in my opinion. 

# How in particular did Object Oriented Programming assist in the solving of this problem?
# It allowed me to be able to reuse code so that I did not have to keep creating new
# functions and methods.

        