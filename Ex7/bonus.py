# python : Write a function that reverses the words in a string, "Hello World! How are you doing today?". Optimize your solution for the minimum number of loops
# Input: "Hello World! How are you doing today?"
# Output: "today? doing you are How !World Hello"

# def reverse_words(string):
#     return " ".join(string.split(" ")[::-1])
# print(reverse_words("Hello World! How are you doing today?"))

#Optimize your solution for the minimum number of loops

# def reverse_words(input_string):
#     words = input_string.split(" ")
#     start = 0
#     end = len(words) - 1
#     while start < end:
#         words[start], words[end] = words[end], words[start]
#         start += 1
#         end -= 1
#     return " ".join(words)
# print(reverse_words("Hello World! How are you doing today?"))

# import re

# def reverse_words_with_special_chars(input_str):
#     words_and_special_chars = re.findall(r'\w+|\W+', input_str)
#     reversed_str = ' '.join(reversed(words_and_special_chars))
#     return reversed_str
# # Example usage:
# input_str = "Hello World! How are you doing today?"
# print(reverse_words_with_special_chars(input_str))