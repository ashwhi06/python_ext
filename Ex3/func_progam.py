# 1. Write a function flatten_dict() to flatten a nested dictionary by joining the keys with . character.
# >>> flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}) {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}
# Hint: You can assume that all dictionary keys will be of type string, and that nested dictionaries will only be nested one layer deep (a dictionary of dictionaries will not have another dictionary nested inside it).
def flatten_dict(d):
    result = dict()
    for key, value in d.items():
        if isinstance(value, dict):
            for subkey, subvalue in flatten_dict(value).items():
                result[key + "." + subkey] = subvalue
        else:
            result[key] = value
    return result

print(f"Flatten Dictionary:" ,flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}))
    

# 2. Write a function unflatten_dict() to do reverse of flatten_dict.
# >>> unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}) {'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}
# Hint: You can assume that the keys for the dictionary will all be of type string, and that you never need to create more than one layer of nested dictionary. 
# It may be helpful to create an empty dictionary as the value for the outer key ('b' in this example), then fill it in iteratively as you find keys that belong to that dictionary.
def unflatten_dict(d):
    result = dict()
    for key, value in d.items():
        keys = key.split(".")
        current_dict = result
        for subkey in keys[:-1]:
            if subkey not in current_dict:
                current_dict[subkey] = dict()
            current_dict = current_dict[subkey]
        current_dict[keys[-1]] = value
    return result

print(f"Unflatten Dictionary:" ,unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}))
    
# 3. Write a function treemap() to map a function over nested list.
# >>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]) [1, 4, [9, 16, [25]]]
# Hint: Using recursion may make this function easier to code. 
# Don't forget to check the type of the element you are iterating over.
def treemap(func, lst):
   for i in range(len(lst)):
       if type(lst[i]) == list:
            lst[i] = treemap(func, lst[i])
       else:
            lst[i] = func(lst[i])
   return lst
    
print(f"TreeMap:", treemap(lambda i: i*i, [1, 2, [3, 4, [5]]]))
    
    
    
    
    
   
