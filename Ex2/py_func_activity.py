#name_args- Accepts any number of named arguments and prints them in the pattern key :value one at a time.

def name_args(**kwargs):
    print("The following arguments were passed to the function:")
    for key, value in kwargs.items():
        print(key, ":", value)
        

# all_true- Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.
# def all_true(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True
def all_true(iterable):
    return all(iterable)

print(all_true([True, True, True]))

# one_true - Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.
# def one_true(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False
def one_true(iterable):
    return any(iterable)

print(one_true([True, False, True]))

# recursive_factorial- Uses recursion to find the factorial of an integer.
def recursive_factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

print(recursive_factorial(3))
print(recursive_factorial(5))
# recursive_deduplicate - Recursively removes all adjacent duplicate letters from a string.
# Input: AABBCCDD
# Output: ABCD
# def recursive_deduplicate(s):
#     if len(s) == 0:
#         return ""
#     elif len(s) == 1:
#         return s
##      Compares the characters in the string | checking the length of s
#     elif s[0] == s[1]:
##     use slice notation to start at 2
#         return recursive_deduplicate(s[1:])
#     else:
#         return s[0] + recursive_deduplicate(s[1:])

# print(recursive_deduplicate("AABBCCDD"))

def recursive_deduplicate(my_str,i=0):
  # if our string is empty or only has 1 thing, it's got no duplicates
  # if i is at the end of the string, no duplicates are left
  if len(my_str) <= 1 or i == len(my_str)-1:
    return my_str
  else:
    # str at current position is same as next position
    if my_str[i] == my_str[i+1]:
      return recursive_deduplicate(my_str[0:i]+my_str[i+1:],i)
    else:
      #no duplicate at current position, check next
      return recursive_deduplicate(my_str,i+1)
      
print(recursive_deduplicate("aaaa"))
print(recursive_deduplicate("aaba"))
print(recursive_deduplicate("AABBCCDD"))
print(recursive_deduplicate(""))
# recursive_reverse - Uses recursion to reverse a string.
def recursive_reverse(s):
    #base case
    if len(s) <= 1:
        return s
     #recursive case
    return s[-1] + recursive_reverse(s[:-1])
    
print(recursive_reverse("apple"))