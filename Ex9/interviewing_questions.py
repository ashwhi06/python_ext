# 1. Write an algorithm that checks if a string contains another string.
# If it does, return True; otherwise, return False.
# Example: When checking if string "Hello world" contains "Hello", the function should return True. 
# If checking if the same string contains "Bye", the function should return False.

def string_contains(string, substring):
    if substring in string:
        return True
    else:
        return False

string = "Hello world"
print("Does this string container the correct value:", string_contains(string, "Hello"))
print("Does this string container the correct value:",string_contains(string, "Bye"))

# 2. Write a recursive function that takes in a number and returns the sum of the numbers from 0 to the number.
# Example: if the input is 5, the expected output would be 15 (5+4+3+2+1 = 15).

def sum_to_number(number):
    if number == 0:
        return 0
    else:
        return number + sum_to_number(number-1)
print("Sum of the numbers from 0 to the number:",sum_to_number(5))

# 3. Write a function that takes in a string and returns the string reversed.
# Example: if the input is "hello", the expected output would be "olleh".

def reverse_string(string):
    if len(string) == 0:
        return ""
    else:
        return reverse_string(string[1:]) + string[0]
print("Reversed string:",reverse_string("hello"))

# 4. Write a recursive function that takes in a list of strings and returns the words capitalized.
# Example: if the input is ['pandas', 'monkeys', 'koalas', 'kangaroos'], then the expected output would be PANDAS MONKEYS KOALAS KANGAROOS.

def capitalize_words(list_of_words):
    if len(list_of_words) == 0:
        return ""
    else:
        return list_of_words[0].capitalize() + " " + capitalize_words(list_of_words[1:])
print("Capitalized words:",capitalize_words(["pandas", "monkeys", "koalas", "kangaroos"]))

# 5. Write a function that takes in a list of numbers and returns the product of the numbers in the list.
# Example: if this input is [4, 3, 5], then the expected output would be 60 (4*3*5=60).

def product_of_numbers(list_of_numbers):
    if len(list_of_numbers) == 0:
        return 1
    else:
        return list_of_numbers[0] * product_of_numbers(list_of_numbers[1:])
print("Product of numbers:",product_of_numbers([4, 3, 5]))

# 6. Write an algorithm that prints the non-repeating integers in a list.
# Example: in a list of [1, 5, 1, 6, 8, 5], the expected output would be 6, 8.

def non_repeating_integers(list_of_integers):
    if len(list_of_integers) == 0:
        return []
    else:
        if list_of_integers[0] in list_of_integers[1:]:
            return non_repeating_integers(list_of_integers[1:])
        else:
            return [list_of_integers[0]] + non_repeating_integers(list_of_integers[1:])
print("Non-repeating integers:",non_repeating_integers([1, 5, 1, 6, 8, 5]))
