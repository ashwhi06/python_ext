# 1. Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.
#Unsorted list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] Sorted list of tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
unsorted_list =[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] #key= 88, 90, 97, 82
sorted_list= sorted(unsorted_list, key=lambda score: score[1])
print(f"Sorted List:",sorted_list)

# 2. Write a lambda function to cube every element of a list.
# Original list: [3,6,9,2] List after lambda function: [27,216,729,8]
original_list= [3,6,9,2]
#takes each element x from the original list and cubes it.
cube = lambda num: num**3  
    #The map function applies this lambda function to each element of the original list, producing a new list containing the cubed elements.
result = list(map(cube, original_list))
print(f"List after lambda function:",result)

# 3. Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False.
#Input list: [3,6,9,2] List after lambda function and list comprehension: [False, True, False, True]
input_list= [3,6,9,2]
    #determine whether a number is even or odd
is_even = lambda input: input % 2 == 0 #lambda function checks if a number is divisible by 2, if yes, it is even, if not, it is odd
    #list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False
result = [is_even(input) for input in input_list]
print(f"List after lambda function and list comprehension:",result)

# 4. Use a list comprehension to create a list of the numbers from 1 to 100 (including 100).
range_list = [item for item in range(1,101)]
print(f"List of numbers from 1 to 100:",range_list)

# 5. Use a dictionary comprehension to count the length of each word in a sentence.
#Input: "The quick brown fox jumped over the fence." 
#output: {'The': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumped': 6, 'over': 4, 'the': 3, 'fence.': 6}
sentence = "The quick brown fox jumped over the fence."
length_of_words = {word: len(word) for word in sentence.split()} #iterates over each word in the list and creates a key:value where the key = word and the value is the len() of the word
print(f"Length of words in sentence:",length_of_words)